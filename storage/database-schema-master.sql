-- ============================================================================
-- DATABASE 1: MASTER PLATFORM DATABASE (Shubham's God-Mode / Super-Admin)
-- Name: jee_platform_master
-- Target: PostgreSQL / Supabase
-- Purpose: Global platform telemetry, institute licensing, billing, and routing.
-- ============================================================================

-- 1. Institutes Registry (All client coaching institutes)
CREATE TABLE IF NOT EXISTS master_institutes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    institute_code VARCHAR(32) UNIQUE NOT NULL,      -- e.g. "APEX_PATNA", "CHANAKYA_KOTA"
    institute_name VARCHAR(255) NOT NULL,
    subdomain_slug VARCHAR(64) UNIQUE NOT NULL,     -- e.g. "apex", "chanakya"
    custom_domain VARCHAR(255) UNIQUE,              -- e.g. "cbt.apexacademy.in"
    contact_person VARCHAR(128) NOT NULL,
    contact_email VARCHAR(255) NOT NULL,
    contact_phone VARCHAR(32) NOT NULL,
    
    -- Branding configuration (White-label JSON)
    theme_config JSONB NOT NULL DEFAULT '{
        "primary_color": "#1e40af",
        "accent_color": "#f59e0b",
        "logo_url": "/assets/default-logo.png",
        "watermark_text": "MOCK TEST CONFIDENTIAL"
    }'::jsonb,
    
    -- Database connection routing for this institute's isolated tenant DB
    tenant_db_connection JSONB NOT NULL DEFAULT '{
        "host": "localhost",
        "port": 5432,
        "db_name": "tenant_default",
        "schema_name": "public"
    }'::jsonb,

    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- 2. Institute Subscriptions & Student Seat Licenses
CREATE TABLE IF NOT EXISTS master_institute_subscriptions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    institute_id UUID NOT NULL REFERENCES master_institutes(id) ON DELETE CASCADE,
    plan_tier VARCHAR(64) NOT NULL DEFAULT 'PRO_TIER', -- STARTER, PRO, ENTERPRISE
    max_active_students INTEGER NOT NULL DEFAULT 500,
    mrr_inr NUMERIC(10, 2) NOT NULL DEFAULT 15000.00,
    billing_cycle VARCHAR(32) NOT NULL DEFAULT 'MONTHLY', -- MONTHLY, ANNUAL
    start_date DATE NOT NULL,
    expiry_date DATE NOT NULL,
    auto_renew BOOLEAN NOT NULL DEFAULT TRUE,
    payment_status VARCHAR(32) NOT NULL DEFAULT 'PAID'  -- PAID, PENDING, OVERDUE, CANCELLED
);

-- 3. Super Admin Credentials (Only Shubham & Co-Founder have access)
CREATE TABLE IF NOT EXISTS master_super_admins (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    full_name VARCHAR(128) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(32) NOT NULL DEFAULT 'SUPER_ADMIN',   -- SUPER_ADMIN, PLATFORM_OPS
    last_login_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- 4. Global Platform Telemetry & Live Concurrency Monitoring
CREATE TABLE IF NOT EXISTS master_global_telemetry (
    id BIGSERIAL PRIMARY KEY,
    institute_id UUID REFERENCES master_institutes(id) ON DELETE SET NULL,
    active_test_count INTEGER NOT NULL DEFAULT 0,
    concurrent_students_online INTEGER NOT NULL DEFAULT 0,
    offline_sync_failures INTEGER NOT NULL DEFAULT 0,
    recorded_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Indices for rapid routing and telemetry lookups
CREATE INDEX IF NOT EXISTS idx_institutes_subdomain ON master_institutes(subdomain_slug);
CREATE INDEX IF NOT EXISTS idx_institutes_status ON master_institutes(is_active);
CREATE INDEX IF NOT EXISTS idx_subscriptions_expiry ON master_institute_subscriptions(expiry_date);
CREATE INDEX IF NOT EXISTS idx_telemetry_timestamp ON master_global_telemetry(recorded_at DESC);
