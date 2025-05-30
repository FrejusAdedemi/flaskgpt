function addToLog(message, type = "bot") {
    const output = document.querySelector('#gpt-output');
    const messageEl = document.createElement('div');
    messageEl.classList.add('message-bubble', 'message');

    if (type === "user") {
        messageEl.classList.add('user-message');
    } else {
        messageEl.classList.add('bot-message');
    }

    messageEl.innerText = message;
    output.appendChild(messageEl);
    scrollToBottom();
    return messageEl;
}

function scrollToBottom() {
    const container = document.querySelector('#gpt-output');
    container.scrollTop = container.scrollHeight;
}

function getChatHistory() {
    const messages = document.querySelectorAll('#gpt-output .message');
    return Array.from(messages).map(msg => msg.innerText.trim());
}

async function fetchPromptResponse(prompt) {
    const response = await fetch("/prompt", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ messages: getChatHistory() }),
    });

    const contentType = response.headers.get("content-type");
    if (contentType && contentType.includes("application/json")) {
        const errorData = await response.json();
        throw new Error(errorData.error || "Une erreur est survenue");
    }

    return response.body.getReader();
}

async function readResponseChunks(reader, block) {
    const decoder = new TextDecoder();
    const converter = new showdown.Converter();

    let chunks = "";
    while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        chunks += decoder.decode(value);
        block.innerHTML = converter.makeHtml(chunks);
        scrollToBottom();
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector('#prompt-form');
    const spinnerIcon = document.querySelector('#spinner-icon');
    const sendIcon = document.querySelector('#send-icon');

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const prompt = form.elements.prompt.value.trim();
        if (!prompt) return;

        form.elements.prompt.value = "";

        spinnerIcon.classList.remove("hidden");
        sendIcon.classList.add("hidden");

        addToLog(prompt, "user");

        try {
            const answerBlock = addToLog("GPT est en train de réfléchir...", "bot");
            const reader = await fetchPromptResponse(prompt);
            await readResponseChunks(reader, answerBlock);
        } catch (error) {
            const errorMessage = error.message || "Erreur inconnue";
            const errorBlock = addToLog(errorMessage, "bot");
            errorBlock.classList.add("text-red-600", "font-semibold");
        } finally {
            spinnerIcon.classList.add("hidden");
            sendIcon.classList.remove("hidden");
            hljs.highlightAll();
        }
    });
});
