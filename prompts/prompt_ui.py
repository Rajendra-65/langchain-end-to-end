from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOpenAI(model = 'gpt-3.5',temperature = 1.5 , max_completion_tokens = 200)

st.header('Research Tool')

user_input = st.text_input(
    'Enter your prompt'
)

if st.button('Summerize'):
    result = model.invoke(user_input)
    st.write(result.content)