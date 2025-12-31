
# 🚀 GitHub Profile Analyzer  
### AI-Assisted GitHub Scoring & Recruiter Visibility Platform

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-Production-teal?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/Backend-REST%20API-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/AI-Local%20LLM-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" />
</p>

---

## 📌 Overview

**GitHub Profile Analyzer** is a full-stack web application that evaluates GitHub profiles using real contribution data, calculates a **GitHub Score (0–100)**, identifies **current profile drawbacks**, and provides **actionable recommendations** to improve recruiter visibility.

The platform combines **deterministic scoring logic** with **optional local AI insights**, ensuring **fast responses, zero paid APIs, and production-ready reliability**.

---

## ✨ Key Features

### 🔢 GitHub Scoring Engine
- Computes a normalized score using:
  - Followers & visibility
  - Repository count
  - Repository documentation quality
  - Stars & forks (community impact)
  - Profile completeness (bio & links)

### 🔍 Drawback Detection
- Automatically identifies weak areas such as:
  - Missing bio or portfolio
  - Poor repository descriptions
  - Low community engagement
  - Low project visibility

### 🛠️ Improvement Suggestions
- Clear, practical steps to improve:
  - GitHub score
  - Profile credibility
  - Recruiter first impression

### 🎯 Recruiter-Focused Insights
- Explains **why recruiters might skip a profile**
- Shows **how improvements increase hiring chances**

### 🤖 Optional Local AI (No Paid APIs)
- Uses **local LLMs via Ollama**
- Fully offline-capable
- Runs asynchronously (never blocks UI)
- Graceful fallback when AI is unavailable

### 🎨 Modern UI
- Responsive dashboard
- Animated evaluation pipeline
- Score ring animation
- Glassmorphism cards
- AOS scroll animations

---

## 🧠 System Design Philosophy

This project follows **production-grade architecture**:

```

User Interface
↓
FastAPI Routes
↓
Deterministic Analysis (Instant)
↓
Background AI Refinement (Optional)

```

### Why this matters:
- ⚡ Fast response times
- 🛡️ AI never blocks user experience
- 📈 Scalable & maintainable
- 💼 Mirrors real hiring platforms

---

## 🏗️ Project Structure

```

github-profile-analyzer/
│
├── app/
│   ├── main.py                # FastAPI entry point
│   ├── routes.py              # Web routes
│   │
│   ├── services/
│   │   ├── github_api.py      # GitHub API integration
│   │   └── score_engine.py    # Scoring logic
│   │
│   ├── ai/
│   │   ├── profile_analyzer.py
│   │   ├── fast_recruiter_rules.py
│   │   ├── prompt_templates.py
│   │   └── local_llm_client.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   └── result.html
│   │
│   └── static/
│       ├── css/style.css
│       └── js/main.js
│
├── .gitignore
├── requirements.txt
└── README.md

````

---

## 🧮 Scoring Criteria (0–100)

| Category | Description |
|--------|------------|
| Popularity | Followers & reach |
| Repositories | Public project count |
| Repo Quality | Descriptions & clarity |
| Community Impact | Stars + forks |
| Profile Completeness | Bio & external links |

Each category is normalized to ensure **fair scoring across experience levels**.

---

## ⚙️ Tech Stack

### Backend
- **Python**
- **FastAPI**
- **Requests**
- **Jinja2**

### Frontend
- **HTML5**
- **CSS3**
- **JavaScript**
- **AOS (Animate On Scroll)**

### AI (Optional)
- **Ollama**
- **Local LLMs (Gemma / Mistral)**

---

## 🚀 Getting Started

### 1️⃣ Clone Repository
```bash
git clone https://github.com/venkat-0706/Github-Profile-Analyzer.git
cd Github-Profile-Analyzer
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Application

```bash
uvicorn app.main:app --reload --port 9000
```

Open 👉 **[http://127.0.0.1:9000](http://127.0.0.1:9000)**

---

## 🔐 GitHub API Rate Limits

* Works **without a token** (limited requests)
* For higher limits, add `.env`:

```
GITHUB_TOKEN=your_token_here
```

---

## 🎯 Why This Project Stands Out

✔ Real-world hiring problem
✔ Clean backend architecture
✔ Performance-optimized
✔ AI used responsibly
✔ No paid APIs
✔ Recruiter-centric design

This is **not a demo project** — it reflects **production-level engineering decisions**.

---

## 📌 Future Enhancements

* Live AI feedback polling
* Profile comparison
* GitHub Actions CI
* Dockerized deployment
* Resume–GitHub score correlation

---

## 🧑‍💻 Author

**Chandu 💗**
Backend Engineer | Python | FastAPI | AI-Driven Developer Tools

---

