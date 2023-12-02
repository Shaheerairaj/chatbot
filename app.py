from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_message = request.form['user_message']
    bot_response = "I'm a simple echo bot. Type something else!"
    
    # Display user and bot messages in the chat container
    chat_messages = [
        {"sender": "You", "message": user_message},
        {"sender": "Chatbot", "message": bot_response}
    ]

    return render_template('index.html', chat_messages=chat_messages)

if __name__ == '__main__':
    app.run(debug=True)
