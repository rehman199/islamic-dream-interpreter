from dotenv import load_dotenv
import streamlit as st
from dream_interpreter import DreamInterpreter
import time

load_dotenv()

di = DreamInterpreter()


def stream_response_generator(prompt):
    for word in di.generate_answer(prompt).split():
        yield word + " "
        time.sleep(0.05)


def response_generator(prompt):
    return di.generate_answer(prompt)


st.set_page_config(
    page_title="Islamic Dream Interpretation",
    page_icon="🌙",
)

st.title("Islamic Dream Interpreter")

st.caption('Welcome to our Islamic Dream Interpretation app! This application draws from the respected work of Imam Ibn Sirin’s Dictionary of Dreams, providing you with insights into dream meanings based on traditional Islamic perspectives. Simply describe your dream, and our tool will retrieve relevant interpretations, helping you explore the possible symbolism and spiritual meanings in light of Islamic teachings.')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter your dream"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant",):
        with st.spinner('Generating interpretation.....'):
            response = response_generator(prompt)
        # response = st.write_stream(stream_response_generator(prompt))
        st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response})
