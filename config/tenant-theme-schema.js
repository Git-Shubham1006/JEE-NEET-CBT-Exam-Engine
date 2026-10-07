/**
 * ============================================================================
 * White-Label Tenant Theme Schema & Dynamic Theme Applicator
 * File: config/tenant-theme-schema.js
 * ============================================================================
 */

export const DefaultThemeConfig = {
    instituteId: "default",
    instituteName: "National Testing Agency Mock Portal",
    subdomain: "portal",
    branding: {
        primaryColor: "#0f4c81",      // Official deep blue
        accentColor: "#f39c12",       // Vibrant amber
        headerBackground: "#0b3c65",
        watermarkText: "CBT MOCK TEST - CONFIDENTIAL",
        logoUrl: "https://via.placeholder.com/160x40/0f4c81/ffffff?text=JEE+PORTAL"
    },
    features: {
        enableWatermark: true,
        strictFullscreen: false,
        showSectionTotals: true
    }
};

/**
 * Validates and merges tenant config with fallback defaults
 * @param {Object} rawConfig 
 * @returns {Object} Clean validated theme config
 */
export function validateAndMergeTheme(rawConfig = {}) {
    return {
        instituteId: rawConfig.instituteId || DefaultThemeConfig.instituteId,
        instituteName: rawConfig.instituteName || DefaultThemeConfig.instituteName,
        subdomain: rawConfig.subdomain || DefaultThemeConfig.subdomain,
        branding: {
            primaryColor: rawConfig.branding?.primaryColor || DefaultThemeConfig.branding.primaryColor,
            accentColor: rawConfig.branding?.accentColor || DefaultThemeConfig.branding.accentColor,
            headerBackground: rawConfig.branding?.headerBackground || DefaultThemeConfig.branding.headerBackground,
            watermarkText: rawConfig.branding?.watermarkText || DefaultThemeConfig.branding.watermarkText,
            logoUrl: rawConfig.branding?.logoUrl || DefaultThemeConfig.branding.logoUrl
        },
        features: {
            enableWatermark: rawConfig.features?.enableWatermark ?? DefaultThemeConfig.features.enableWatermark,
            strictFullscreen: rawConfig.features?.strictFullscreen ?? DefaultThemeConfig.features.strictFullscreen,
            showSectionTotals: rawConfig.features?.showSectionTotals ?? DefaultThemeConfig.features.showSectionTotals
        }
    };
}

/**
 * Injects CSS variables dynamically into document root for white-label styling
 * @param {Object} themeConfig 
 */
export function applyThemeToDOM(themeConfig) {
    if (typeof document === 'undefined') return;
    const root = document.documentElement;
    root.style.setProperty('--tenant-primary', themeConfig.branding.primaryColor);
    root.style.setProperty('--tenant-accent', themeConfig.branding.accentColor);
    root.style.setProperty('--tenant-header-bg', themeConfig.branding.headerBackground);
}
