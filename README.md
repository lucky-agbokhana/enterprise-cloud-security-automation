# Azure Infrastructure Security Audit & Hardening

## 🎯 Project Overview
This project demonstrates a proactive DevSecOps approach to securing Cloud Infrastructure-as-Code (IaC). I performed a security audit on an Azure Storage Account deployment, identified critical misconfigurations using static analysis, and implemented automated remediations.

## 🛠️ Tech Stack
* **Cloud Provider:** Azure
* **IaC Tool:** Terraform
* **Security Scanner:** Checkov (SCA/Static Analysis)
* **Environment:** Azure Cloud Shell

## 🔍 The Challenge (Problem)
The initial Terraform configuration (`main.tf`) contained several high-severity security vulnerabilities:
* **Public Network Access:** The storage account was exposed to the open internet.
* **Insecure Encryption:** The configuration allowed legacy TLS versions (1.0/1.1).
* **Anonymous Access:** Container-level permissions allowed unauthenticated data reads.

## 🛡️ The Solution (Action)
1. **Audit:** Ran `checkov` against the Terraform plan to identify 11 failed security checks.
2. **Remediation:** * Set `public_network_access_enabled = false` to enforce private networking.
    * Enforced `min_tls_version = "TLS1_2"`.
    * Disabled `allow_nested_items_to_be_public`.
3. **Validation:** Re-scanned the code to confirm a 100% reduction in critical failures.
4. **Deployment:** Provisioned the hardened infrastructure successfully using `terraform apply`.

## 📈 Key Results
* **Risk Reduction:** Eliminated all critical public-facing vulnerabilities before deployment.
* **Compliance:** Aligned infrastructure with Azure Security Benchmark and CIS standards.
* **Automation:** Demonstrated a repeatable "Shift-Left" security workflow.