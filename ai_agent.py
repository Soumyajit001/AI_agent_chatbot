import os

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

groq_llm = ChatGroq(model="llama-3.3-70b-versatile")
openai_llm = ChatOpenAI(model="gpt-4o-mini")

search_tool = TavilySearchResults(max_results=2)

from langgraph.prebuilt import create_react_agent

system_prompt = "Act as an AI chatbot who is smart and friendly"

agent = create_react_agent(
    model = groq_llm,
    tools = [search_tool],
    state_modifier = system_prompt
)

query = "Tell me about the trends in crypto markets"
state = {"messagess": query}
response = agent.invoke(state)

print(response)