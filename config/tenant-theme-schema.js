/**
 * ============================================================================
 * White-Label Tenant Theme Schema & Adaptive Design System
 * File: config/tenant-theme-schema.js
 * ============================================================================
 * Enables coaching institutes to dynamically renew and adapt their:
 * - Brand Colors (Primary, Dark Primary, Accent, Header BG)
 * - Border Styling & Corner Radii (Sharp, Standard, Smooth, Pill)
 * - Navigation Tabs, Badges, and Button Themes
 */

export const THEME_PRESETS = Object.freeze({
    sapphire: {
        id: "sapphire",
        name: "Apex Sapphire (Patna Elite)",
        primary: "#1e3a8a",
        primaryDark: "#0f172a",
        accent: "#2563eb",
        border: "#cbd5e1",
        headerBg: "#0f172a",
        logoBg: "#2563eb",
        btnRadius: "8px",
        tag: "Classic Navy Blue"
    },
    crimson: {
        id: "crimson",
        name: "Chanakya Crimson (Kota Fire)",
        primary: "#881337",
        primaryDark: "#4c0519",
        accent: "#e11d48",
        border: "#fecdd3",
        headerBg: "#4c0519",
        logoBg: "#e11d48",
        btnRadius: "6px",
        tag: "Royal Maroon & Ruby"
    },
    emerald: {
        id: "emerald",
        name: "Emerald Academy (Allen-Style)",
        primary: "#065f46",
        primaryDark: "#022c22",
        accent: "#10b981",
        border: "#a7f3d0",
        headerBg: "#022c22",
        logoBg: "#10b981",
        btnRadius: "8px",
        tag: "Forest Green & Mint"
    },
    royal_purple: {
        id: "royal_purple",
        name: "Imperial Violet (Resonance-Style)",
        primary: "#581c87",
        primaryDark: "#3b0764",
        accent: "#9333ea",
        border: "#e9d5ff",
        headerBg: "#3b0764",
        logoBg: "#9333ea",
        btnRadius: "10px",
        tag: "Deep Purple & Amethyst"
    },
    amber_gold: {
        id: "amber_gold",
        name: "Suryavanshi Amber (Narayana-Style)",
        primary: "#b45309",
        primaryDark: "#78350f",
        accent: "#f59e0b",
        border: "#fde68a",
        headerBg: "#78350f",
        logoBg: "#f59e0b",
        btnRadius: "6px",
        tag: "Deep Amber & Golden Sand"
    },
    cyber_slate: {
        id: "cyber_slate",
        name: "Cyber Slate (Modern Minimalist)",
        primary: "#0f172a",
        primaryDark: "#020617",
        accent: "#06b6d4",
        border: "#334155",
        headerBg: "#020617",
        logoBg: "#06b6d4",
        btnRadius: "12px",
        tag: "Dark Matrix & Neon Cyan"
    }
});

const STORAGE_PREFIX = "JEE_CBT_TENANT_THEME_";

/**
 * Loads stored theme or returns default
 */
export function getTenantTheme(tenantId = "apex") {
    if (typeof window === "undefined") return THEME_PRESETS.sapphire;
    try {
        const key = STORAGE_PREFIX + tenantId.toLowerCase();
        const stored = localStorage.getItem(key);
        if (stored) {
            return JSON.parse(stored);
        }
    } catch (e) {
        console.warn("Theme storage read error:", e);
    }
    return tenantId.toLowerCase().includes("chanakya") ? THEME_PRESETS.crimson : THEME_PRESETS.sapphire;
}

/**
 * Saves and persists tenant theme
 */
export function saveTenantTheme(tenantId, themeConfig) {
    if (typeof window === "undefined") return;
    try {
        const key = STORAGE_PREFIX + tenantId.toLowerCase();
        localStorage.setItem(key, JSON.stringify(themeConfig));
    } catch (e) {
        console.warn("Theme storage save error:", e);
    }
}

/**
 * Dynamically applies theme tokens to the DOM
 */
export function applyThemeToDOM(theme) {
    if (typeof document === "undefined" || !theme) return;
    const root = document.documentElement;

    root.style.setProperty("--primary", theme.primary);
    root.style.setProperty("--primary-dark", theme.primaryDark);
    root.style.setProperty("--accent", theme.accent);
    root.style.setProperty("--border", theme.border);
    root.style.setProperty("--btn-radius", theme.btnRadius || "8px");

    // Header and Logo styling
    const header = document.querySelector(".inst-header");
    if (header) {
        header.style.backgroundColor = theme.headerBg;
        header.style.borderBottomColor = theme.accent;
    }

    const logo = document.getElementById("instLogo");
    if (logo) {
        logo.style.backgroundColor = theme.logoBg;
        logo.style.borderRadius = theme.btnRadius || "8px";
    }

    // Dynamic button radius
    document.querySelectorAll(".btn-action, .btn-confirm").forEach(btn => {
        btn.style.borderRadius = theme.btnRadius || "8px";
    });
}
