-- ============================================================================
-- DATABASE 2: TENANT INSTITUTE DATABASE (Coaching Institute Admin Level)
-- Name: institute_tenant_{slug} (e.g. institute_tenant_apex_patna)
-- Target: PostgreSQL / Supabase
-- Purpose: Complete isolation of institute's students, login history, tests, marks, and responses.
-- ============================================================================

-- 1. Batches / Cohorts (e.g., "JEE 2026 Dropper Batch", "Class 12th Super 30")
CREATE TABLE IF NOT EXISTS tenant_batches (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    batch_code VARCHAR(32) UNIQUE NOT NULL,
    batch_name VARCHAR(128) NOT NULL,
    target_exam VARCHAR(64) NOT NULL DEFAULT 'JEE_MAIN_ADVANCED',
    target_year INTEGER NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- 2. Enrolled Students
CREATE TABLE IF NOT EXISTS tenant_students (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    enrollment_number VARCHAR(64) UNIQUE NOT NULL,   -- e.g. "APEX-2026-0412"
    full_name VARCHAR(128) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    email VARCHAR(255),
    password_hash VARCHAR(255) NOT NULL,
    batch_id UUID REFERENCES tenant_batches(id) ON DELETE SET NULL,
    avatar_url VARCHAR(512),
    is_blocked BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- 3. Student Login History (Device fingerprints, IP audits, multi-login detection)
CREATE TABLE IF NOT EXISTS tenant_student_login_history (
    id BIGSERIAL PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES tenant_students(id) ON DELETE CASCADE,
    ip_address VARCHAR(45) NOT NULL,
    user_agent TEXT,
    device_fingerprint VARCHAR(128),
    login_time TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    logout_time TIMESTAMPTZ,
    session_status VARCHAR(32) NOT NULL DEFAULT 'ACTIVE' -- ACTIVE, EXPIRED, TERMINATED_BY_ADMIN
);

-- 4. Tests Scheduled by the Institute
CREATE TABLE IF NOT EXISTS tenant_tests (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    test_code VARCHAR(64) UNIQUE NOT NULL,
    title VARCHAR(255) NOT NULL,
    pattern VARCHAR(32) NOT NULL DEFAULT 'JEE_MAIN', -- JEE_MAIN, JEE_ADVANCED, BITSAT
    duration_minutes INTEGER NOT NULL DEFAULT 180,
    total_marks INTEGER NOT NULL DEFAULT 300,
    start_window TIMESTAMPTZ NOT NULL,
    end_window TIMESTAMPTZ NOT NULL,
    is_published BOOLEAN NOT NULL DEFAULT FALSE,
    marking_scheme JSONB NOT NULL DEFAULT '{
        "single_correct": {"correct": 4, "incorrect": -1, "unattempted": 0},
        "numerical": {"correct": 4, "incorrect": 0, "unattempted": 0}
    }'::jsonb,
    created_by VARCHAR(128) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- 5. Test Questions with KaTeX LaTeX Support
CREATE TABLE IF NOT EXISTS tenant_test_questions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    test_id UUID NOT NULL REFERENCES tenant_tests(id) ON DELETE CASCADE,
    question_order INTEGER NOT NULL,
    subject VARCHAR(32) NOT NULL,                    -- PHYSICS, CHEMISTRY, MATHEMATICS
    section_type VARCHAR(32) NOT NULL DEFAULT 'SCQ', -- SCQ (Single Correct), NUMERICAL
    question_latex TEXT NOT NULL,
    options_json JSONB,                             -- Array of options with LaTeX text: [{"id": "A", "latex": "..."}, ...]
    correct_answer VARCHAR(64) NOT NULL,            -- e.g. "A" or "42" for numerical
    solution_latex TEXT,
    difficulty VARCHAR(16) DEFAULT 'MEDIUM'          -- EASY, MEDIUM, HARD
);

-- 6. Student Test Attempts
CREATE TABLE IF NOT EXISTS tenant_student_attempts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id UUID NOT NULL REFERENCES tenant_students(id) ON DELETE CASCADE,
    test_id UUID NOT NULL REFERENCES tenant_tests(id) ON DELETE CASCADE,
    start_time TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    submit_time TIMESTAMPTZ,
    time_taken_seconds INTEGER DEFAULT 0,
    total_score NUMERIC(6, 2) DEFAULT 0,
    physics_score NUMERIC(6, 2) DEFAULT 0,
    chemistry_score NUMERIC(6, 2) DEFAULT 0,
    math_score NUMERIC(6, 2) DEFAULT 0,
    status VARCHAR(32) NOT NULL DEFAULT 'IN_PROGRESS', -- IN_PROGRESS, SUBMITTED, AUTO_SUBMITTED, CANCELLED
    client_sync_status VARCHAR(32) NOT NULL DEFAULT 'PENDING' -- PENDING, SYNCED
);

-- 7. Granular Attempt Responses (Recorded during test & sync)
CREATE TABLE IF NOT EXISTS tenant_attempt_responses (
    id BIGSERIAL PRIMARY KEY,
    attempt_id UUID NOT NULL REFERENCES tenant_student_attempts(id) ON DELETE CASCADE,
    question_id UUID NOT NULL REFERENCES tenant_test_questions(id) ON DELETE CASCADE,
    selected_option VARCHAR(64),                     -- "A", "B", "C", "D" or numeric string "25"
    response_state INTEGER NOT NULL DEFAULT 0,       -- 0: Not Visited, 1: Not Answered, 2: Answered, 3: Review, 4: Marked & Answered
    time_spent_seconds INTEGER NOT NULL DEFAULT 0,
    is_correct BOOLEAN,
    marks_awarded NUMERIC(5, 2) DEFAULT 0,
    recorded_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT unique_attempt_question UNIQUE (attempt_id, question_id)
);

-- Indices for rapid query performance
CREATE INDEX IF NOT EXISTS idx_tenant_students_batch ON tenant_students(batch_id);
CREATE INDEX IF NOT EXISTS idx_tenant_login_student ON tenant_student_login_history(student_id, login_time DESC);
CREATE INDEX IF NOT EXISTS idx_tenant_attempts_student ON tenant_student_attempts(student_id, test_id);
CREATE INDEX IF NOT EXISTS idx_tenant_responses_attempt ON tenant_attempt_responses(attempt_id);
