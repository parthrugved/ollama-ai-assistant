# 🧠 LocalMind – Local AI Chat Assistant

<p align="center">
  🚀 Your own private ChatGPT — running fully offline on your machine  
</p>

<p align="center">
  <img src="screenshot 1.png" alt="LocalMind UI" width="80%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Backend-Flask-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/AI-Ollama-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Model-Llama%203.1-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
</p>

---

## 🌟 What is LocalMind?

**LocalMind** is a powerful **full-stack AI assistant** that runs entirely on your local machine using **Ollama**.

No API keys. No cloud. No limits.
Just pure local AI ⚡

> 💡 Think: *ChatGPT + Privacy + Full Control*

---

## ✨ Features

### 🤖 AI Capabilities

* 💬 Chat with LLM (**Llama 3.1 via Ollama**)
* ⚡ Real-time **streaming responses** (typing effect)
* 🧠 **Conversation memory** (context-aware replies)
* 💾 Persistent chat history (`app.txt`)
* 🧹 `/clear` command to reset chat

---

### 🎨 UI / UX

* 🖥️ Clean and minimal chat interface
* 📱 Fully responsive (mobile + desktop)
* 🧭 Sidebar navigation (mobile-friendly toggle)
* ⚡ Smooth auto-scroll during streaming
* 💬 Chat bubbles (user vs AI)

---

### 💻 Developer Features

* 🧾 **Markdown rendering** (formatted responses)
* 💻 **Syntax highlighting** (highlight.js)
* 📋 **Copy button for code blocks**
* 📐 Clean structured responses (headings, lists, spacing)
* ⚡ Fast local inference

---

### 🧪 Extras

* 🖥️ CLI version included
* 🔌 Works completely offline
* 🧠 Context-aware AI replies

---

## 🏗️ Tech Stack

| Layer        | Technology                     |
| ------------ | ------------------------------ |
| Backend      | Python, Flask                  |
| AI Engine    | Ollama (Llama 3.1)             |
| Frontend     | HTML, Tailwind CSS, JavaScript |
| Markdown     | Marked.js                      |
| Highlighting | Highlight.js                   |
| Storage      | Local file (`app.txt`)         |

---

## 📂 Project Structure

```bash
OPEN WEB UI/
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── favicon.png
│
├── templates/
│   └── index.html
│
├── main.py              # Flask app (web UI + streaming)
├── cli_version_app.py   # CLI version
├── app.txt              # Chat memory
├── README.md
├── screenshot1.png
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/parthrugved/ollama-ai-assistant.git
cd ollama-ai-assistant
```

---

### 2️⃣ Install dependencies

```bash
pip install flask requests
```

---

### 3️⃣ Install Ollama

Download and install:
👉 https://ollama.com

---

## ▶️ Run the App

### 🔹 Start Ollama

```bash
ollama run llama3.1
```

---

### 🔹 Start Flask Server

```bash
python main.py
```

---

### 🌐 Open in browser

```
http://127.0.0.1:5000
```

---

## 💡 Usage

1. Type your message
2. Click **Send**
3. Watch AI respond in real-time ⚡

---

### 🔥 Commands

| Command  | Description         |
| -------- | ------------------- |
| `/clear` | Clears chat history |

---

## 🧠 How Memory Works

LocalMind stores chat history in `app.txt` and sends recent context to the model:

```text
User: Hello
Assistant: Hi!

User: Explain AI
Assistant:
```

👉 This allows the AI to **remember previous conversation context**.

---

## ⚡ Streaming Architecture

```text
Frontend (JavaScript fetch)
        ↓
Flask (/stream endpoint)
        ↓
Ollama API (stream=True)
        ↓
Token-by-token response
        ↓
Live UI rendering
```

---

## 💻 Code Highlighting & Copy Feature

LocalMind automatically enhances developer experience:

* 🎨 Syntax-highlighted code
* 📋 One-click copy button

```python
def greet():
    print("Hello from LocalMind 🚀")
```

---

## 🚀 Future Improvements

* 🧠 Multi-chat system (ChatGPT-style sidebar)
* 🗂️ Chat sessions & titles
* 🌙 Dark mode
* ⚡ WebSocket-based streaming
* 🗄️ Database storage (SQLite / MongoDB)
* 🔐 Authentication system

---

## 🤝 Contributing

Contributions are welcome!

```bash
# Fork the repo
# Create a new branch
git checkout -b feature-name

# Commit changes
git commit -m "Added feature"

# Push
git push origin feature-name
```

Then open a Pull Request 🚀

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---

## 👨‍💻 Author

Built with 👨‍💻 by **Parth**

---

## 🧠 Final Thought

> "The future of AI is not just powerful — it's personal."

Welcome to **LocalMind** ⚡
