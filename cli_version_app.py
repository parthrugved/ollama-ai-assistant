import requests

url = "http://localhost:11434/api/generate"

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

    response = requests.post(url, json=data)

    print(f"AI : {response.json()["response"]}")

    file = open("cli_version_app.txt","+a")
    file.write(f"You: {prompt} {"\n"}AI: {response.json()["response"] + "\n \n"}")
    file.close()