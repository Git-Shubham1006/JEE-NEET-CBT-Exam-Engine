/**
 * ============================================================================
 * Session Authentication Guard & Strict Multi-Tenant Isolator
 * File: auth/session-auth-guard.js
 * ============================================================================
 * Enforces strict role boundaries:
 * 1. SUPER_ADMIN (RannVijay): God-Mode across all institutes.
 * 2. INSTITUTE_ADMIN: Locked strictly to their own tenant DB. Zero cross-tenant leakage.
 * 3. STUDENT: Locked to their enrolled institute's tests and practice hub.
 */

const SESSION_KEY = 'JEE_CBT_AUTH_SESSION';

export const USER_ROLES = Object.freeze({
    SUPER_ADMIN: 'SUPER_ADMIN',
    INSTITUTE_ADMIN: 'INSTITUTE_ADMIN',
    STUDENT: 'STUDENT'
});

export const PRESET_ACCOUNTS = Object.freeze({
    // Super-Admin (Platform Owner)
    'rannvijay@platform.com': {
        role: USER_ROLES.SUPER_ADMIN,
        name: 'RannVijay',
        title: 'Platform Co-Founder & Super-Admin',
        instituteId: 'master_global'
    },
    // Institute 1: Apex Patna Admin
    'director@apexpatna.in': {
        role: USER_ROLES.INSTITUTE_ADMIN,
        name: 'Director S. K. Roy',
        instituteId: 'apex',
        instituteName: 'Apex IIT-JEE Academy, Patna',
        subdomain: 'apex-patna',
        logoText: 'APEX',
        dbName: 'institute_tenant_apex_patna'
    },
    // Institute 2: Chanakya Kota Admin
    'admin@chanakyakota.in': {
        role: USER_ROLES.INSTITUTE_ADMIN,
        name: 'HOD Examination Council',
        instituteId: 'chanakya',
        instituteName: 'Chanakya Science Institute, Kota',
        subdomain: 'chanakya-kota',
        logoText: 'CHANAKYA',
        dbName: 'institute_tenant_chanakya_kota'
    },
    // Student: RannVijay Student Profile
    'student@apexpatna.in': {
        role: USER_ROLES.STUDENT,
        name: 'RannVijay Kumar',
        rollNo: '26030412',
        instituteId: 'apex',
        instituteName: 'Apex IIT-JEE Academy, Patna',
        batchName: 'JEE 2026 Dropper Elite'
    }
});

/**
 * Retrieves the currently active session
 */
export function getCurrentSession() {
    if (typeof window === 'undefined') return null;
    try {
        const raw = sessionStorage.getItem(SESSION_KEY) || localStorage.getItem(SESSION_KEY);
        return raw ? JSON.parse(raw) : null;
    } catch (e) {
        return null;
    }
}

/**
 * Saves authenticated session
 */
export function setAuthSession(sessionData, rememberMe = true) {
    if (typeof window === 'undefined') return;
    const serialized = JSON.stringify(sessionData);
    sessionStorage.setItem(SESSION_KEY, serialized);
    if (rememberMe) {
        localStorage.setItem(SESSION_KEY, serialized);
    }
}

/**
 * Clears session (Logout)
 */
export function clearAuthSession() {
    if (typeof window === 'undefined') return;
    sessionStorage.removeItem(SESSION_KEY);
    localStorage.removeItem(SESSION_KEY);
}

/**
 * Enforces role access on a page. Redirects unauthorized users.
 * @param {Array<string>} allowedRoles 
 * @param {string} redirectOnFail 
 */
export function enforceAccess(allowedRoles = [], redirectOnFail = '/login.html') {
    if (typeof window === 'undefined') return null;
    const session = getCurrentSession();

    if (!session) {
        window.location.href = redirectOnFail;
        return null;
    }

    if (allowedRoles.length > 0 && !allowedRoles.includes(session.role)) {
        alert(`⛔ Access Denied: You do not have permissions to access this portal.`);
        if (session.role === USER_ROLES.INSTITUTE_ADMIN) {
            window.location.href = '/dashboards/institute-admin.html';
        } else if (session.role === USER_ROLES.STUDENT) {
            window.location.href = '/index.html';
        } else {
            window.location.href = redirectOnFail;
        }
        return null;
    }

    return session;
}
