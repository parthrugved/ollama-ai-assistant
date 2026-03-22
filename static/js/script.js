function addCopyButtons() {
    document.querySelectorAll("pre").forEach((block) => {
        if (block.querySelector(".copy-btn")) return;

        const button = document.createElement("button");
        button.innerText = "Copy";
        button.className = "copy-btn";

        button.onclick = () => {
            navigator.clipboard.writeText(block.innerText);
            button.innerText = "Copied!";
            setTimeout(() => button.innerText = "Copy", 1500);
        };

        block.appendChild(button);
    });
}

function scrollToBottom() {
    const chat = document.getElementById("chat");
    chat.scrollTop = chat.scrollHeight + 9999;
}

async function sendMessage() {
    const input = document.getElementById("prompt");
    const chat = document.getElementById("chat");

    const userText = input.value.trim();
    if (!userText) return;
    input.value = "";

    // USER MESSAGE — use createElement, NOT innerHTML +=
    const userDiv = document.createElement("div");
    userDiv.className = "flex justify-end";
    userDiv.innerHTML = `
        <div class="bg-blue-600 text-white px-6 py-3 rounded-2xl max-w-xs md:max-w-md shadow-sm break-words">
            ${userText.replace(/</g, "&lt;").replace(/>/g, "&gt;")}
        </div>
    `;
    chat.appendChild(userDiv);
    scrollToBottom();

    // AI MESSAGE
    const aiDiv = document.createElement("div");
    aiDiv.className = "flex justify-start";

    const aiBubble = document.createElement("div");
    aiBubble.className = "px-6 py-5 rounded-2xl w-full shadow-sm border border-gray-200";
    aiBubble.style.backgroundColor = "rgb(249, 250, 251)";

    aiDiv.appendChild(aiBubble);
    chat.appendChild(aiDiv);
    scrollToBottom();

    try {
        const res = await fetch("/stream", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt: userText })
        });

        const reader = res.body.getReader();
        const decoder = new TextDecoder();

        let fullText = "";

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            const chunk = decoder.decode(value, { stream: true });
            fullText += chunk;

            let formatted = fullText
                .replace(/^(## .*)/gm, "$1\n\n---\n\n")
                .replace(/^(### .*)/gm, "$1\n\n")
                .replace(/\n{1}/g, "\n\n");

            aiBubble.innerHTML = marked.parse(formatted);

            aiBubble.querySelectorAll("pre code").forEach((block) => {
                hljs.highlightElement(block);
            });

            addCopyButtons();
            scrollToBottom();
        }
    } catch (err) {
        aiBubble.innerHTML = "<p style='color:red'>Error connecting to AI. Make sure the server is running.</p>";
        console.error(err);
    }
}

// ENTER KEY — keydown is reliable on both desktop and mobile keyboards
document.getElementById("prompt").addEventListener("keydown", function (e) {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

// MOBILE SIDEBAR TOGGLE
function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    const overlay = document.getElementById("sidebar-overlay");

    sidebar.classList.toggle("-translate-x-full");
    overlay.classList.toggle("hidden");
}