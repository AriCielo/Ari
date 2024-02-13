import streamlit as st

st.title('CHATBOT')

if "messages" not in st.session_state:
    st.session_state.messages = []

if "state" not in st.session_state:
    st.session_state.state = "init"

def get_response(prompt, state):
    responses = {
        "init": ("Hello! How can I assist you?", "user"),
        "greeted": ("How are you today?", "assistant"),
        "asked_identity": ("I am your assistant.", "assistant"),
        "asked_hi": ("Hello!", "assistant"),
    }
    if prompt in responses:
        return responses[prompt]
    elif state in responses:
        return responses[state]
    else:
        return ("I'm sorry, I didn't understand that.", "assistant")

prompt = st.chat_input("user")

for message in st.session_state.messages:
    user_input = st.chat_message(message['role'])
    user_input.write(message['content'])

if prompt and prompt != '':
    st.session_state.messages.append({'role': 'user', 'content': prompt})

response, new_state = get_response(prompt, st.session_state.state)

st.chat_message(new_state).write(response)

st.session_state.state = new_state
