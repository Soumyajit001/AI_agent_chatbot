from pydantic import BaseModel
from typing import List

# Define a Pydantic model for request data validation
class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES = ["llama3-70b-8192", "llama-3.3-70b-versatile", "gpt-4o"]

app = FastAPI(title="AI Agent Chatbot")

@app.post("/chat")
def chat_endpoint(request: RequestState):   # Whatever data came within request, it should be the type give in class RequestState
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request.
    """

    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model"}
    
    # create ai_agent and get response from it.
    llm_id = request.model_name
    query = request.messages
    # query = {"messages": request.messages}
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    # Create AI Agent and get response from it!
    response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)
