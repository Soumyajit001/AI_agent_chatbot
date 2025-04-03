import os
from langchain.agents import create_react_agent
from langchain.schema import AIMessage
from typing import List, Union
# load env
from dotenv import load_dotenv
load_dotenv()

# API setup for Groq, Tavily and OpenAI
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

# llm setup
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")
openai_llm = ChatOpenAI(model="gpt-4o-mini")

# 
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

system_prompt = "Act as an AI chatbot who is smart and friendly"


# tools = [TavilySearchResults(max_results=2)]
# agent = create_react_agent(
#         model = groq_llm,
#         tools = tools,
#         state_modifier = system_prompt
#     )

# query = "Tell me about paracetamol-650"
# state = {"messages": [query]}
# response = agent.invoke(state)
# print(response)

# def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
#     if provider=="Groq":
#       llm = ChatGroq(model=llm_id)

#     elif provider=="OpenAI":
#        llm= ChatOpenAI(model=llm_id)

#     tools = [TavilySearchResults(max_results=2)] if allow_search else []

#     agent = create_react_agent(
#         model = llm,
#         tools = tools,
#         state_modifier = system_prompt
#     )

#     state = {"messages": query}
#     response = agent.invoke(state)
#     messages = response.get("messages")
#     ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
#     return ai_messages[-1]


def get_response_from_ai_agent(llm_id: str, query: Union[str, List[str]], allow_search: bool, system_prompt: str, provider: str):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)

    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)
    
    else:
        raise ValueError("Invalid provider. Must be 'Groq' or 'OpenAI'.")

    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    agent = create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )

    # Prepare the messages in the correct format
    if isinstance(query, str):
        messages = [{"role": "user", "content": query}]
    elif isinstance(query, list):
        messages = [{"role": "user", "content": message} for message in query]
    else:
        raise ValueError("Query must be a string or a list of strings.")
    
    # Invoke the agent
    state = {"messages": messages}
    response = agent.invoke(state)
    
    # Extract AI messages from the response
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    
    if not ai_messages:
        return "No valid response received from the AI agent."
    
    return ai_messages[-1]