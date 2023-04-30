import streamlit as st
from PIL import Image


def app():
    st.markdown("""

    # Emotion Detection for given text
    
    Natural language processing is the use of computers for processing natural language text or speech.  
    

    


    """)

    # image = Image.open('images/speech-text.png')
    image = Image.open('images/nlp1.png')
    st.image(image)

    st.markdown("""
    Natural language interfaces permit computers to interact with humans using natural language, for example, to query databases. 
    Coupled with speech recognition and speech synthesis, these capabilities will become more 
    important with the growing popularity of portable computers that lack keyboards and large display screens.
    """)
