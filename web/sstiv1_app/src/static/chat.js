const form = document.getElementById("chat-form");
const chatBox = document.getElementById("chat-box");

form.onsubmit = async (event) => {
    event.preventDefault();
    const userInput = document.getElementById("user-input").value;

    const userMessage = document.createElement("div");
    userMessage.className = "message user-message";
    userMessage.textContent = `You: ${userInput}`;
    userMessage.style.color = "red"; 
    chatBox.appendChild(userMessage);

    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: `user_input=${encodeURIComponent(userInput)}`
    });
    const data = await response.json();

    const botMessage = document.createElement("div");
    botMessage.className = "message bot-message";
    botMessage.innerHTML = data.response; 
    chatBox.appendChild(botMessage);

    chatBox.scrollTop = chatBox.scrollHeight;
    form.reset();
};