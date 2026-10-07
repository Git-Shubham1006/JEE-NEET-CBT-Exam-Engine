/**
 * ============================================================================
 * Drift-Free Exam Countdown Timer Engine
 * File: core/exam-timer-engine.js
 * ============================================================================
 * Standard setInterval(1000) causes 2-5 minutes of clock drift in throttled tabs.
 * This engine calculates remaining seconds from an epoch timestamp delta:
 * remainingSeconds = Math.max(0, Math.floor((endTimestamp - Date.now()) / 1000))
 */

export class ExamTimerEngine {
    /**
     * @param {number} durationMinutes - e.g. 180 for 3 hours
     * @param {Object} callbacks - { onTick(remainingSec, formatted), onWarning(minsLeft), onTimeUp() }
     * @param {number|null} existingEndTimestamp - Optional recovery timestamp from IndexedDB
     */
    constructor(durationMinutes = 180, callbacks = {}, existingEndTimestamp = null) {
        this.durationMinutes = durationMinutes;
        this.callbacks = Object.assign({
            onTick: () => {},
            onWarning: () => {},
            onTimeUp: () => {}
        }, callbacks);

        this.isRunning = false;
        this.timerHandle = null;
        this.warningFired = {};

        if (existingEndTimestamp && existingEndTimestamp > Date.now()) {
            this.endTimestamp = existingEndTimestamp;
        } else {
            this.endTimestamp = Date.now() + (durationMinutes * 60 * 1000);
        }
    }

    start() {
        if (this.isRunning) return;
        this.isRunning = true;
        this._tick(); // immediate first tick
        this.timerHandle = setInterval(() => this._tick(), 500); // 500ms check for high fidelity
    }

    pause() {
        this.isRunning = false;
        if (this.timerHandle) {
            clearInterval(this.timerHandle);
            this.timerHandle = null;
        }
    }

    getRemainingSeconds() {
        const deltaMs = this.endTimestamp - Date.now();
        return Math.max(0, Math.floor(deltaMs / 1000));
    }

    getFormattedTime() {
        const totalSec = this.getRemainingSeconds();
        const hrs = Math.floor(totalSec / 3600);
        const mins = Math.floor((totalSec % 3600) / 60);
        const secs = totalSec % 60;

        const pad = (n) => String(n).padStart(2, '0');
        return `${pad(hrs)}:${pad(mins)}:${pad(secs)}`;
    }

    getEndTimestamp() {
        return this.endTimestamp;
    }

    _tick() {
        const remaining = this.getRemainingSeconds();
        const formatted = this.getFormattedTime();

        this.callbacks.onTick(remaining, formatted);

        // Warning alerts at 15 mins and 5 mins
        if (remaining <= 900 && !this.warningFired[15]) {
            this.warningFired[15] = true;
            this.callbacks.onWarning(15);
        }
        if (remaining <= 300 && !this.warningFired[5]) {
            this.warningFired[5] = true;
            this.callbacks.onWarning(5);
        }

        if (remaining <= 0) {
            this.pause();
            this.callbacks.onTimeUp();
        }
    }
}
