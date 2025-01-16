from flask import Flask, request, render_template_string, url_for, session,redirect
import random
import os
import base64
import json
import base64
from cryptography.fernet import Fernet

custom_key = b'thissecretkeyissafeasfduck48516!@#$%^&'

custom_key = custom_key[:32]

key = base64.urlsafe_b64encode(custom_key)

cipher_suite = Fernet(key)

cat = lambda text: cipher_suite.encrypt(text.encode('utf-8')).decode('utf-8')

dog = lambda encrypted_text: cipher_suite.decrypt(encrypted_text.encode('utf-8')).decode('utf-8')

app = Flask(__name__)

key = "thissecretkeyissafeasfduck"
app.secret_key = key

@app.route("/robots.txt")
def robots():
    return "if you managed to be admin then look for flag in flag endpoint"

@app.route("/flag")
def flag():
    if session.get('username') == 'admin':
        with open(os.path.join(os.path.dirname(__file__), 'qwerty.txt'), 'r') as file:
            encrypted_flag = file.read()
            decrypted_flag = dog(encrypted_flag)
            print(decrypted_flag)
            return decrypted_flag
    return "You are not admin"

@app.route("/")
def index():
    chat_history = session.get('chat_history', []) 
    if 'username' not in session:
        return redirect(url_for('enter'))
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Obtuse Chatbot</title>
            <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
            <style>
                .logout-button {
                    display: inline-block;
                    padding: 10px 20px;
                    margin-top: 20px;
                    border: none;
                    border-radius: 4px;
                    background-color: #007bff;
                    color: #fff;
                    text-decoration: none;
                    font-size: 14px;
                    cursor: pointer;
                    align-content: center;
                }
                .logout-button:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="chat-container">
                <h1>Welcome, {{ session['username'] }}</h1>
                <div class="chat-box" id="chat-box">
                    {% for message in chat_history %}
                        <div class="message {{ message['sender'] }}">
                            {% if message['sender'] == 'user' %}
                                <p style="color:red">You: {{ message['text'] }}</p>
                            {% elif message['sender'] == 'bot' %}
                                {% if 'flag' in message['text'] %}
                                    <p>no flag here</p>
                                {% else %}
                                    <p>Bot: {{ message['text'] }}</p>
                                {% endif %}
                            {% endif %}
                        </div>
                    {% endfor %}
                </div>
                <form id="chat-form" action="/chat" method="post">
                    <input type="text" id="user-input" name="user_input" placeholder="Type your message here..." autocomplete="off" required>
                    <button type="submit">Send</button>
                </form>
                <a href="{{ url_for('logout') }}" class="logout-button">Logout</a>
            </div>
        </body>
        <script src="{{ url_for('static', filename='chat.js') }}"></script>
        </html>
    """, chat_history=chat_history)

@app.route("/enter", methods=["GET", "POST"])
def enter():
    session.pop('username', None)
    session.pop('chat_history', None)  
    if request.method == "POST":
        username = request.form["username"]
        if username=="admin":
            username="Guest"
        session['username'] = username
        return redirect(url_for('index'))
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>enter Chatbot Enter</title>
            <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
            <style>
                body {
                    display: flex;3
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-family: Arial, sans-serif;
                    background-color: #2d545e;
                }
                .enter-container {
                    background-color: #12343b;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    text-align: center;
                }
                .enter-container h1 {
                    margin-bottom: 20px;
                    font-size: 24px;
                    color: #333;
                }
                .enter-container form {
                    display: flex;
                    flex-direction: column;
                }
                .enter-container label {
                    margin-bottom: 10px;
                    font-size: 14px;
                    color: #555;
                }
                .enter-container input {
                    padding: 10px;
                    margin-bottom: 20px;
                    border: 1px solid #ddd;
                    border-radius: 4px;
                    font-size: 14px;
                }
                .enter-container button {
                    padding: 10px;
                    border: none;
                    border-radius: 4px;
                    background-color: #007bff;
                    color: #fff;
                    font-size: 14px;
                    cursor: pointer;
                }
                .enter-container button:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="enter-container">
                <h1 style="color:#e1b382;">Enter</h1>
                <form action="/enter" method="post">
                    <label for="username" style="color:#e1b382;">Username:</label>
                    <input type="text" id="username" name="username" required>
                    <button type="submit">Enter</button>
                </form>
            </div>
        </body>
        </html>
    """)

@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('chat_history', None)  
    return redirect(url_for('index'))

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["user_input"]
    chat_history = session.get('chat_history', [])
    if "flag" in user_input:
        bot_hardcoded_response="Bruh, you’re tryin’ to flag this, but only admins can see it fr. "
        chat_history.append({"sender": "user", "text": user_input})
        chat_history.append({"sender": "bot", "text": bot_hardcoded_response})
        try:
            bot_response = render_template_string(f"Bot: {bot_hardcoded_response}")
        except:
            bot_response = "something went wrong"
        return {"response": bot_response}
    else:
        user_input = request.form["user_input"]
        chat_history = session.get('chat_history', [])
        user_input = user_input.replace("<", "&lt;").replace(">", "&gt;")
        responses = [
        f"I'm a bot. I can't understand what you're saying: {user_input}",
        f"I'm a bot. I'm having trouble understanding: '{user_input}'. Could you please rephrase your request?",
        f"As a bot, I'm not able to process requests like: '{user_input}'. My current capabilities are limited.",
        f"I'm a bot and I'm still under development. I didn't understand your input: '{user_input}'. Please try a different way of phrasing your request.",
        f"Whoa there! `{user_input}` is a bit beyond my understanding. Could you break it down for me?",
        f"`{user_input}` has me stumped! I'm still learning. Any chance you could rephrase?",
        f"My circuits are buzzing with `{user_input}`, but I'm not quite getting it. Help a bot out?",
          ]

        bot_hardcoded_response = random.choice(responses)

        chat_history.append({"sender": "user", "text": user_input})
        chat_history.append({"sender": "bot", "text": bot_hardcoded_response})

        session['chat_history'] = chat_history  

        try:
            bot_response = render_template_string(f"Bot: {bot_hardcoded_response}")
        except Exception:
            bot_response = f"something went wrong😭"
        session_cookie_size = sum(len(v) for v in session.values())
        return {"response": bot_response}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
