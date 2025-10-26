# GRC Risk Assessment Toolkit

## 1. Project Objective

This project demonstrates a practical Governance, Risk, and Compliance (GRC) workflow. It includes creating an asset register, performing a simplified risk assessment based on threats and vulnerabilities, and using a Python script (with Pandas) to automate the creation of a **Prioritised Risk Register**.

The goal is to show a practical understanding of risk management principles as taught in MSc modules like **Cybersecurity and Risk Management** and **Business Continuity**.

## 2. The Fictional Scenario

* **Company:** `Random Company Ltd.`
* **Size:** 50-employee UK startup.
* **Business:** A new mobile payment app that processes and stores **PII** (names, addresses) and **Financial Data** (transaction histories).
* **Compliance:** Subject to UK GDPR / DPA 2018.

## 3. Risk Methodology

The risk assessment uses a simple 3x3 qualitative matrix to calculate a **Risk Score**:

**Risk Score = Likelihood x Impact**

| Score | Likelihood | Impact |
| :--- | :--- | :--- |
| **1** | Low (Unlikely) | Low (Minor disruption) |
| **2** | Medium (Possible) | Medium (Reputational damage) |
| **3** | High (Very Likely) | High (Data breach, fines) |

This score is then mapped to a **Risk Level**:

* **High (6-9):** Needs immediate action.
* **Medium (3-4):** Needs a treatment plan.
* **Low (1-2):** Accept and monitor.

## 4. The Process

1.  **`assets.csv`:** An asset register was created to identify the company's "crown jewels" (e.g., databases, servers, laptops).
2.  **`risk_assessment.csv`:** A list of risks was brainstormed, linking specific **Threats** (e.g., *Ransomware*) and **Vulnerabilities** (e.g., *Unpatched server*) to each asset.
3.  **`generate_risk_register.py`:** This Python script:
    * Creates a `venv` to manage dependencies (Pandas).
    * Reads both `.csv` files into Pandas DataFrames.
    * Merges the two tables, linking risks to their asset details.
    * Calculates the `RiskScore` and maps the `RiskLevel` for every risk.
    * Sorts the final list by the highest risk.
    * Saves the complete report as `Prioritised_Risk_Register.csv`.

## 5. The Final Output (Top 5 Risks)

The script automatically generates the full register. Here is a summary of the top 5 risks identified for "Random Company Ltd.":

| Risk_ID | Threat | Vulnerability | RiskLevel | RiskScore | AssetName |
| :--- | :--- | :--- | :--- | :--- | :--- |
| R-001 | Phishing Attack | Untrained staff clicking malicious links | High | 9 | Customer PII Database |
| R-002 | Ransomware | Unpatched server vulnerability | High | 6 | AWS Production Environment |
| R-005 | Malicious Code Commit | Stolen developer credentials | High | 6 | GitHub Code Repository |
| R-009 | Privilege Escalation | Misconfigured user permissions on support... | High | 6 | Customer Support Portal |
| R-011 | User Session Hijacking | Stored XSS in user profile field | High | 6 | Customer Support Portal |

## 6. Recommended Controls (Example)

This register allows the business to prioritise action. For example:

* **For R-001 (Phishing):**
    * **Recommendation:** Implement mandatory company-wide **Security Awareness Training** (aligns with *Cyber Essentials*).
    * **Recommendation:** Deploy an **Email Filtering** solution, an Network-based IDS to detect malicious network signatures.

* **For R-002 (Ransomware):**
    * **Recommendation:** Implement a formal **Patch Management Policy** for all production servers.
    * **Recommendation:** Test **Business Continuity (BCP)** backup and recovery plans immediately, and updated backups in regular intervals.

* **For R-005 (Malicious Commit):**
    * **Recommendation:** Enforce **Multi-Factor Authentication (MFA)** on all GitHub accounts.
    * **Recommendation:** Implement a **branch protection rule** requiring peer review (PR) before merging to the `main` branch.