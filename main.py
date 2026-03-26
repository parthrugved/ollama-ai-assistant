from flask import Flask, request, render_template, Response
import requests
import json
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"

client = MongoClient("mongodb://localhost:27017/")
db = client["localmind_db"]
collection = db["history"]


# HOME ROUTE 
@app.route("/", methods=["GET"])
def index():
    messages = []

    history_docs = collection.find().sort("timestamp", 1).limit(50)

    for doc in history_docs:
        messages.append({"role": "user", "text": doc.get("prompt", "")})
        messages.append({"role": "ai", "text": doc.get("response", "")})

    return render_template("index.html", messages=messages)


# STREAM ROUTE
@app.route("/stream", methods=["POST"])
def stream():
    prompt = request.json.get("prompt")

    #  CLEAR COMMAND
    if prompt.strip().lower() == "/clear":
        collection.delete_many({})
        return Response("Chat memory cleared 🧹", content_type="text/plain")

    #  LOAD HISTORY FROM DB
    history_docs = collection.find().sort("timestamp", -1).limit(10)

    history = ""
    for doc in reversed(list(history_docs)):
        prompt_text = doc.get("prompt", "")
        response_text = doc.get("response", "")
        history += f"User: {prompt_text}\nAssistant: {response_text}\n"

    #  BUILD PROMPT
    full_prompt = history + f"""
    User: {prompt}

    Assistant:
    Respond in a clean, structured format:
    - Use headings (##, ###)
    - Add emojis to headings (🤖 🧠 🎯 📌 🚀 🔥 👍 ✍️ 🎖️ 🏅 💻 👨‍💻 🧹 💪 )
    - Use bullet points
    - Add spacing between sections
    - Format code using triple backticks
    - Make response visually clean and easy to read
    """

    #  STREAM RESPONSE
    def generate():
        res = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3.1",
                "prompt": full_prompt,
                "stream": True
            },
            stream=True
        )

        full_response = ""

        for line in res.iter_lines():
            if line:
                chunk = json.loads(line.decode("utf-8"))
                token = chunk.get("response", "")

                full_response += token
                yield token

        # SAVE TO DB
        collection.insert_one({
            "user": "Parth",
            "prompt": prompt,
            "response": full_response,
            "timestamp": datetime.utcnow(),
            "length": len(full_response)
        })

    return Response(generate(), content_type="text/plain")

if __name__ == "__main__":
    app.run(debug=False)