import streamlit as st
from openai import OpenAI
import os

class UseOpenAi:
    def __init__(self, model):
        self.model = model
        self.client = None
        self.api_key = None

    def validate_and_connect(self, api_key):
        try:
            if not api_key:
                raise ValueError("API key is not provided")
            self.api_key = api_key
            self.client = OpenAI(api_key=self.api_key)
            # Test the connection by listing models
            self.client.models.list()
            return True, "API key validated successfully!"
        except Exception as e:
            self.client = None
            return False, f"OpenAI Connection Error: {e}"

    def get_response(self, messages):
        if not self.client:
            return "Connection failed. Please check your API key."
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error while fetching response: {e}"

class PromptGenerator:
    def __init__(self, system_prompt, user_prompt, chat_history):
        self.system_prompt = system_prompt
        self.user_prompt = user_prompt
        self.chat_history = chat_history

    def generate_prompt(self):
        # Combine system prompt, chat history, and new user input
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(self.chat_history)  # Add previous messages
        messages.append({"role": "user", "content": self.user_prompt})
        return messages

# Initialize session state
if 'api_key_validated' not in st.session_state:
    st.session_state.api_key_validated = False

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []  # Stores conversation history

# Streamlit App UI
st.title("🤖 Coding Assistant")
st.sidebar.title("⚙️ Configuration")

# API Key input and validation
api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")
if st.sidebar.button("Validate API Key"):
    client = UseOpenAi("gpt-3.5-turbo")  # Using a known model for validation
    is_valid, message = client.validate_and_connect(api_key)
    st.session_state.api_key_validated = is_valid
    if is_valid:
        st.sidebar.success(message)
    else:
        st.sidebar.error(message)

# Only show the rest of the UI if API key is validated
if st.session_state.api_key_validated:
    # Model selection dropdown with correct model names
    model_choice = st.sidebar.selectbox(
        "Select AI Model",
        ("gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo", "gpt-4", "gpt-4-turbo-preview")
    )

    # Programming language selection
    programming_language = st.sidebar.selectbox(
        "Select Programming Language",
        ["python", "javascript", "VBS", "ABAP"]
    )

    # Dynamic system prompt based on language selection
    system_prompt = (
        f"You are an expert {programming_language.upper()} programmer assisting with code development. "
        f"All responses must be valid {programming_language} code snippets. "
        f"Identify and correct any syntax errors or logical issues in the code provided. "
        f"Explain any changes or improvements using comments in proper {programming_language.upper()} style. "
        f"Exclude explanations outside of code comments."
    )

    # User input chat window
    user_prompt = st.text_area(
        "💬 Your Message:",
        "",
        height=300
    )

    # Response button
    if st.button("🚀 Get Response"):
        messages = PromptGenerator(system_prompt, user_prompt, st.session_state.chat_history)
        client = UseOpenAi(model_choice)
        client.validate_and_connect(api_key)  # Reconnect with validated API key
        response = client.get_response(messages.generate_prompt())

        # Update chat history
        st.session_state.chat_history.append({"role": "user", "content": user_prompt})
        st.session_state.chat_history.append({"role": "assistant", "content": response})

        # Display response
        st.subheader("💡 AI Response")
        st.code(response, language=programming_language)

    # Clear chat memory button
    if st.sidebar.button("🗑️ Clear Chat Memory"):
        st.session_state.chat_history = []
        st.sidebar.success("Chat memory cleared!")

else:
    st.warning("Please enter and validate your API key to use the application.")

# Add footer styling
st.markdown(
    "<hr><center>Made with by Yirong Mo</center>",
    unsafe_allow_html=True
)
