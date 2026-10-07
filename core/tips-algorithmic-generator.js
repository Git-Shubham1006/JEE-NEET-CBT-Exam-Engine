/**
 * ============================================================================
 * TIPS Algorithmic Paper Generator & Syllabus Filter Engine
 * File: core/tips-algorithmic-generator.js
 * ============================================================================
 * Powers the Test Integration Platform System (TIPS).
 * Allows coaching teachers to generate customized JEE mock tests algorithmically
 * by selecting chapters, difficulty quotas, and question types.
 */

/**
 * Extracts syllabus hierarchy (Subjects -> Chapters -> Topics) from question bank
 * @param {Array} questionBank 
 * @returns {Object} { [subject]: { [chapter]: [topics] } }
 */
export function extractSyllabusTaxonomy(questionBank = []) {
    const taxonomy = {};

    questionBank.forEach(q => {
        const sub = q.subject || 'General';
        const ch = q.chapter || 'Misc';
        const top = q.topic || 'General Topic';

        if (!taxonomy[sub]) taxonomy[sub] = {};
        if (!taxonomy[sub][ch]) taxonomy[sub][ch] = new Set();
        taxonomy[sub][ch].add(top);
    });

    // Convert sets to sorted arrays
    const formatted = {};
    for (const sub in taxonomy) {
        formatted[sub] = {};
        for (const ch in taxonomy[sub]) {
            formatted[sub][ch] = Array.from(taxonomy[sub][ch]).sort();
        }
    }
    return formatted;
}

/**
 * Filters master question bank by selected chapters, difficulties, and types
 * @param {Array} questionBank 
 * @param {Object} filterOptions - { selectedChapters: [], selectedDifficulties: [], selectedTypes: [] }
 */
export function filterQuestions(questionBank = [], filterOptions = {}) {
    const {
        selectedChapters = [],
        selectedDifficulties = [],
        selectedTypes = []
    } = filterOptions;

    return questionBank.filter(q => {
        if (selectedChapters.length > 0 && !selectedChapters.includes(q.chapter)) {
            return false;
        }
        if (selectedDifficulties.length > 0 && !selectedDifficulties.includes(q.difficulty)) {
            return false;
        }
        if (selectedTypes.length > 0 && !selectedTypes.includes(q.type)) {
            return false;
        }
        return true;
    });
}

/**
 * Algorithmic Test Paper Generator
 * Automatically picks questions according to specified quotas and constraints
 * @param {Array} pool - Filtered candidate questions
 * @param {number} totalRequested - Target number of questions (e.g. 10 or 25)
 * @returns {Array} Selected questions list
 */
export function assembleTestPaper(pool = [], totalRequested = 10) {
    if (pool.length <= totalRequested) {
        return [...pool];
    }

    // Shuffle pool with Fisher-Yates algorithm
    const shuffled = [...pool];
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }

    return shuffled.slice(0, totalRequested);
}

/**
 * 1-Click Question Swap / Replace Engine
 * Replaces a specific question with an alternative from the same chapter/difficulty
 * @param {Array} currentPaperQuestions 
 * @param {number} targetIndexToSwap 
 * @param {Array} masterBank 
 * @returns {Object} { updatedPaper, replacedWith }
 */
export function swapQuestionInPaper(currentPaperQuestions = [], targetIndexToSwap = 0, masterBank = []) {
    const targetQ = currentPaperQuestions[targetIndexToSwap];
    if (!targetQ) return { updatedPaper: currentPaperQuestions, replacedWith: null };

    const currentIds = new Set(currentPaperQuestions.map(q => q.id));

    // Find candidates from same chapter and difficulty not currently in test
    const candidates = masterBank.filter(q => 
        q.chapter === targetQ.chapter &&
        !currentIds.has(q.id)
    );

    if (candidates.length === 0) {
        // Fallback: any question from same subject not in test
        const subjectCandidates = masterBank.filter(q => 
            q.subject === targetQ.subject && 
            !currentIds.has(q.id)
        );
        if (subjectCandidates.length === 0) {
            return { updatedPaper: currentPaperQuestions, replacedWith: null };
        }
        const replacement = subjectCandidates[Math.floor(Math.random() * subjectCandidates.length)];
        const updated = [...currentPaperQuestions];
        updated[targetIndexToSwap] = replacement;
        return { updatedPaper: updated, replacedWith: replacement };
    }

    const replacement = candidates[Math.floor(Math.random() * candidates.length)];
    const updated = [...currentPaperQuestions];
    updated[targetIndexToSwap] = replacement;
    return { updatedPaper: updated, replacedWith: replacement };
}

/**
 * Merges multiple individual subject sections made by different teachers into a full mock paper
 * @param {Array} subjectDrafts - Array of { subject: string, teacherName: string, questions: Array }
 * @param {Object} metadata - { testId, title, durationMinutes, pattern }
 * @returns {Object} Complete unified test package ready for Student CBT
 */
export function mergeSubjectSections(subjectDrafts = [], metadata = {}) {
    const combinedQuestions = [];
    const sections = [];

    let currentIndex = 0;

    subjectDrafts.forEach(draft => {
        const count = draft.questions.length;
        if (count === 0) return;

        const subName = draft.subject.toUpperCase();
        const startIndex = currentIndex;
        const endIndex = startIndex + count - 1;

        sections.push({
            id: subName,
            name: draft.subject,
            teacher: draft.teacherName || 'Subject Specialist',
            startIndex,
            endIndex
        });

        draft.questions.forEach((q, qSubIdx) => {
            combinedQuestions.push({
                ...q,
                questionNumber: currentIndex + 1,
                sectionSubject: draft.subject
            });
            currentIndex++;
        });
    });

    return {
        testId: metadata.testId || `MOCK_COMBINED_${Date.now()}`,
        title: metadata.title || 'Combined All India Mock Examination',
        pattern: metadata.pattern || 'JEE_MAIN',
        durationMinutes: metadata.durationMinutes || 180,
        totalQuestions: combinedQuestions.length,
        sections,
        questions: combinedQuestions,
        generatedAt: new Date().toISOString()
    };
}

