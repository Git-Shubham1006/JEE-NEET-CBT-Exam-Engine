# 🚀 JEE CBT & AI Mentorship Platform — Enterprise B2B Blueprint
**Co-Founders:** RannVijay & Antigravity (Google Senior Staff / Tech Co-Founder)  
**Target:** Build an offline-first, white-label CBT examination platform sold to coaching institutes with multi-tenant isolation, AI diagnostics, and fail-safe local persistence.

---

## 1. Business & Architectural Model: White-Label B2B SaaS
The platform is designed as a **reusable, white-label template** sold to coaching institutes (Patna, Kota, Delhi, etc.) on a monthly/annual subscription per active student.

### Key Capabilities:
1. **Dynamic Theming / White-Labeling:**
   - Custom subdomain (e.g., `apex.platform.com`, `resonance.platform.com`).
   - Dynamic institute logo, primary/accent brand colors, and anti-leak watermarking.
2. **Offline-First Student Terminal:**
   - Zero data loss during internet drops via client-side IndexedDB write-ahead persistence.
   - Background synchronization queue when network restores.
3. **AI JEE Mentor Diagnostic Engine:**
   - Time-wasted analytics (>4 mins spent with negative score).
   - Wild-guess / negative marking audit.
   - Targeted instant revision prescriptions.

---

## 2. Dual-Database Multi-Tenant Isolation Architecture

To ensure strict data privacy (Institute A must never see Institute B's question banks, student details, or test scores), the architecture uses a two-tier database separation:

### Tier 1: Platform Master Database (`jee_platform_master`)
*Accessible only by Super Admin (Shubham).*
* **`institutes`**: Registered institutes, subdomain slugs, branding theme configs, active/suspended status.
* **`subscriptions`**: Institute subscription tiers, student seat limits, renewal cycles, billing history.
* **`super_admins`**: Super-admin authentication and role management.
* **`global_telemetry`**: Platform-wide uptime, total active tests, global student concurrency.

### Tier 2: Tenant Institute Database (`institute_tenant_{slug}`)
*Accessible by Institute Directors, Teachers, and their enrolled Students.*
* **`students`**: Student ID, enrollment number, name, phone, assigned batches, account status.
* **`student_login_history`**: IP address, device fingerprints, login timestamps, concurrent session locks.
* **`batches`**: Cohort management (e.g., JEE 2026 Dropper Batch, Foundation 11th).
* **`tests`**: Scheduled exams, start/end windows, durations, marking schemes (+4/-1, partial marking).
* **`test_questions`**: Questions with KaTeX LaTeX math/chemical formulas, options, correct answers, hints.
* **`student_test_attempts`**: Started/submitted attempts, final scores, percentile, subject-wise splits.
* **`attempt_responses`**: Question-by-question responses, time spent per question, marked-for-review history.

---

## 3. Competitive Teardown: `myjeementor.theonlinetests.com`
* **Vulnerability 1: Fake Client-Side Validation:** Captcha and phone OTP tokens generated and checked in client-side JavaScript.
* **Vulnerability 2: RAM-Only Question State:** Entire test lives in volatile JavaScript memory without IndexedDB backing. Page refresh or network disconnect wipes progress.
* **Vulnerability 3: Outdated Monolith:** PHP/Laravel + jQuery 3.5.1 + Bootstrap 4 without PWA capabilities or offline sync queues.

---

## 4. Modern Technology Stack
* **Frontend Exam Shell:** Modular ES6 / React / Next.js with strict separation of storage, state machine, and rendering.
* **Math & Chemistry Rendering:** **KaTeX** (instant vector rendering, no blurry images).
* **Client-Side Persistence:** **IndexedDB + Service Worker (PWA)** (<2ms async writes).
* **Database & Backend:** Supabase / PostgreSQL (Schema-per-tenant or isolated DBs) + FastAPI / Node.js.
* **Security & Anti-Cheating:** Fullscreen enforcement, tab-switch blur detection, dynamic background watermarks, server-side HMAC response signing.

---

## 5. File System & Modularity Standards (Fault-Isolation)
To ensure no single file failure can corrupt or break the system:
* **`config/`**: Dynamic white-label theme schemas and DB connection resolvers.
* **`core/`**: Pure business logic (NTA 5-state machine, drift-free timestamp delta timer, scoring engine). Zero UI code.
* **`storage/`**: IndexedDB storage adapters and FIFO offline sync queues.
* **`rendering/`**: Isolated KaTeX equation parsers with error boundaries.
* **`components/`**: Decoupled UI modules (Header, Question Canvas, Question Palette).
* **`dashboards/`**:
  * `super-admin-view`: Master analytics across all institutes for Shubham.
  * `institute-admin-view`: Institute director portal for student management, test creation, and reports.

---

## 6. Competitive Benchmarks & Reference Systems

### Benchmark A: `myjeementor.theonlinetests.com` (CollegeDoors Engine)
* **The TIPS Mechanism:** Test Integration Platform System. Teachers generate tests algorithmically by selecting `Subject -> Chapter -> Topic -> Difficulty -> Freshness (Unused only)`.
* **Weaknesses to Exploit:** Legacy PHP/Laravel + jQuery stack, lack of offline IndexedDB persistence, low-res screenshot images for math equations.

### Benchmark B: `https://web.getmarks.app/` (MARKS App by MathonGo)
* **Target Audience:** B2C Student practice & diagnostic powerhouse.
* **Core Strengths:** Chapter-wise PYQ drilldown (JEE Main, Advanced, NEET, BITSAT), custom test generator, formula sheets, revision bookmarking, and preparation tracking.
* **Tech Stack:** Next.js + React + PWA manifest + MathJax/LaTeX (`mhchem.js`) for chemistry formulas.
* **Our Integration Moat:** We combine MARKS's clean chapter-wise PYQ drill-down & diagnostic UX with CollegeDoors's B2B white-label TIPS engine, powered by KaTeX and IndexedDB offline persistence.

