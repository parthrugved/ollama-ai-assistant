# 🧠 LocalMind – Local AI Chat Assistant

> A powerful **local AI assistant** with streaming responses, memory, and a modern web UI — built using **Flask + Ollama**.

---

## 🚀 Overview

LocalMind is a full-stack AI chat application that runs **completely locally** using Ollama.
It features **real-time streaming responses**, **chat memory**, and a clean **ChatGPT-like interface**.

No APIs. No cloud. Just your machine ⚡

---

## ✨ Features

* 💬 Chat with LLM (Llama 3.1 via Ollama)
* ⚡ **Streaming responses** (typing effect like ChatGPT)
* 🧠 **Conversation memory** (context-aware replies)
* 💾 Persistent chat history (`app.txt`)
* 🧹 `/clear` command to reset chat
* 🖥️ Modern UI with Tailwind CSS
* 🧪 CLI version included

---

## 🏗️ Tech Stack

| Layer     | Technology                     |
| --------- | ------------------------------ |
| Backend   | Python, Flask                  |
| AI Engine | Ollama (Llama 3.1)             |
| Frontend  | HTML, Tailwind CSS, JavaScript |
| Storage   | Local file (`app.txt`)         |

---

## 📂 Project Structure

```id="p7k8a3"
OPEN WEB UI/
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── favicon.png
│
├── templates/
│   └── index.html
│
├── main.py              # Flask app (web UI + streaming)
├── cli_version_app.py   # CLI version of assistant
├── app.txt              # Chat history (memory)
├── Readme.md
├── screenshot1.png
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash id="wq4l9k"
git clone https://github.com/your-username/localmind.git
cd localmind
```

---

### 2. Install dependencies

```bash id="ozg2n1"
pip install flask requests
```

---

### 3. Install Ollama

Download and install from:
👉 https://ollama.com

---

## ▶️ Run the App

### Start Ollama

```bash id="snx3rv"
ollama run llama3.1
```

---

### Run Flask server

```bash id="p0z8yb"
python main.py
```

---

### Open in browser

```id="k4m9cx"
http://127.0.0.1:5000
```

---

## 💡 Usage

* Type a message in the input box
* Click **Send**
* Watch AI respond in real-time ✨

---

### 🔥 Commands

* `/clear` → Clears chat history

---

## 🧠 How Memory Works

LocalMind stores chat history in `app.txt` and sends recent conversation as context:

```id="5mdqg2"
User: Hello
Assistant: Hi!

User: What is Python?
Assistant:
```

👉 This allows the AI to remember previous messages.

---

## ⚡ Streaming Architecture

```id="f9c2kd"
Frontend (JS fetch)
        ↓
Flask (/stream)
        ↓
Ollama API (stream=True)
        ↓
Token-by-token response
        ↓
Live UI update
```

---

## 📸 Screenshot

<img src="screenshot 1.png">

---

## 🔥 Future Improvements

* 🧠 Multi-chat system (ChatGPT-style sidebar)
* 📂 Chat sessions & titles
* 🌙 Dark mode
* ⚡ Faster streaming
* 🗂️ JSON/DB-based storage

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork and improve this project.

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---

## 👨‍💻 Author

Built by **Parth** 🚀

---
