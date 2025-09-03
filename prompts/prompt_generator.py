from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(model = 'gpt-3.5',temperature = 1.5 , max_completion_tokens = 1000)

st.header('Research Tool')

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers", 
        "GPT-3: Language models are Few-Short Learners",
        "Diffusion models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Freindly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium(3-5 paragraphs)",
        "Long(detailed explanation)"
    ]
)

user_input = st.text_input(
    'Enter your prompt'
)

#template
template = PromptTemplate(
    template = """
        Please summarize papaer titled "{paper_input}" with the following spcifications:
        Explanation Style : {style_input}
        Explanation Length : {length_input}
        1. Mathematical Details:
            -Include relevant mathematical equations if present in the paper.
            -Explain the mathematical concepts using simple , intuitive code snippets where applicable.
        2. Analogies:
            = Use relatable analogies to simplify complex ideas.
        If certain information is not available in the paper, repond with: "Insufficient information 
        Ensure the summary is clear, accurate and alligned with the provided style and length.
""",
input_variables = ['paper_input', 'style_input', 'length_input'],
validate_template = True
)

template.save('template.json')