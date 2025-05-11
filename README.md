# Online Persian Text Translator

This is a simple Flask web application that translates text from any language into Persian using the DeepSeek Chat API via OpenRouter.

## Overview

The application provides a user-friendly web interface where users can input text, and the server processes the request using the DeepSeek API to provide the Persian translation. The frontend is a single HTML page styled for readability and right-to-left (RTL) text direction appropriate for Persian.

## Features

* Translate text from multiple languages to Persian.
* Simple and clean web interface.
* Uses the DeepSeek Chat model through the OpenRouter API.
* Responsive design.
* Handles API errors gracefully.

## Requirements

* Python 3.12+
* Flask = 3.0.0
* Requests library = 2.31.0
* python-dotenv (optional, but recommended for managing environment variables)

## Installation

1.  **Clone the repository (or download the files):**
    ```bash
    # If using git
    git clone <repository_url>
    cd <repository_directory>
    # If downloading, just navigate to the directory containing app.py and index.html
    ```

2.  **Install the required Python packages:**
    ```bash
    pip install Flask requests python-dotenv
    ```

3.  **Obtain an API Key:**
    You need an API key from OpenRouter to access the DeepSeek model. Sign up on the OpenRouter website and get your API key.

4.  **Set up Environment Variables:**
    You need to set the `DEEPSEEK_API_KEY` environment variable with your API key.
    * **Using a `.env` file (recommended):**
        Create a file named `.env` in the same directory as `app.py` and add the following line:
        ```dotenv
        DEEPSEEK_API_KEY="sk-YOUR_OPENROUTER_API_KEY"
        ```
        Replace `"sk-YOUR_OPENROUTER_API_KEY"` with your actual API key. The `python-dotenv` library will automatically load this variable when the app runs.
    * **Exporting in the terminal:**
        Alternatively, you can export the variable in your terminal before running the app:
        ```bash
        export DEEPSEEK_API_KEY="sk-YOUR_OPENROUTER_API_KEY"
        ```
        *(Note: This is temporary and only lasts for the current terminal session)*

## Usage

1.  **Run the Flask application:**
    ```bash
    python app.py
    ```

2.  **Access the web interface:**
    Open your web browser and go to `http://127.0.0.1:5000/`.

3.  **Translate text:**
    Enter the text you want to translate into the input box and click the "ترجمه کن" (Translate) button. The Persian translation will appear below.

## File Structure
```bash
Translate_deepseekAPI/
│
├── app.py                  # Main Flask application
├── templates/
│   └── index.html          # HTML template for translation interface
├── README.md               # This file
└── requirements.txt        # Python dependencies
```


* `app.py`: Contains the Flask application logic, including the route handler and the translation function that interacts with the OpenRouter API.
* `index.html`: The HTML template for the web interface, including the form for input and the display area for the output.
* `.env`: (Optional) File to store the `DEEPSEEK_API_KEY` environment variable.

## Code Details

### `app.py`

* Initializes a Flask application.
* Reads the `DEEPSEEK_API_KEY` from environment variables.
* Defines `API_URL` for the OpenRouter API endpoint.
* The `process_translation` function takes user input, constructs the API request payload, sends it to the OpenRouter API using the `requests` library, and returns the translated text or an error message.
* The `index` route (`/`) handles both GET and POST requests.
    * GET: Renders the `index.html` template.
    * POST: Retrieves the input text from the form, calls `process_translation`, and renders `index.html` again with the original input and the translated output.
* Runs the Flask development server when the script is executed directly.

### `index.html`

* A simple HTML5 document with a Persian language setting (`lang="fa"`) and Right-to-Left direction (`dir="rtl"`).
* Includes basic CSS for styling the layout, form elements, and the result box.
* Uses a `textarea` for user input and a `button` to submit the form via a POST request to the `/` route.
* Uses Jinja2 templating syntax (`{{ input_text }}` and `{{ output_text }}`) to pre-fill the input field after submission and conditionally display the translation result.

## Author and License

* **Author:** Rahim Jamali <rahim.jamali@gmail.com>
* **Copyright:** © 2025 Rahim Jamali
* **License:** as-is License (Based on the comment in the source files, implying minimal restrictions or provided as is without warranty).
