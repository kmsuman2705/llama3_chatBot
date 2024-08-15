import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
import openai
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS

# Set OpenAI API key
openai.api_key = os.getenv("API_KEY")

# Function to scrape the website content
def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        texts = soup.get_text()
        return texts
    except requests.exceptions.RequestException as e:
        return f"Error occurred while scraping the website: {str(e)}"

# Scrape content from the website
website_content = scrape_website('https://talentconnectt.netlify.app')

# Function to interact with GPT model
def ask_gpt(question, context):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Act as a chatbot for the following website content. Only provide information from the context provided:\n\n{context}"},
                {"role": "user", "content": question}
            ],
            max_tokens=150,
            temperature=0.7,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].message['content'].strip()
    except openai.error.RateLimitError:
        return "Sorry, I have exceeded my current quota. Please try again later."
    except openai.error.OpenAIError as e:
        return f"An error occurred: {str(e)}"

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Chatbot API route
@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({"response": "Please provide a valid message."}), 400

        if user_message.lower() == "hello":
            answer = "How can I assist you today?"
        elif user_message.lower() == "clear chat":
            answer = "Chat history is not maintained in this implementation."
        else:
            context = website_content
            answer = ask_gpt(user_message, context)

        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"response": f"Something went wrong: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
