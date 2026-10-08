/**
 * ============================================================================
 * Anti-Cheating & Live Proctoring Telemetry Engine
 * File: core/anti-cheating-proctor-engine.js
 * ============================================================================
 * Powers enterprise-grade examination integrity for CBT tests:
 * - Kiosk Full-Screen Lockdown & ESC Detection
 * - Tab-Switch & Window Blur Detection with duration tracking
 * - Clipboard (Copy/Cut/Paste) & Text Selection Lockout
 * - DevTools (F12, Inspect Element) Shortcut Disablement
 * - Superhuman Solving Speed & AI Behavioral Anomaly Detection
 * - Real-Time Inter-Tab Broadcast Telemetry & Remote Proctor Command Control
 */

const PROCTOR_CHANNEL_NAME = 'cbt_live_proctor_channel';

export class AntiCheatingProctorEngine {
    constructor(options = {}) {
        this.studentMeta = options.studentMeta || {
            studentId: 'STUDENT_DEFAULT',
            studentName: 'Shubham Kumar',
            rollNo: 'APEX-2026-1042',
            batch: 'JEE 2026 Dropper Elite'
        };
        this.testId = options.testId || 'JEE_MAIN_MOCK';
        this.maxViolations = options.maxViolations || 3;
        this.onViolation = options.onViolation || (() => {});
        this.onLockout = options.onLockout || (() => {});
        this.onProctorCommand = options.onProctorCommand || (() => {});

        this.violationsCount = 0;
        this.violationsLog = [];
        this.speedAnomalies = [];
        this.isLocked = false;
        this.isFrozen = false;
        this.isFullScreen = false;

        this.blurTimestamp = null;
        this.channel = null;
        this.heartbeatTimer = null;

        this.initChannel();
        this.bindSecurityEvents();
        this.startHeartbeat();
    }

    /**
     * Initializes BroadcastChannel & LocalStorage fallback for real-time inter-window telemetry
     */
    initChannel() {
        try {
            if (typeof window !== 'undefined' && 'BroadcastChannel' in window) {
                this.channel = new BroadcastChannel(PROCTOR_CHANNEL_NAME);
                this.channel.onmessage = (event) => this.handleProctorCommand(event.data);
            }
        } catch (e) {
            console.warn('BroadcastChannel not supported, falling back to storage sync.', e);
        }

        // Storage listener fallback
        if (typeof window !== 'undefined') {
            window.addEventListener('storage', (e) => {
                if (e.key === 'cbt_proctor_command_broadcast' && e.newValue) {
                    try {
                        const cmd = JSON.parse(e.newValue);
                        this.handleProctorCommand(cmd);
                    } catch (err) {}
                }
            });
        }
    }

    /**
     * Binds client security defense listeners (Tab switch, shortcuts, copy-paste)
     */
    bindSecurityEvents() {
        if (typeof window === 'undefined') return;

        // 1. Visibility & Tab Switch Detector
        document.addEventListener('visibilitychange', () => {
            if (document.hidden) {
                this.handleFocusLost('Tab Switch / Minimized Window');
            } else {
                this.handleFocusRegained();
            }
        });

        // 2. Window Blur / Focus Detector
        window.addEventListener('blur', () => {
            this.handleFocusLost('Window Blur / Switched Application');
        });

        window.addEventListener('focus', () => {
            this.handleFocusRegained();
        });

        // 3. Full-Screen Exit Detector
        document.addEventListener('fullscreenchange', () => {
            const isFull = !!document.fullscreenElement;
            this.isFullScreen = isFull;
            if (!isFull && !this.isLocked) {
                this.recordViolation('Exited Kiosk Full-Screen Mode', 'CRITICAL');
            }
        });

        // 4. Disable Right-Click Context Menu
        document.addEventListener('contextmenu', (e) => {
            e.preventDefault();
            this.recordViolation('Attempted Right-Click Context Menu', 'MINOR');
            return false;
        });

        // 5. Disable Text Selection & Clipboard (Copy/Cut/Paste)
        document.addEventListener('selectstart', (e) => {
            // Allow selection inside inputs only
            if (e.target.tagName !== 'INPUT' && e.target.tagName !== 'TEXTAREA') {
                e.preventDefault();
            }
        });

        document.addEventListener('copy', (e) => {
            e.preventDefault();
            this.recordViolation('Attempted Clipboard Copy (Ctrl+C)', 'MAJOR');
        });

        document.addEventListener('cut', (e) => {
            e.preventDefault();
            this.recordViolation('Attempted Clipboard Cut (Ctrl+X)', 'MAJOR');
        });

        document.addEventListener('paste', (e) => {
            e.preventDefault();
            this.recordViolation('Attempted External Paste (Ctrl+V)', 'MAJOR');
        });

        // 6. Block DevTools & Inspection Shortcuts
        window.addEventListener('keydown', (e) => {
            // F12 key
            if (e.key === 'F12') {
                e.preventDefault();
                this.recordViolation('Triggered DevTools Key (F12)', 'CRITICAL');
                return false;
            }

            // Ctrl+Shift+I, Ctrl+Shift+J, Ctrl+Shift+C (Inspect elements)
            if (e.ctrlKey && e.shiftKey && ['I', 'J', 'C', 'i', 'j', 'c'].includes(e.key)) {
                e.preventDefault();
                this.recordViolation('Triggered Browser Inspector Shortcut', 'CRITICAL');
                return false;
            }

            // Ctrl+U (View Source)
            if (e.ctrlKey && (e.key === 'u' || e.key === 'U')) {
                e.preventDefault();
                this.recordViolation('Triggered View Source (Ctrl+U)', 'MAJOR');
                return false;
            }

            // Ctrl+P (Print / Screen Grab)
            if (e.ctrlKey && (e.key === 'p' || e.key === 'P')) {
                e.preventDefault();
                this.recordViolation('Triggered Print Screen (Ctrl+P)', 'MINOR');
                return false;
            }
        });
    }

    handleFocusLost(reason) {
        if (this.isLocked || this.blurTimestamp) return;
        this.blurTimestamp = Date.now();
        this.recordViolation(reason, 'MAJOR');
    }

    handleFocusRegained() {
        if (!this.blurTimestamp) return;
        const durationSec = ((Date.now() - this.blurTimestamp) / 1000).toFixed(1);
        this.blurTimestamp = null;

        // Log duration of focus loss
        if (this.violationsLog.length > 0) {
            const lastViolation = this.violationsLog[this.violationsLog.length - 1];
            lastViolation.duration = `${durationSec}s`;
        }
        this.broadcastTelemetry();
    }

    /**
     * Records an infraction, increments strikes, triggers callback, and checks lockout threshold
     */
    recordViolation(reason, severity = 'MAJOR') {
        if (this.isLocked) return;

        this.violationsCount++;
        const violationRecord = {
            id: `VIOL_${Date.now()}_${Math.random().toString(36).substr(2, 4)}`,
            timestamp: new Date().toLocaleTimeString(),
            timestampEpoch: Date.now(),
            reason,
            severity,
            strikeNumber: this.violationsCount,
            duration: 'Active'
        };

        this.violationsLog.push(violationRecord);

        // Notify client listener
        this.onViolation({
            strikeNumber: this.violationsCount,
            maxAllowed: this.maxViolations,
            violation: violationRecord,
            isLocked: this.violationsCount >= this.maxViolations
        });

        this.broadcastTelemetry();

        // Lockout evaluation
        if (this.violationsCount >= this.maxViolations) {
            this.lockoutExam(`Exceeded maximum allowed security violations (${this.maxViolations}/${this.maxViolations}). Reason: ${reason}`);
        }
    }

    /**
     * AI Anomaly Detection: Checks if a question was answered with superhuman velocity
     */
    trackQuestionVelocity(qId, difficulty, timeSpentSeconds, isCorrect) {
        // Threshold: A HARD question solved in <8 seconds with correct answer indicates external key
        if (difficulty === 'HARD' && timeSpentSeconds < 8 && isCorrect) {
            const anomaly = {
                questionId: qId,
                difficulty,
                timeSpentSeconds,
                timestamp: new Date().toLocaleTimeString(),
                flag: '🚨 Superhuman Answering Velocity (<8s on HARD problem)'
            };
            this.speedAnomalies.push(anomaly);
            this.recordViolation(`AI Anomaly: Solved HARD Q [${qId}] in ${timeSpentSeconds}s (Suspected Key Leak)`, 'CRITICAL');
        } else if (difficulty === 'MEDIUM' && timeSpentSeconds < 4 && isCorrect) {
            const anomaly = {
                questionId: qId,
                difficulty,
                timeSpentSeconds,
                timestamp: new Date().toLocaleTimeString(),
                flag: '⚡ Rapid Guess Velocity (<4s on MEDIUM problem)'
            };
            this.speedAnomalies.push(anomaly);
        }
        this.broadcastTelemetry();
    }

    /**
     * Locks out the examination session immediately
     */
    lockoutExam(reason) {
        this.isLocked = true;
        this.onLockout(reason);
        this.broadcastTelemetry('TERMINATED');
    }

    /**
     * Requests Full-Screen Kiosk Mode
     */
    requestKioskMode() {
        if (typeof document !== 'undefined' && document.documentElement.requestFullscreen) {
            return document.documentElement.requestFullscreen()
                .then(() => {
                    this.isFullScreen = true;
                    this.broadcastTelemetry();
                    return true;
                })
                .catch(err => {
                    console.warn('Full-screen request denied or user cancelled:', err);
                    return false;
                });
        }
        return Promise.resolve(false);
    }

    /**
     * Handles remote commands sent by the faculty proctor from institute-admin.html
     */
    handleProctorCommand(cmd) {
        if (!cmd) return;
        // Verify target: broadcast or matches this student's ID/rollNo
        const matchesTarget = !cmd.targetStudentId || 
            cmd.targetStudentId === 'ALL' || 
            cmd.targetStudentId === this.studentMeta.studentId || 
            cmd.targetStudentId === this.studentMeta.rollNo;

        if (!matchesTarget) return;

        switch (cmd.type) {
            case 'PROCTOR_WARNING':
                this.onProctorCommand({
                    type: 'WARNING',
                    message: cmd.message || '⚠️ Proctor Alert: Discontinue unauthorized activity immediately.'
                });
                break;
            case 'PROCTOR_FREEZE':
                this.isFrozen = true;
                this.onProctorCommand({
                    type: 'FREEZE',
                    message: '⏸️ Examination Frozen by Institute Proctor. Awaiting verification.'
                });
                break;
            case 'PROCTOR_UNFREEZE':
                this.isFrozen = false;
                this.onProctorCommand({
                    type: 'UNFREEZE',
                    message: '▶️ Examination Resumed by Institute Proctor.'
                });
                break;
            case 'PROCTOR_TERMINATE':
                this.lockoutExam(`Disqualified by Institute Proctor: ${cmd.message || 'Disciplinary violation'}`);
                break;
        }
    }

    /**
     * Broadcasts live telemetry packet to the Proctor Radar in institute-admin.html
     */
    broadcastTelemetry(overrideStatus = null) {
        let status = 'NORMAL';
        if (this.isLocked || overrideStatus === 'TERMINATED') {
            status = 'TERMINATED';
        } else if (this.violationsCount >= 2 || this.speedAnomalies.length > 0) {
            status = 'CRITICAL';
        } else if (this.violationsCount === 1) {
            status = 'WARNING';
        }

        const telemetryPacket = {
            studentId: this.studentMeta.studentId,
            studentName: this.studentMeta.studentName,
            rollNo: this.studentMeta.rollNo,
            batch: this.studentMeta.batch,
            testId: this.testId,
            status,
            violationsCount: this.violationsCount,
            violationsLog: [...this.violationsLog],
            speedAnomalies: [...this.speedAnomalies],
            isFullScreen: this.isFullScreen,
            isFrozen: this.isFrozen,
            isLocked: this.isLocked,
            lastPing: Date.now(),
            lastPingTime: new Date().toLocaleTimeString()
        };

        // Broadcast to BroadcastChannel
        if (this.channel) {
            this.channel.postMessage({ type: 'TELEMETRY_PING', packet: telemetryPacket });
        }

        // Broadcast to LocalStorage shared bus
        if (typeof localStorage !== 'undefined') {
            localStorage.setItem('cbt_active_proctor_telemetry', JSON.stringify(telemetryPacket));
        }
    }

    /**
     * Starts background telemetry heartbeat (pings proctor every 3 seconds)
     */
    startHeartbeat() {
        if (typeof window === 'undefined') return;
        this.heartbeatTimer = setInterval(() => {
            this.broadcastTelemetry();
        }, 3000);
    }

    destroy() {
        if (this.heartbeatTimer) clearInterval(this.heartbeatTimer);
        if (this.channel) this.channel.close();
    }
}
