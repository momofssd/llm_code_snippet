# 🤖 Coding Assistant

A Streamlit-based application that serves as an AI-powered coding assistant, helping developers with code generation, review, and improvements across multiple programming languages.

## Features

- 🔑 Secure API key validation for OpenAI integration
- 🔄 Support for multiple OpenAI models (GPT-3.5-turbo, GPT-4, etc.)
- 💻 Multi-language support (Python, JavaScript, VBS, ABAP)
- 💡 Intelligent code suggestions and improvements
- 🔍 Syntax error detection and correction
- 📝 In-code documentation through comments

## Requirements

- Python 3.6+
- streamlit>=1.28.0
- openai>=1.3.0

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Launch the application and enter your OpenAI API key in the sidebar
2. Click "Validate API Key" to verify your credentials
3. Select your preferred:
   - AI Model (e.g., GPT-3.5-turbo, GPT-4)
   - Programming Language (Python, JavaScript, VBS, or ABAP)
4. Enter your code or question in the text area
5. Click "Get Response" to receive AI-generated code with explanatory comments

## Note

- Ensure you have a valid OpenAI API key
- The application requires an active internet connection
- Responses are formatted as code with integrated comments for explanation

Made with ❤️ by Yirong Mo
