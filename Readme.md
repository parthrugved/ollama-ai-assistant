# 🧠 LocalMind — Private AI Assistant (Fully Local)

<p align="center">
  <b>Run a ChatGPT-like assistant on your own machine — fast, private, and free.</b>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-blue">
  <img alt="Flask" src="https://img.shields.io/badge/Flask-Backend-black">
  <img alt="MongoDB" src="https://img.shields.io/badge/MongoDB-Database-green">
  <img alt="Ollama" src="https://img.shields.io/badge/Ollama-Local%20AI-orange">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-lightgrey">
  <img alt="Status" src="https://img.shields.io/badge/Status-Active-success">
</p>

---

## 🚀 Overview

**LocalMind** is a full-stack AI chat application that runs **entirely locally** using **Ollama**, with persistent memory powered by **MongoDB** and a clean, modern UI.

> No cloud. No tracking. No limits. Just your AI — on your machine.

---

## ✨ Features

### 🧠 AI & Streaming

* Local inference via **Ollama (llama3.1)**
* Token-by-token **streaming responses**
* Context-aware conversations

### 💾 Memory System

* Chat history stored in **MongoDB**
* Automatic context loading (last N messages)
* `/clear` command to reset memory instantly

### 🎨 UI & Rendering

* **Markdown rendering** (headings, lists, code)
* **Syntax highlighting** via highlight.js
* **Copy button** for code blocks
* Clean, responsive layout (desktop + mobile)

### ⚡ Performance & Privacy

* Fully local → **no API latency**
* **No rate limits**
* **100% private** data

---

## 🧰 Tech Stack

| Layer             | Technology                       |
| ----------------- | -------------------------------- |
| Backend           | Flask (Python)                   |
| AI Engine         | Ollama (llama3.1)                |
| Database          | MongoDB                          |
| Frontend          | HTML + Tailwind CSS + JavaScript |
| Markdown          | marked.js                        |
| Code Highlighting | highlight.js                     |

---

## 🏗️ Architecture

```text
Browser (UI)
    ↓
Flask API (main.py)
    ↓
Ollama (Local LLM)
    ↓
MongoDB (Chat Memory)
```

---

## 📁 Project Structure

```text
LocalMind/
├── main.py                # Flask backend
├── templates/
│   └── index.html        # UI template
├── static/
│   ├── css/
│   │   └── style.css     # Styling
│   ├── js/
│   │   └── script.js     # Frontend logic
│   └── favicon.png
└── README.md
```

---

## ⚙️ Setup (Quick Start)

### 1) Install dependencies

```bash
pip install flask pymongo requests
```

### 2) Setup MongoDB (macOS via Homebrew)

```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
```

### 3) Install Ollama & pull model

```bash
ollama pull llama3.1
```

### 4) Run the app

```bash
python3 main.py
```

Open: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 💬 Commands

### 🧹 Clear chat memory

```text
/clear
```

Deletes all documents in MongoDB (`localmind_db.history`).

---

## 🗃️ Database

* **Database:** `localmind_db`
* **Collection:** `history`

Example document:

```json
{
  "user": "Parth",
  "prompt": "What is Python?",
  "response": "Python is a programming language...",
  "timestamp": "2026-03-26T00:00:00Z",
  "length": 120
}
```

---

## 🎨 Markdown Support

Supported out-of-the-box:

* Headings (`##`, `###`)
* Bullet lists
* Code blocks
* Inline code
* Horizontal rules

````markdown
## 🚀 Example

- Clean UI
- Fast responses

```python
print("Hello from LocalMind")
````

````

---

## 🔧 Configuration

Edit in `main.py`:

```python
OLLAMA_URL = "http://localhost:11434/api/generate"
````

You can customize:

* Model (e.g., llama3.1 → others)
* DB / collection names
* Prompt template

---

## 🧠 Why LocalMind?

| Feature | LocalMind | Cloud AI    |
| ------- | --------- | ----------- |
| Privacy | ✅ Full    | ❌ Limited   |
| Cost    | ✅ Free    | ❌ Paid      |
| Speed   | ⚡ Fast    | 🌐 Variable |
| Control | ✅ Full    | ❌ Limited   |

---

## 🛣️ Roadmap

### 🔜 Upcoming Features

* [ ] Chat sessions (multi-conversation)
* [ ] Sidebar with chat history (ChatGPT-style UI)
* [ ] Dark mode 🌙
* [ ] Search conversations 🔍
* [ ] Export chats (JSON / Markdown)
* [ ] User authentication system 🔐
* [ ] Model switching (multiple Ollama models)
* [ ] Better memory (summarization instead of raw history)

---

## 📦 Git Setup (Initialize Repository)

```bash
git init
git add .
git commit -m "Initial commit - LocalMind"

git branch -M main
git remote add origin https://github.com/your-username/localmind.git
git push -u origin main
```

---

## 🤝 Contributing

PRs are welcome! Feel free to:

* Open issues
* Suggest features
* Improve UI/UX

---

## ⭐ Final Note

LocalMind is a **foundation for building real AI products locally**.

If you like this project, give it a ⭐ and extend it into something even bigger 🚀
