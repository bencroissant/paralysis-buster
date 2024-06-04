from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# Set the OpenAI API key from the environment variable
openai.api_key = 'OPENAI_API_KEY'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    user_input = request.json['message']
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Help organize tasks from disorganized thoughts."},
            {"role": "user", "content": user_input}
        ]
    )
    # Extract the text part of the response to send back to the client
    response_text = completion.choices[0].message['content']  # Corrected to navigate through the actual response structure
    return jsonify(reply=response_text)

if __name__ == '__main__':
    app.run(debug=True)