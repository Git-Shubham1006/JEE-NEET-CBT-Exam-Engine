/**
 * ============================================================================
 * Official NTA JEE 5-State Response Machine
 * File: core/question-state-machine.js
 * ============================================================================
 * Strict adherence to official NTA examination rules:
 * - State 0: Not Visited (Silver / White / Gray)
 * - State 1: Not Answered (Red / Orange)
 * - State 2: Answered (Green) -> Evaluated
 * - State 3: Marked for Review without answer (Violet / Purple) -> Not Evaluated
 * - State 4: Answered & Marked for Review (Violet with Green Dot) -> Evaluated
 */

export const NTA_STATES = Object.freeze({
    NOT_VISITED: 0,
    NOT_ANSWERED: 1,
    ANSWERED: 2,
    MARKED_FOR_REVIEW: 3,
    ANSWERED_AND_MARKED: 4
});

export const NTA_STATE_METADATA = Object.freeze({
    [NTA_STATES.NOT_VISITED]: {
        label: "Not Visited",
        cssClass: "nta-not-visited",
        color: "#e2e8f0",
        evaluated: false
    },
    [NTA_STATES.NOT_ANSWERED]: {
        label: "Not Answered",
        cssClass: "nta-not-answered",
        color: "#ef4444",
        evaluated: false
    },
    [NTA_STATES.ANSWERED]: {
        label: "Answered",
        cssClass: "nta-answered",
        color: "#22c55e",
        evaluated: true
    },
    [NTA_STATES.MARKED_FOR_REVIEW]: {
        label: "Marked for Review",
        cssClass: "nta-marked-review",
        color: "#8b5cf6",
        evaluated: false
    },
    [NTA_STATES.ANSWERED_AND_MARKED]: {
        label: "Answered & Marked for Review",
        cssClass: "nta-answered-marked",
        color: "#7c3aed",
        evaluated: true // NTA evaluates this for JEE rank scoring
    }
});

/**
 * Calculates new state when a question is first opened/viewed
 */
export function transitionOnView(currentState) {
    if (currentState === NTA_STATES.NOT_VISITED) {
        return NTA_STATES.NOT_ANSWERED;
    }
    return currentState;
}

/**
 * Calculates new state when student clicks "Save & Next"
 * @param {string|null} selectedOption 
 */
export function transitionOnSaveAndNext(selectedOption) {
    if (selectedOption !== null && selectedOption !== undefined && selectedOption !== "") {
        return NTA_STATES.ANSWERED;
    }
    return NTA_STATES.NOT_ANSWERED;
}

/**
 * Calculates new state when student clicks "Mark for Review & Next"
 * @param {string|null} selectedOption 
 */
export function transitionOnMarkForReview(selectedOption) {
    const hasAnswer = selectedOption !== null && selectedOption !== undefined && selectedOption !== "";
    return hasAnswer ? NTA_STATES.ANSWERED_AND_MARKED : NTA_STATES.MARKED_FOR_REVIEW;
}

/**
 * Calculates new state and reset when student clicks "Clear Response"
 */
export function transitionOnClearResponse() {
    return {
        newState: NTA_STATES.NOT_ANSWERED,
        clearedOption: null
    };
}

/**
 * Computes palette statistics across all questions
 * @param {Object} responsesMap - { [questionId]: { state: number, selectedOption: any } }
 * @param {number} totalQuestions
 */
export function computePaletteStats(responsesMap = {}, totalQuestions = 75) {
    const stats = {
        [NTA_STATES.NOT_VISITED]: 0,
        [NTA_STATES.NOT_ANSWERED]: 0,
        [NTA_STATES.ANSWERED]: 0,
        [NTA_STATES.MARKED_FOR_REVIEW]: 0,
        [NTA_STATES.ANSWERED_AND_MARKED]: 0
    };

    let accountedCount = 0;
    for (const qId in responsesMap) {
        const item = responsesMap[qId];
        if (item && item.state !== undefined && stats[item.state] !== undefined) {
            stats[item.state]++;
            accountedCount++;
        }
    }

    // Remaining untouched questions default to Not Visited
    stats[NTA_STATES.NOT_VISITED] = Math.max(0, totalQuestions - accountedCount);

    return stats;
}
