import os
from flask import Flask, request, jsonify
from flask_cors import CORS

# Import your chatbot function from chat.py
from chat import Chat

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Use your chatbot function here
    response_text, confidence = Chat(user_message)

    return jsonify({
        "response": response_text,
        "confidence": confidence
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
