/**
 * ============================================================================
 * Sample Coaching Institutes Registry (For White-Label Switcher Demo)
 * File: config/platform-tenants.sample.js
 * ============================================================================
 */

export const SampleTenants = [
    {
        instituteId: "inst_nta_default",
        instituteName: "Official NTA JEE CBT Simulation",
        subdomain: "jee-nta",
        branding: {
            primaryColor: "#0f4c81",
            accentColor: "#f39c12",
            headerBackground: "#0b3c65",
            watermarkText: "NTA MOCK - FOR PRACTICE ONLY",
            logoUrl: "NTA MOCK"
        },
        features: { enableWatermark: true, strictFullscreen: false }
    },
    {
        instituteId: "inst_apex_patna",
        instituteName: "Apex IIT-JEE Academy, Kankarbagh Patna",
        subdomain: "apex-patna",
        branding: {
            primaryColor: "#1e3a8a", // Royal Blue
            accentColor: "#dc2626", // Crimson Red
            headerBackground: "#172554",
            watermarkText: "APEX PATNA - CONFIDENTIAL TEST",
            logoUrl: "APEX PATNA"
        },
        features: { enableWatermark: true, strictFullscreen: true }
    },
    {
        instituteId: "inst_chanakya_kota",
        instituteName: "Chanakya Science Institute, Kota",
        subdomain: "chanakya-kota",
        branding: {
            primaryColor: "#065f46", // Emerald Forest
            accentColor: "#d97706", // Amber
            headerBackground: "#064e3b",
            watermarkText: "CHANAKYA KOTA RANK TEST",
            logoUrl: "CHANAKYA KOTA"
        },
        features: { enableWatermark: true, strictFullscreen: false }
    },
    {
        instituteId: "inst_super30_bihar",
        instituteName: "Ramanujan Super-30 Foundation, Bihar",
        subdomain: "super30",
        branding: {
            primaryColor: "#7c2d12", // Deep Terracotta
            accentColor: "#eab308", // Golden
            headerBackground: "#451a03",
            watermarkText: "SUPER-30 SCHOLARSHIP EXAM",
            logoUrl: "SUPER 30"
        },
        features: { enableWatermark: true, strictFullscreen: false }
    }
];
