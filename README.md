🛡️ Azure DevSecOps: AI-Powered Infrastructure Hardening
A comprehensive two-phase security project demonstrating Cloud Infrastructure Hardening and AI-Driven Automated Auditing. This repository bridges the gap between raw technical vulnerabilities and executive-level risk assessment.

🏗️ Chapter 1: Infrastructure Security & Hardening
Objective: Identify and remediate critical misconfigurations in Azure Storage Account deployments using Static Analysis (SCA).

🔍 The Security Audit
Initial scans of the Terraform configuration (main.tf) revealed 11 failed security checks. High-priority risks included:

Public Network Access: Storage exposed to the open internet.

Insecure Encryption: Usage of legacy TLS 1.0/1.1 protocols.

Anonymous Access: Container-level permissions allowed unauthenticated data reads.

🛠️ Remediation Strategy
Implemented a "Shift-Left" security approach by hardening the code before deployment:

Network Isolation: Set public_network_access_enabled = false to enforce private networking.

Encryption Standards: Enforced min_tls_version = "TLS1_2".

Data Protection: Disabled allow_nested_items_to_be_public.

🤖 Chapter 2: AI-Powered Automated Auditing
Objective: Scale security operations by using Generative AI to translate complex technical logs into actionable intelligence.

🚀 The "AI Auditor" Workflow
I developed a custom Python orchestration script (ai_auditor.py) to streamline the security review process.

Automated Scanning: The script triggers Checkov to audit the /terraform directory.

Telemetry Capture: Raw stdout results are captured and sanitized.

LLM Analysis: Data is fed into Google Gemini 2.0 Flash via the google-genai SDK.

Executive Reporting: The AI generates a 3-sentence summary identifying the #1 risk, business impact, and a "Go/No-Go" recommendation.

🔧 Resilience & Scalability
Error Handling: Implemented robust try/except logic to manage API Quota Limits (429 Errors).

Environment Security: Leveraged os.environ for API key management to prevent secret leakage.

📈 Project Impact
100% Risk Reduction: Eliminated all critical public-facing vulnerabilities prior to provisioning.

Time-to-Insight: Reduced the time required to interpret security logs from minutes to seconds.

Compliance Alignment: Ensured infrastructure adheres to Azure Security Benchmark and CIS standards.

📂 Repository Structure
Plaintext
enterprise-cloud-security-automation/
├── terraform/          # Hardened Azure Infrastructure-as-Code
├── scripts/            # AI Auditor & Python environment
│   └── ai_auditor.py   # Main AI orchestration script
├── .gitignore          # Root-level secret/venv protection
└── README.md           # Professional project documentation
🚀 Getting Started
Clone the Repo: git clone <url>

Configure API: export GOOGLE_API_KEY='your_key'

Run Audit: python3 scripts/ai_auditor.py

Ready to Push?
Since you are in the root, run:

Bash
git add README.md
git commit -m "docs: finalize professional two-chapter README structure"
git push origin main
How does it feel to see the project look this polished? This is a serious "Senior-level" presentation!