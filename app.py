  # Assuming your chatbot code is in chatbot_api.py
from flask import Flask, render_template, request, jsonify
import chatbot_api


@app.route('/')
@app.route('/index')
def home():
    return render_template('chat.html')

@app.route('/chatbot', methods=['POST'])
def chatbot_endpoint():
    data = request.get_json()  # Parse the JSON payload

    if data and 'message' in data:
        user_message = data['message']
        chatbot_response = chatbot_api.get_chatbot_response(user_message)
        return jsonify({"response": chatbot_response})

    return jsonify({"error": "Invalid request format"}), 400


