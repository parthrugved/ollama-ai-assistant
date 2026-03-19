from flask import Flask , request , render_template
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.route("/", methods=["GET","POST"])
def index():
    response_text = ""

    if request.method == "POST":
        prompt = request.form.get("prompt")

        res = requests.post(OLLAMA_URL,json={
            "model": "llama3.1",
            "prompt": prompt,
            "stream": False
        })

        response_text = res.json()["response"]

        file = open("app.txt","+a")
        file.write(f"You: {prompt} {"\n"}AI: {response_text + "\n \n"}")
        file.close()

        if prompt.strip().lower() == "/clear":
            with open("app.txt", "w") as file:
                pass

    return render_template("index.html" , response=response_text)

@app.route("/history")
def history():
        with open("app.txt", "r") as f:
            return f.read()
    

app.run(debug=False)