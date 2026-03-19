# 🧠 LocalMind – Local AI Assistant

LocalMind is a powerful **local AI assistant** built using **Flask + Ollama**.
It allows you to chat with a locally running LLM directly from your browser or terminal.

---

## 🚀 Features

* 💬 Chat with a local LLM (Llama 3.1 via Ollama)
* ⚡ Fast responses (runs locally, no internet needed)
* 🖥️ Web UI built with Flask
* 🧾 Chat history saved to file
* 🧹 Clear chat with `/clear` command
* 🔌 Simple and clean architecture

---

## 🏗️ Tech Stack

* **Backend:** Python, Flask
* **LLM Engine:** Ollama
* **Frontend:** HTML, CSS
* **API:** REST (local)

---

## 📂 Project Structure

```
localmind/
│
├── app.py
├── app.txt
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── favicon.png
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone hhttps://github.com/parthrugved/ollama-ai-assistant.git
cd localmind
```

### 2. Install dependencies

```bash
pip install flask requests
```

### 3. Install Ollama

Download from: https://ollama.com

---

## ▶️ Run the App

### Start Ollama

```bash
ollama run llama3.1
```

### Run Flask server

```bash
python app.py
```

### Open in browser

```
http://127.0.0.1:5000
```

---

## 💡 Usage

* Type your question in the input box
* Click **Send**
* View AI response instantly

### Special Commands

* `/clear` → Clears chat history

---

## 📸 Screenshot

*Add your UI screenshot here*

---

## 🔥 Future Improvements

* ⏳ Streaming responses (typing effect)
* 💬 Chat bubbles UI (ChatGPT-style)
* 🧠 Conversation memory
* 📂 Multiple chat sessions
* 🌙 Dark mode

---

## 🧠 How It Works

```
User → Flask → Ollama API → LLM → Response → UI
```

---

## 🤝 Contributing

Feel free to fork this repo and improve it!

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---

## 📌 Author

Built by Parth 🚀