**Healthcare Assistant Chat App**
================================

This is a Streamlit app that uses the OpenAI API to create a chat interface for a healthcare assistant. The app is designed to provide emotional support and stress analysis to users.

## Demo
![Untitled Project](https://github.com/mshojaei77/healthcare-assistant/assets/76538971/3c84a050-f604-4f67-b2a3-9c41118f44d0)


**Getting Started**

---------------

### Prerequisites

* An OpenAI API key
* Streamlit installed (`pip install streamlit`)

### Running the App

1. Clone this repository and navigate to the directory.
2. Run `streamlit run app.py` (assuming the file is named `app.py`).
3. Open a web browser and navigate to `http://localhost:8501`.
4. Enter your OpenAI API key in the sidebar.
5. Choose a chat model from the dropdown menu.
6. Start chatting with the healthcare assistant!

**Features**
------------

* Chat interface with a healthcare assistant persona
* Stress analysis feature that analyzes the conversation and provides actionable solutions to alleviate stress
* Support for multiple chat models (gpt-3.5-turbo, gpt-4, gpt-4-turbo-2024-04-09)

**Configuration**
---------------

The app can be configured using the following variables:

* `openai_api_key`: Your OpenAI API key
* `model`: The chat model to use (gpt-3.5-turbo, gpt-4, gpt-4-turbo-2024-04-09)
* `initial_prompt`: The initial prompt for the healthcare assistant (can be modified to change the tone and guidelines)

**Troubleshooting**
-----------------

If you encounter any issues, check the Streamlit console output for error messages. Make sure you have entered a valid OpenAI API key and chosen a supported chat model.
