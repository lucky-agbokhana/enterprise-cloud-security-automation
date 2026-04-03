# 🛡️ Azure DevSecOps: AI-Powered Infrastructure Hardening

> A comprehensive two-phase security project demonstrating **Cloud Infrastructure Hardening** and **AI-Driven Automated Auditing** — bridging the gap between raw technical vulnerabilities and executive-level risk assessment.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Chapter 1: Infrastructure Security & Hardening](#chapter-1-infrastructure-security--hardening)
- [Chapter 2: AI-Powered Automated Auditing](#chapter-2-ai-powered-automated-auditing)
- [Project Impact](#project-impact)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Tech Stack](#tech-stack)

---

## Project Overview

This project simulates a real-world DevSecOps engagement where insecure cloud infrastructure is identified, hardened, and monitored using a combination of static analysis tooling and Generative AI. The result is a fully automated security pipeline that produces executive-ready reports from raw scan data.

---

## 🏗️ Chapter 1: Infrastructure Security & Hardening

**Objective:** Identify and remediate critical misconfigurations in Azure Storage Account deployments using Static Code Analysis (SCA).

### 🔍 The Security Audit

Initial scans of the Terraform configuration (`main.tf`) revealed **11 failed security checks**. High-priority risks included:

| Risk | Description |
|------|-------------|
| 🌐 Public Network Access | Storage account exposed to the open internet |
| 🔓 Insecure Encryption | Legacy TLS 1.0/1.1 protocols in use |
| 👤 Anonymous Access | Container-level permissions allowed unauthenticated data reads |

### 🛠️ Remediation Strategy

Implemented a **"Shift-Left"** security approach by hardening the infrastructure code before deployment:

- **Network Isolation** — Set `public_network_access_enabled = false` to enforce private networking
- **Encryption Standards** — Enforced `min_tls_version = "TLS1_2"`
- **Data Protection** — Disabled `allow_nested_items_to_be_public`

---

## 🤖 Chapter 2: AI-Powered Automated Auditing

**Objective:** Scale security operations by using Generative AI to translate complex technical logs into actionable intelligence.

### 🚀 The AI Auditor Workflow

A custom Python orchestration script (`ai_auditor.py`) was developed to automate the entire security review process end-to-end:

```
Checkov Scan → Raw stdout capture → Gemini 2.0 Flash → Executive Summary
```

1. **Automated Scanning** — Script triggers Checkov to audit the `/terraform` directory
2. **Telemetry Capture** — Raw `stdout` results are captured and sanitized
3. **LLM Analysis** — Data is fed into Google Gemini 2.0 Flash via the `google-genai` SDK
4. **Executive Reporting** — AI generates a 3-sentence summary identifying the #1 risk, business impact, and a **Go/No-Go** deployment recommendation

### 🔧 Resilience & Scalability

- **Error Handling** — Robust `try/except` logic manages API Quota Limits (429 errors) gracefully
- **Environment Security** — `os.environ` used for API key management to prevent secret leakage

---

## 📈 Project Impact

| Metric | Result |
|--------|--------|
| 🔴 Critical Vulnerabilities | Reduced from 11 → 0 |
| ⏱️ Time-to-Insight | Security logs interpreted in seconds vs. minutes |
| ✅ Compliance | Aligned with Azure Security Benchmark & CIS standards |

---

## 📂 Repository Structure

```
enterprise-cloud-security-automation/
├── terraform/               # Hardened Azure Infrastructure-as-Code
│   └── main.tf              # Storage Account with security controls applied
├── scripts/                 # AI Auditor & Python environment
│   └── ai_auditor.py        # Main AI orchestration script
├── .gitignore               # Root-level secret/venv protection
└── README.md                # Project documentation
```

---

## 🚀 Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/lucky-agbokhana/enterprise-cloud-security-automation.git
cd enterprise-cloud-security-automation
```

**2. Set up Python environment**
```bash
cd scripts
python3 -m venv .venv
source .venv/bin/activate
pip install -q -U google-genai checkov
```

**3. Configure your API key**
```bash
export GOOGLE_API_KEY='your_gemini_api_key_here'
```

**4. Run the AI Security Audit**
```bash
python3 ai_auditor.py
```

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|---------|
| **Terraform** | Infrastructure-as-Code (Azure) |
| **Checkov** | Static security analysis |
| **Python 3** | Orchestration scripting |
| **Google Gemini 2.0 Flash** | AI-powered report generation |
| **google-genai SDK** | Gemini API integration |
| **Git & GitHub** | Version control & portfolio hosting |

---

> *"Finding the vulnerability is only half the job. The other half is communicating the risk to people who don't write code."*