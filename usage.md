# 🚀 SentinelLite — Usage & Execution Guide

> Back to [Main Project Overview (README.md)](https://www.google.com/search?q=./README.md)

This guide explains how to set up, run, and test each module of **SentinelLite** step by step from your terminal.

---

## 🛠️ 1. Prerequisites & Setup

SentinelLite is written in pure **Python 3** and uses built-in standard libraries (`random`, `re`, `sqlite3`), so no heavy external installations are required to run Stages 1 to 3.

1. Clone the repository and navigate into the project folder:
   ```bash
   git clone https://github.com/HuzaifaMohammed00/SentinelLite.git
   cd SentinelLite
   ```

2. Make sure the `data/` folder exists before generating logs:
   ```bash
   mkdir -p data
   ```

---

## 🧪 2. Running Stage 1: Generate Sample Web Logs (`v0.1`)

Run `log_generator.py` to create a fresh `data/sample_access.log` file containing 50 lines of mixed normal requests and simulated web attacks (`SQL Injection` and `Unauthorized Admin Access`):

```bash
python3 src/log_generator.py
```

**Expected Output:**
```text
[+] Log file generated successfully!
```

**Verify the generated log file (first 3 lines):**
```bash
head -n 3 data/sample_access.log
```
```text
192.168.1.15 - [01/Nov/2026:14:36:11] "GET /login?user=admin' OR 1=1-- HTTP/1.1" 403
10.0.0.5 - [01/Nov/2026:14:36:11] "GET /products HTTP/1.1" 404
192.168.1.15 - [01/Nov/2026:14:36:11] "GET /products HTTP/1.1" 200
```

---

## 🔍 3. Running Stage 2: Parse Logs & Detect Attacks (`v0.2`)

Run `parser.py` to extract the `IP`, `Path`, and `HTTP Status Code` from every log line using `Regular Expressions`, classify malicious requests, and display unique attacker IPs using a Python `set`:

```bash
python3 src/parser.py
```

**Expected Output:**
```text
[+] Total events parsed: 50
[ALERT] SQL injection from 192.168.1.15 -> Status: 403
[ALERT] Unauthorized Admin access from 185.106.96.158 -> Status: 401
[ALERT] SQL injection from 185.106.96.158 -> Status: 200
...

[+] Unique Attacker IPs (using Set): {'192.168.1.15', '10.0.0.5', '185.106.96.158'}
```

---

## 🗄️ 4. Running Stage 3: SQLite Forensic Database (`v0.3` — Upcoming)

Once `src/database.py` is added in `v0.3`, you will run:

```bash
python3 src/database.py
```
This will save all non-normal attack events into `data/sentinel.db` and output statistical summaries of the top attacking IPs and successful `HTTP 200` breaches.
