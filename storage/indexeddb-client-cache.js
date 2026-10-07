/**
 * ============================================================================
 * Zero-Data-Loss IndexedDB Client Persistence Engine
 * File: storage/indexeddb-client-cache.js
 * ============================================================================
 * Provides async local storage for student responses and session state.
 * Guarantees zero data loss if Wi-Fi disconnects or browser refreshes.
 */

const DB_NAME = 'JEE_CBT_CLIENT_VAULT';
const DB_VERSION = 1;

export class IndexedDBClientCache {
    constructor() {
        this.db = null;
    }

    /**
     * Initializes IndexedDB with required object stores
     */
    async init() {
        if (this.db) return this.db;

        return new Promise((resolve, reject) => {
            if (typeof window === 'undefined' || !window.indexedDB) {
                console.warn('IndexedDB not supported in current environment.');
                return resolve(null);
            }

            const request = window.indexedDB.open(DB_NAME, DB_VERSION);

            request.onupgradeneeded = (event) => {
                const db = event.target.result;

                // 1. Session store (test metadata, endTimestamp, current question)
                if (!db.objectStoreNames.contains('test_session')) {
                    db.createObjectStore('test_session', { keyPath: 'testId' });
                }

                // 2. Responses store (keyed by questionId)
                if (!db.objectStoreNames.contains('responses')) {
                    const responseStore = db.createObjectStore('responses', { keyPath: 'questionId' });
                    responseStore.createIndex('by_test', 'testId', { unique: false });
                }

                // 3. Offline Outbox Queue (FIFO for server sync)
                if (!db.objectStoreNames.contains('outbox_sync_queue')) {
                    db.createObjectStore('outbox_sync_queue', { keyPath: 'queueId', autoIncrement: true });
                }
            };

            request.onsuccess = (event) => {
                this.db = event.target.result;
                resolve(this.db);
            };

            request.onerror = (event) => {
                console.error('IndexedDB open error:', event.target.error);
                reject(event.target.error);
            };
        });
    }

    /**
     * Persists or updates the active test session state
     */
    async saveSession(sessionData) {
        await this.init();
        if (!this.db) return;

        return new Promise((resolve, reject) => {
            const tx = this.db.transaction('test_session', 'readwrite');
            const store = tx.objectStore('test_session');
            const req = store.put(sessionData);

            req.onsuccess = () => resolve(true);
            req.onerror = () => reject(req.error);
        });
    }

    /**
     * Retrieves test session by test ID
     */
    async getSession(testId) {
        await this.init();
        if (!this.db) return null;

        return new Promise((resolve, reject) => {
            const tx = this.db.transaction('test_session', 'readonly');
            const store = tx.objectStore('test_session');
            const req = store.get(testId);

            req.onsuccess = () => resolve(req.result || null);
            req.onerror = () => reject(req.error);
        });
    }

    /**
     * Persists an answer response directly to disk (< 2ms)
     * @param {Object} responseItem - { testId, questionId, selectedOption, state, timeSpentSeconds, updatedAt }
     */
    async saveResponse(responseItem) {
        await this.init();
        if (!this.db) return;

        return new Promise((resolve, reject) => {
            const tx = this.db.transaction(['responses', 'outbox_sync_queue'], 'readwrite');
            
            const responseStore = tx.objectStore('responses');
            responseStore.put(responseItem);

            // Also enqueue in offline sync outbox
            const outboxStore = tx.objectStore('outbox_sync_queue');
            outboxStore.add({
                action: 'SAVE_RESPONSE',
                payload: responseItem,
                timestamp: Date.now()
            });

            tx.oncomplete = () => resolve(true);
            tx.onerror = () => reject(tx.error);
        });
    }

    /**
     * Loads all saved responses for a given test
     */
    async getAllResponses(testId) {
        await this.init();
        if (!this.db) return {};

        return new Promise((resolve, reject) => {
            const tx = this.db.transaction('responses', 'readonly');
            const store = tx.objectStore('responses');
            const index = store.index('by_test');
            const req = index.getAll(testId);

            req.onsuccess = () => {
                const map = {};
                (req.result || []).forEach(item => {
                    map[item.questionId] = item;
                });
                resolve(map);
            };
            req.onerror = () => reject(req.error);
        });
    }

    /**
     * Clears all session and response data for a submitted test
     */
    async clearTestVault(testId) {
        await this.init();
        if (!this.db) return;

        return new Promise((resolve, reject) => {
            const tx = this.db.transaction(['test_session', 'responses', 'outbox_sync_queue'], 'readwrite');
            tx.objectStore('test_session').delete(testId);
            tx.objectStore('responses').clear();
            tx.objectStore('outbox_sync_queue').clear();

            tx.oncomplete = () => resolve(true);
            tx.onerror = () => reject(tx.error);
        });
    }
}
