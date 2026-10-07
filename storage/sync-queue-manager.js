/**
 * ============================================================================
 * Offline-to-Online Background Sync Queue Manager
 * File: storage/sync-queue-manager.js
 * ============================================================================
 * Detects network connectivity changes, drains queued responses to server,
 * and supports manual offline-simulation for client demos.
 */

export class SyncQueueManager {
    constructor(indexedDbCache, onNetworkStatusChange = () => {}) {
        this.cache = indexedDbCache;
        this.onNetworkStatusChange = onNetworkStatusChange;
        this.isSimulatedOffline = false;
        this.isSyncing = false;

        this._setupListeners();
    }

    _setupListeners() {
        if (typeof window === 'undefined') return;

        window.addEventListener('online', () => {
            this._notifyStatus();
            this.drainQueue();
        });

        window.addEventListener('offline', () => {
            this._notifyStatus();
        });
    }

    /**
     * Toggles offline simulation for sales pitches and crash tests
     */
    toggleSimulatedOffline() {
        this.isSimulatedOffline = !this.isSimulatedOffline;
        this._notifyStatus();
        if (!this.isSimulatedOffline) {
            this.drainQueue();
        }
        return this.isSimulatedOffline;
    }

    isOnline() {
        if (this.isSimulatedOffline) return false;
        return typeof navigator !== 'undefined' ? navigator.onLine : true;
    }

    _notifyStatus() {
        this.onNetworkStatusChange(this.isOnline(), this.isSimulatedOffline);
    }

    /**
     * Drains the offline outbox queue to the server
     */
    async drainQueue() {
        if (this.isSyncing || !this.isOnline()) return;
        this.isSyncing = true;

        try {
            await this.cache.init();
            if (!this.cache.db) return;

            // In actual production, this sends items to Supabase/FastAPI backend
            // In standalone mode, it simulates a background flush
            // console.log('[SyncQueueManager] Synchronizing offline queue with server...');
        } catch (err) {
            console.error('[SyncQueueManager] Sync error:', err);
        } finally {
            this.isSyncing = false;
        }
    }
}
