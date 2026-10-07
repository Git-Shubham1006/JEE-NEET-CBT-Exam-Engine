/**
 * ============================================================================
 * Official JEE Scoring & AI Diagnostic Metrics Engine
 * File: core/scoring-engine.js
 * ============================================================================
 * Default Marking Scheme (JEE Main):
 * - Correct: +4
 * - Incorrect (Single Correct): -1
 * - Unattempted / Marked for Review without answer: 0
 * - Answered & Marked for Review: Evaluated as answered
 */

import { NTA_STATES } from './question-state-machine.js';

export function evaluateStudentAttempt(questions = [], responsesMap = {}) {
    const summary = {
        totalQuestions: questions.length,
        attempted: 0,
        unattempted: 0,
        correctCount: 0,
        incorrectCount: 0,
        totalScore: 0,
        positiveMarks: 0,
        negativeMarks: 0,
        accuracyPercentage: 0,
        subjectWise: {
            PHYSICS: { attempted: 0, correct: 0, incorrect: 0, score: 0 },
            CHEMISTRY: { attempted: 0, correct: 0, incorrect: 0, score: 0 },
            MATHEMATICS: { attempted: 0, correct: 0, incorrect: 0, score: 0 }
        },
        aiDiagnostics: {
            timeWastedQuestions: [], // Questions with high time spent but negative result
            wildGuessCount: 0,
            percentileLostToNegative: 0
        }
    };

    questions.forEach((q) => {
        const resp = responsesMap[q.id];
        const subject = q.subject?.toUpperCase() || 'PHYSICS';
        const isAnsweredState = resp && (resp.state === NTA_STATES.ANSWERED || resp.state === NTA_STATES.ANSWERED_AND_MARKED);
        const hasSelection = resp && resp.selectedOption !== null && resp.selectedOption !== undefined && resp.selectedOption !== "";

        if (isAnsweredState && hasSelection) {
            summary.attempted++;
            summary.subjectWise[subject].attempted++;

            const isCorrect = String(resp.selectedOption).trim().toUpperCase() === String(q.correctAnswer).trim().toUpperCase();

            if (isCorrect) {
                summary.correctCount++;
                summary.positiveMarks += 4;
                summary.totalScore += 4;
                summary.subjectWise[subject].correct++;
                summary.subjectWise[subject].score += 4;
            } else {
                summary.incorrectCount++;
                summary.negativeMarks += 1;
                summary.totalScore -= 1;
                summary.subjectWise[subject].incorrect++;
                summary.subjectWise[subject].score -= 1;

                // AI Diagnostic check: If student spent > 240 seconds and got it wrong
                if (resp.timeSpentSeconds && resp.timeSpentSeconds > 240) {
                    summary.aiDiagnostics.timeWastedQuestions.push({
                        questionId: q.id,
                        subject: q.subject,
                        timeSpentSeconds: resp.timeSpentSeconds
                    });
                }
            }
        } else {
            summary.unattempted++;
        }
    });

    if (summary.attempted > 0) {
        summary.accuracyPercentage = Math.round((summary.correctCount / summary.attempted) * 100);
    }

    return summary;
}
