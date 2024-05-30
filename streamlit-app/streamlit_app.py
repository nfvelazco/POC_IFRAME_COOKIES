import time
import streamlit as st
import requests


url = "http://127.0.0.1:8000/base"
headers = {"Content-Type": "application/json"}
session_id = "1"



def generate_response(id, message):

    data = {
        "id": session_id,
        "message": message
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            assistant_response = response.json()
        else:
            assistant_response = "Hubo un error al obtener respuesta del bot."
    except Exception as e:
        assistant_response = "Hubo un error al obtener respuesta del bot."
    return assistant_response

def run_app():
    name_cookie = "cookiedemo_guille"
    cookie = {
        "flag_novedad": True,
        "id_producto": 5
    }
    
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            assistant_response = generate_response(session_id, prompt)
            # Simulate stream of response with milliseconds delay
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

if __name__ == '__main__':
    
    st.title('Copilot de Compra')

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    run_app()