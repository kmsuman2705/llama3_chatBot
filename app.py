import os
import requests
from flask_cors import CORS

from flask import Flask, request, jsonify, render_template
from bs4 import BeautifulSoup
from langchain_community.llms import Ollama
from langchain.schema import LLMResult

# Initialize Flask app
app = Flask(__name__)
CORS(app)


# Set up Ollama model
model = Ollama(base_url="http://localhost:11434/", model="llama3.2")

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()
    except requests.RequestException as e:
        return f"An error occurred while scraping the website: {str(e)}"

# Scrape website content
website_content = scrape_website('http://192.168.29.229/')



def ask_gpt(question, context):
    try:
        # Create a concise prompt for quick response
        prompt = f"{context}\n\nQ: {question}\nA (briefly):"
        
        # Use Ollama model to generate a response
        result = model.generate(prompts=[prompt])
        
        # Extract the response text from the result object
        if isinstance(result, LLMResult):
            response_text = result.generations[0][0].text.strip()
            return response_text
        else:
            return "No response generated."
    except Exception as e:
        return f"An error occurred while processing your request: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')

    if user_message.lower() == "hello":
        answer = "How can I assist you today?"
    elif user_message.lower() == "clear chat":
        answer = "Chat history is not maintained in this implementation."
    else:
        context = website_content
        answer = ask_gpt(user_message, context)

    return jsonify({"response": answer})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
