# 🛡️ SentinelLite — Automated Web Log Triage & Threat Intelligence Tool

> **Author:** Huzaifa Mohammed ([@HuzaifaMohammed00](https://github.com/HuzaifaMohammed00))  
> **Category:** SOC Automation & Web Security Triage (`SOAR-Lite`)  
> **Tech Stack:** `Python 3`, `Regular Expressions (re)`, `SQLite3`, `VirusTotal API v3`

---

## 📌 Project Overview

**SentinelLite** is a lightweight, modular command-line security tool designed to automate the daily workflow of a **SOC Analyst** and **Web Penetration Tester**. Instead of inspecting thousands of raw web server logs by hand, SentinelLite parses standard `Apache/Nginx` access logs, detects web exploitation attempts (`SQL Injection`, `Unauthorized Admin Probing`, `Path Traversal`), stores suspicious events in a relational `SQLite` database for statistical threat hunting, enriches attacker IPs with threat intelligence, and generates a clean `Markdown` incident report.

👉 **Want to run or test the tool?** Read the step-by-step [Usage \& Execution Guide (USAGE.md)](https://www.google.com/search?q=./USAGE.md).

---

## ✨ Key Features

- **Standard Web Log Simulation (`log_generator.py`):** Generates realistic `Apache/Nginx` access logs combining normal user traffic with real-world web attack payloads and known `Cobalt Strike C2` indicators.
- **Regex Extraction & Attack Classification (`parser.py`):** Extracts visitor `IPv4` addresses, requested `URI` paths, and `HTTP` status codes using Python `re`, and classifies attacks (`SQL Injection`, `Unauthorized Admin Access`, or `Normal`).
- **Unique Threat Tracking (`Set` Optimization):** Uses Python `set` data structures for fast $O(1)$ lookup and deduplication of unique attacker IP addresses.
- **Forensic Database & SOC Analytics (`database.py`):** *(Upcoming in v0.3)* Saves suspicious events into `SQLite` using parameterized queries (`?`) and runs `GROUP BY` statistical queries to rank top attackers and spot `HTTP 200 OK` breaches.
- **Threat Intelligence & Cyber Kill Chain Mapping (`intel.py` & `reporter.py`):** *(Upcoming in v0.4 - v1.0)* Checks attacker IP reputation via `VirusTotal API` (with offline fallback) and maps each alert to its stage in the **Lockheed Martin Cyber Kill Chain**.

---

## 🗂️ Project Structure

```text
SentinelLite/
├── data/
│   └── sample_access.log      # Generated standard Apache/Nginx access logs
├── src/
│   ├── log_generator.py       # v0.1: Standard web access log generator
│   └── parser.py              # v0.2: Regex log parser & attack classifier
├── USAGE.md                   # Step-by-step installation & execution guide
└── README.md                  # Project overview & version history
```

---

## 🕒 Version History & Release Roadmap (Changelog)

This project is built incrementally using clean, modular software engineering practices:

| Version | Release Date | Status | What Was Added |
| :--- | :--- | :--- | :--- |
| **`v0.1`** | `2026-11-02` | ✅ Completed | Initial project structure and `src/log_generator.py` to simulate standard `Apache/Nginx` web logs with embedded `SQLi` and `C2` traffic. |
| **`v0.2`** | `2026-11-06` | ✅ Completed | Built `src/parser.py` using `Regex` functions (`parser_ip`, `parser_path`, `parser_status`), `zip()` stream linking, `classify_request()`, and `set()` deduplication for unique attacker IPs. |
| **`v0.3`** | `Upcoming` | 🔄 Next Step | Build `src/database.py` to store detected attacks in `SQLite` and run `SOC` statistical queries (`Top Attackers` & `200 OK Breaches`). |
| **`v0.4`** | `Planned` | ⏳ Planned | Build `src/intel.py` for `VirusTotal API` IP reputation checks (with offline mode) and `Cyber Kill Chain` stage classification. |
| **`v1.0`** | `Planned` | ⏳ Planned | Build `src/reporter.py` and `main.py` to export the final automated `incident_report.md`. |

---

## 📖 How to Run

For full setup instructions, stage-by-stage commands, and expected terminal outputs, check out the dedicated [Usage \& Execution Guide (USAGE.md)](https://www.google.com/search?q=./USAGE.md).

---

## 👤 Author

**Huzaifa Mohammed**  
Software Engineering Student & Cybersecurity Analyst in Training  
- **GitHub:** [@HuzaifaMohammed00](https://github.com/HuzaifaMohammed00)
