# LangGraph AI Chatbot
A web-based AI agent chatbot application built with Streamlit, FastAPI, and LangGraph, leveraging Groq and OpenAI models for conversational responses. Supports optional web search via Tavily.

## Features
Dynamic Model Selection: Choose between Groq (e.g., llama-3.3-70b-versatile) and OpenAI (e.g., gpt-4o-mini) models.
Custom System Prompt: Define the AI’s behavior (e.g., "Act as a financial advisor").
Web Search: Enable Tavily search for real-time information.
User-Friendly UI: Built with Streamlit for an interactive experience.

## Prerequisites
Python 3.8+
Anaconda (optional, for environment management)

API Keys:

Groq API Key

OpenAI API Key

Tavily API Key (for web search)

## Installation
### 1. Clone the Repository:
```bash
git clone https://github.com/yourusername/langgraph-ai-chatbot.git
```

### 2. Create a Virtual Environment (optional with Anaconda):
```bash
conda create -n agent_chatbot python=3.9
conda activate agent_chatbot
```

### 3. Install Dependencies:
```bash
pip install -r requirements.txt
```

### 4. requirements.txt:
```bash
streamlit
fastapi
uvicorn
requests
python-dotenv
langchain-groq
langchain-openai
langchain-community
langgraph
```

### 4. Set Environment Variables:

Create a .env file in the project root:
```bash
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Running the Application
### 1. Start the FastAPI Backend:
```bash
uvicorn FastAPI:app --host 127.0.0.1 --port 9999
```

### 2. Launch the Streamlit Frontend (in a separate terminal):
```bash
streamlit run frontend.py
```

### 3. Access the App: 
Open your browser to http://localhost:8501.

## Usage
Configure the AI: Enter a system prompt (e.g., "Act as a financial advisor").
Select a Model: Choose a provider (Groq or OpenAI) and a model from the dropdown.
Enable Web Search: Check the box if you want the AI to search the web.
Ask a Question: Type your query (e.g., "Tell me about good stocks to invest in small cap in 2025") and click "Ask Agent!".
### Troubleshooting
Connection Error: Ensure the FastAPI server is running on http://127.0.0.1:9999.
Invalid Model Name: Verify the selected model is in ALLOWED_MODEL_NAMES (FastAPI.py) and supported by the provider.
API Key Issues: Check that .env is loaded correctly and keys are valid.
### Project Structure

├── ai_agent.py       # AI agent logic with LangGraph

├── FastAPI.py        # Backend API server

├── frontend.py       # Streamlit frontend

├── .env             # Environment variables

└── requirements.txt  # Dependencies

### Contributing
Feel free to submit issues or pull requests to improve the project!

## License
This project is licensed under the MIT License. See the  file for details.

## Acknowledgments
Built with Streamlit, FastAPI, and LangGraph, leveraging Groq and OpenAI models.

