import streamlit as st

st.set_page_config(page_title = "LangGraph Agent UI", layout="centered")
st.title("AI Chatbot Agents")
st.write("Create and Interact with the AI Agents!")

system_prompt = st.text_area("Tell about your AI Agent: ", height=70, placeholder="Type your system prompt here...")

MODEL_NAME_GROQ = ["llama-3.3-70b-versatile", "llama3-70b-8192"]
MODEL_NAME_OPENAI = ["gpt-4o"]

provider = st.radio("Select Provider:", ("Groq", "OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model: ", MODEL_NAME_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select OpenAI Model: ", MODEL_NAME_OPENAI)

allow_web_search = st.checkbox("Allow Web Search")

user_query = st.text_area("Enter query: ", height=200, placeholder="Ask anything...")

API_URL = "http://127.0.0.1:9999/chat"

# if st.button("Ask Agent!"):
#     if user_query.strip():
#         payload = {
#             "model_name": selected_model,
#             "model_provider": provider,
#             "system_prompt": system_prompt,
#             "messages": [user_query],
#             "allow_search": allow_web_search
#         }

#         response = requests.post(API_URL, json=payload)
#         if response.status_code == 200:
#             response_data = response.json()

#             if "error" in response_data:
#                 st.error(response_data["error"])
#             else:
#                 st.subheader("Agent Response")
#                 agent_response = response_data.get("response", "No response field found in API data")
#                 st.markdown(f"**Final Response:** {response}")
#         else:
#             st.error(f"API request failed with status code: {response.status_code}")
#     else:
#         st.warning("Please enter a query before submitting.")


if st.button("Ask Agent!"):
    if user_query.strip():
        import requests
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            st.write(f"Raw response_data: {response_data}")
            st.write(f"Type of response_data: {type(response_data)}")

            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                # agent_response = response_data.get("response", "No response field found in API data")
                if isinstance(response_data, dict):  # Ensure it's a dictionary
                    agent_response = response_data.get("response", "No response field found in API data")
                else:
                    agent_response = response_data  # If string, return as-is
                st.markdown(f"**Final Response:** {agent_response}")
                # st.markdown(f"**Final Response:** {response}")
        else:
            st.error(f"API request failed with status code: {response.status_code}")
    else:
        st.warning("Please enter a query before submitting.")