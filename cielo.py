from google.cloud import dialogflow_v2beta1 as dialogflow
import streamlit as st
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'cielo.json'

project_id = "ariannecielo-lifx"
session_id = '1234567'
language_code = 'en'

session_client = dialogflow.SessionsClient()

def detect_intent_text(text):
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(request={'session':session, 'query_input': query_input})

    return response.query_result.fulfillment_text


st.title('CHATBOT')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    user_input = st.chat_message(message['role'])
    user_input.write(message['content'])

prompt = st.chat_input('You:')

if prompt and prompt != '':
    st.chat_message('user').write(prompt)
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    bot_response = detect_intent_text(prompt)
    st.chat_message('assistant').write(bot_response)