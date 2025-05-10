"""
/*!
 * @file        app.py
 * @brief       Flask web server for translating text into Persian
 * @author      Rahim Jamali <rahim.jamali@gmail.com>
 * @copyright   © 2025 Rahim Jamali
 * @license     as-is License
 * @date        2025-04-05
 * @version     1.0.0
 */

Flask Web Application for Text Translation to Persian using DeepSeek API.

This application provides a simple web interface where users can input text in any language,
and the server translates it into Persian using the DeepSeek Chat API via OpenRouter.

Requirements:
    - Flask
    - requests
    - python-dotenv (optional, for environment variable management)

Environment Variables:
    - DEEPSEEK_API_KEY: API key for accessing the DeepSeek model through OpenRouter.

Routes:
    - / (GET, POST): Main page that displays a form for input and shows translated text.

Functions:
    - process_translation(user_input): Sends translation request to the API and returns the result.
"""

from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# API Configuration
# You must take API Key and export it by below terminal command:
# export DEEPSEEK_API_KEY="sk..."
API_KEY = os.getenv("DEEPSEEK_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"


def process_translation(user_input):
    """Handle translation process with API call.

    Translates the provided English or multilingual text into Persian using DeepSeek API.

    Args:
        user_input (str): The text input provided by the user for translation.

    Returns:
        str: Translated text in Persian, or an error message if translation fails.
    """
    if not user_input:
        return "لطفاً متنی برای ترجمه وارد کنید."

    data = {
        "model": "deepseek/deepseek-chat:free",
        "messages": [
            {
                "role": "user",
                "content": f"Translate the following text into Persian:\n{user_input}",
            }
        ],
    }

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    try:
        response = requests.post(API_URL, json=data, headers=headers)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"خطا: ترجمه با مشکل مواجه شد. کد خطا: {response.status_code}"

    except Exception as e:
        return f"خطایی رخ داده است: {str(e)}"


@app.route("/", methods=["GET", "POST"])
def index():
    """Main route for rendering the translation form and handling submitted input.

    GET Request:
        Displays the translation form with empty fields.

    POST Request:
        Receives user input, calls the translation function, and displays the result.

    Template:
        templates/index.html

    Context Variables Passed to Template:
        - input_text (str): Original text entered by the user.
        - output_text (str): Translated text returned from the API.
    """
    output_text = ""
    input_text = ""
    if request.method == "POST":
        input_text = request.form.get("input_text", "")
        output_text = process_translation(input_text)

    return render_template("index.html", input_text=input_text, output_text=output_text)


if __name__ == "__main__":
    app.run(debug=True)
