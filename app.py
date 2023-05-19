from flask import Flask, request, render_template
import os
import openai
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__)

_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key  = os.getenv('OPENAI_API_KEY')

# Initialize the conversation with a system message

with open('content.txt', 'r') as file:
    content = file.read()

messages = [
    {
        'role': 'system',
        'content': content    
    },
    {
        'role': 'assistant',
        'content': 'Ciao! Cosa vuoi ordinare?'
    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get')
def get_bot_response():
    userText = request.args.get('msg')
    messages.append({"role": "user", "content": userText})  # add the user's message to the conversation
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,  # pass the entire conversation to the model
        temperature=0, # this is the degree of randomness of the model's output
        max_tokens=300
    )
    messages.append({"role": "assistant", "content": response.choices[0].message["content"]})  # add the bot's response to the conversation
    return response.choices[0].message["content"]

if __name__ == "__main__":
    app.debug = True
    app.run()
