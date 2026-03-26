import requests
from pymongo import MongoClient

OLLAMA_URL = "http://localhost:11434/api/generate"

client = MongoClient("mongodb://localhost:27017/")
db = client["localmind_db_cli"]
collection = db["history"]

while True:
    prompt = input("You : ")

    if "/exit" in prompt.lower():
        break
    if "/quit" in prompt.lower():
        break
    if "/clear" in prompt.lower():
        with open("cli_version_app.txt", "w") as f:
            pass

    data = {
        "model": "llama3.1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=data)

    print(f"AI : {response.json()["response"]}")

    file = open("cli_version_app.txt","+a")
    file.write(f"You: {prompt} {"\n"}AI: {response.json()["response"] + "\n \n"}")
    file.close()

    collection.insert_one({
        "user": "Parth",
        "prompt": prompt,
        "response": response.json()["response"]
    })
    