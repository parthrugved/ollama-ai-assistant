from flask import Flask , request , render_template
import requests
from flask import Response
import json

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.route("/", methods=["GET"])
def index():
    messages = []

    try:
        with open("app.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("User:"):
                    messages.append({"role": "user", "text": line.replace("User:", "").strip()})
                elif line.startswith("Assistant:"):
                    messages.append({"role": "ai", "text": line.replace("Assistant:", "").strip()})
    except:
        pass

    return render_template("index.html", messages=messages)

@app.route("/stream", methods=["POST"])
def stream():
    prompt = request.json.get("prompt")

    #  CLEAR COMMAND
    if prompt.strip().lower() == "/clear":
        with open("app.txt", "w") as f:
            pass
        return Response("Chat cleared 🧹", content_type="text/plain")

    #  LOAD HISTORY
    history = ""
    try:
        with open("app.txt", "r") as f:
            history = f.read()
    except:
        pass
    
    history = history[-3000:]
    # Build context
    full_prompt = history + f"""
    User: {prompt}

    Assistant:
    Respond in a clean, structured format:
    - Use headings (##, ###)
    - Add emojis to headings (🤖 🧠 📌 🚀 🔥 👍 ✍️ 🎖️ 🏅 💻 👨‍💻)
    - Use bullet points
    - Add spacing between sections
    - Format code using triple backticks
    - Make response visually clean and easy to read
    """

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

        #  SAVE WITH CONTEXT FORMAT
        with open("app.txt", "a") as file:
            file.write(f"User: {prompt}{"\n"}Assistant: {full_response} {"\n \n \n"}")

    return Response(generate(), content_type="text/plain")

app.run(debug=False)