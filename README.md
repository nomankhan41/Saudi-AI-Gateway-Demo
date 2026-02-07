# 🇸🇦 Saudi AI Gateway (Enterprise Edition)
**PDPL-Compliant Middleware for Sovereign AI Infrastructure**

[![License: Proprietary](https://img.shields.io/badge/License-Enterprise-blue.svg)](mailto:noman.asif.khan.cs@gmail.com)
[![Status: Production Ready](https://img.shields.io/badge/Status-Dockerized-green.svg)]()

## 🚨 The Problem
Using OpenAI or Anthropic directly violates **Saudi PDPL Article 29** when sensitive data (Iqama IDs, IBANs, Royal Decrees) leaves the Kingdom's digital borders.

## 🛡️ The Solution
**Saudi AI Gateway** is a Dockerized middleware that sits between your internal applications and external LLMs. It enforces data sovereignty **locally** before any request hits the internet.

---

### 🎥 Watch the Verification Demo (30 Seconds)
**See the Kill Switch and Redaction Logic in action:**

[![Watch the Demo]](https://www.loom.com/share/0e164a714032417e90e1f803068e3d28)

<img width="1365" height="749" alt="image" src="https://github.com/user-attachments/assets/76afb32a-7c35-4e3c-8442-47a4734fe2cf" />


---

## 🔐 Key Features
1.  **Zero-Latency PII Redaction:** Automatically masks Saudi National IDs, Phone Numbers, and Banking Data.
2.  **Role-Based Access Control (RBAC):** Junior agents cannot authorize high-value transactions.
3.  **Financial "Kill Switch":** Instant emergency shutdown if spending anomalies are detected.
4.  **Offline-Ready:** Runs entirely on-premise or within a private cloud (KSA Region).

## 🛠️ Technology Stack
* **Engine:** Python 3.11 + FastAPI (High Performance Async)
* **Privacy:** Microsoft Presidio + Custom Regex (Hybrid Detection)
* **NLP:** Spacy `en_core_web_lg` (Local Processing, No API calls for redaction)
* **Deployment:** Docker Container (Platform Agnostic)

## 📜 verify_compliance.py
This repository includes the `verify_compliance.py` audit script. You can run this against the deployed gateway to verify:
* ✅ Redaction of confidential data.
* ✅ Blocking of unauthorized spending.
* ✅ System resilience during attacks.

## 💼 Enterprise Licensing
This software is available for **Enterprise Licensing** and **Source Code Acquisition**.
Perfect for Systems Integrators (Master Works, Mozn, 10Pearls) building government solutions.

**📩 Contact for Demo / PoC:**
* **Lead Architect:** [Noman Asif Khan](https://www.linkedin.com/in/noman-asif-khan-250358295/)
* **Email:** noman.asif.khan.cs@gmail.com
