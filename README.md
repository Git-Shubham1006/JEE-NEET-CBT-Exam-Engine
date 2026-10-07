# 🚀 JEE/NEET CBT Exam & AI Mentorship Platform (Enterprise White-Label Edition)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Founder: RannVijay](https://img.shields.io/badge/Founder-RannVijay-blue.svg)]()
[![Co-Founder & CTO: Barry](https://img.shields.io/badge/CTO-Barry-indigo.svg)]()
[![Architecture: Multi--Tenant](https://img.shields.io/badge/Architecture-Multi--Tenant_Isolated-success.svg)]()
[![Math: KaTeX Vector](https://img.shields.io/badge/Math-KaTeX_Vector-60fps-orange.svg)]()
[![Storage: IndexedDB Offline](https://img.shields.io/badge/Storage-IndexedDB_Offline_Shield-green.svg)]()

> **Co-Founders:** **RannVijay** (Founder & CEO) & **Barry** (Co-Founder & CTO)  
> **Mission:** Replace slow, blurry legacy test systems (Classplus, TheOnlineTests) with an offline-first, white-label, multi-tenant JEE/NEET CBT exam and AI mentorship engine sold directly to coaching institutes.

---

## 🌐 Live Cloudflare Public Links (SSL / Encrypted)

* **🏢 Isolated Institute Portal (Apex Patna White-Label):** [`/login.html?org=apex`](https://watch-scene-productions-introductory.trycloudflare.com/login.html?org=apex)
* **🔐 Unified Portal Entry (Role-Based Login):** [`/login.html`](https://watch-scene-productions-introductory.trycloudflare.com/login.html)
* **🎓 Student CBT Exam Terminal (1:1 NTA Exact Clone):** [`/index.html`](https://watch-scene-productions-introductory.trycloudflare.com/index.html)
* **📚 Student Self-Study & PYQ Practice Hub (MARKS-Style):** [`/dashboards/student-practice-hub.html`](https://watch-scene-productions-introductory.trycloudflare.com/dashboards/student-practice-hub.html)
* **⚡ TIPS Test Paper Builder & 1-Click Merger:** [`/dashboards/tips-paper-builder.html`](https://watch-scene-productions-introductory.trycloudflare.com/dashboards/tips-paper-builder.html)
* **👑 RannVijay Master Console (God Mode):** [`/dashboards/super-admin.html`](https://watch-scene-productions-introductory.trycloudflare.com/dashboards/super-admin.html)

---

## 🏛️ Core Architectural Pillars

### 1. 🎓 Student CBT Terminal (`index.html`)
- **Offline-First Resilience:** Instant write-ahead persistence into client IndexedDB (`<2ms`). If Wi-Fi cuts out mid-test, the student never loses a second or an answer.
- **Official NTA Rules:** Official 5-state response machine (Not Visited, Not Answered, Answered, Marked for Review, Answered & Marked).
- **Vector KaTeX Math:** Crisp, scalable vector formulas across Physics, Chemistry, and Math at 60 fps (zero blurry image crops).
- **Drift-Free Clock:** Epoch timestamp delta timer immune to background tab throttling.
- **Wi-Fi Drop Simulator:** Click `🔌 Simulate Wi-Fi Drop` to test zero data loss on page refresh.

### 2. 📚 Student Practice Hub (`dashboards/student-practice-hub.html`)
*Inspired by `web.getmarks.app` (MARKS App by MathonGo)*
- **Self-Paced Chapter PYQ Drilling:** Physics, Chemistry, Mathematics, and Biology.
- **Instant Solution Feedback:** Immediate green/red validation upon option selection with full step-by-step mathematical derivations.
- **Instant Chapter Formula Sheets:** Quick formulas (e.g. $PV^\gamma = \text{const}$, $H_{max} = \frac{u^2 \sin^2\theta}{2g}$).
- **Mistake Notebook & Bookmarking:** Bookmark tricky questions for quick revision.

### 3. ⚡ TIPS Test Paper Builder (`dashboards/tips-paper-builder.html`)
- **Mode 1 (Subject Specialist):** Physics, Chemistry, Maths, and Biology teachers independently compile and stage subject drafts.
- **Mode 2 (Multi-Subject Mock):** Full PCM / PCB papers generated in one click.
- **Mode 3 (Subject Merger Hub):** Coordinators select and merge individual teacher drafts into unified 3-hour grand mock exams.
- **Dynamic KaTeX Preview & 1-Click "🔄 Swap Question"** replacement.

### 4. 🏢 Institute-Admin Portal (`dashboards/institute-admin.html`)
*Connects to Database 2 (`institute_tenant_{slug}`)*
- **Interactive Student ID Management:** Add new student accounts, delete accounts, and live search.
- **Teacher Academic Remarks:** Attach diagnostic pedagogical guidance directly to each student's profile.
- **Device & Login Audit:** Tracks IP addresses, browser user agents, and flags multi-device hotspot sharing.
- **Marks & AI Diagnostics:** Detailed scorecards, subject breakdowns, and penalty warnings.
- **Strict Tenant Isolation:** Apex Patna never sees Chanakya Kota or any competitor.

### 5. 👑 Super-Admin Master Portal (`dashboards/super-admin.html`)
*Connects to Database 1 (`jee_platform_master`)*
- **Partner Institutes Registry:** Telemetry across all onboarded institutes.
- **Financial & License Metrics:** Track Monthly Recurring Revenue (MRR in ₹) and student seat capacity.
- **1-Click Tenant Provisioning:** Instantly onboard a new coaching institute, assign brand colors, and configure an isolated tenant DB.

---

## 📁 Repository Layout
```
├── auth/
│   └── session-auth-guard.js          # Role-based access control & tenant boundary lock
├── config/
│   ├── platform-tenants.sample.js     # Multi-tenant coaching institute profiles
│   └── tenant-theme-schema.js         # Dynamic CSS variable injector & theme validator
├── core/
│   ├── exam-timer-engine.js           # Drift-free epoch delta countdown clock
│   ├── question-state-machine.js      # Official NTA 5-state transitions
│   ├── scoring-engine.js              # JEE +4/-1 scoring & AI diagnostic flags
│   └── tips-algorithmic-generator.js  # TIPS syllabus filter & question swap/merge engine
├── dashboards/
│   ├── institute-admin.html           # Institute Director & Teacher portal
│   ├── student-practice-hub.html      # Student Self-Study Hub (MARKS-style PYQ practice)
│   ├── super-admin.html               # RannVijay's God-Mode Master portal
│   └── tips-paper-builder.html        # TIPS Test Paper Compiler with 3 modes
├── mock-data/
│   ├── master-question-bank.json      # Categorized multi-chapter question database (PCM + Bio)
│   └── sample-jee-paper.json          # 15 authentic JEE questions with LaTeX
├── storage/
│   ├── database-schema-master.sql     # Database 1: Super Admin Master DB schema
│   ├── database-schema-tenant.sql     # Database 2: Institute Tenant DB schema
│   ├── indexeddb-client-cache.js      # Browser IndexedDB persistence engine
│   └── sync-queue-manager.js          # Offline queue and network detection manager
├── index.html                         # Student CBT Exam Player (1:1 NTA layout)
├── login.html                         # Unified & White-Label Portal Gateway
├── PUBLIC-LINKS.txt                   # Shareable public HTTPS URLs
├── serve.js                           # Zero-dependency local Node.js server
├── start-platform.bat                 # One-click Windows launcher
├── STARTUP-BLUEPRINT.md               # Enterprise B2B SaaS blueprint & competitive teardown
└── README.md
```

---

## 📜 License & Copyright

Engineered with precision by **RannVijay** & **Barry**. Distributed under the MIT License.
