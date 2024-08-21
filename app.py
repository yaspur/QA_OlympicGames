import os
import streamlit as st
from logic.olympic_games import OlympicGames

st.set_page_config('QA OlympicGames')
st.title("HACKATON Avvy + SupaBase")
st.header("¿Qué quieres saber sobre los Juegos Olímpicos?")
st.image('images\JO.png')


st.markdown("Esta aplicación te permite consultar información sobre los **Juegos Olímpicos**. "
            "Por favor sigue las instrucciones para continuar.")

#Input OpenAI API Key
def get_openai_api_key():
    input_text = st.text_input(
        label="OpenAI API Key ",  
        placeholder="Ex: sk-2twmA8tfCb8un4...", 
        key="openai_api_key_input", 
        type="password")
    return input_text

st.markdown("1. Ingresa una API KEY valida de OpenAI")

openai_api_key = get_openai_api_key()

if openai_api_key:
    
    os.environ["OPENAI_API_KEY"] = openai_api_key
    
    user_question = st.text_input("Haz una pregunta sobre los juegos olimpicos:")
    
    if user_question:
        
        result = OlympicGames.response_process(query=user_question)
        
        st.write(result)