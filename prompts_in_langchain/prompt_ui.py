from langchain_core.prompts import PromptTemplate, load_prompt
from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

model = ChatOpenAI(
    model="llama3-8b-8192",  # or llama3-70b-8192
    openai_api_key=api_key,
    openai_api_base="https://api.groq.com/openai/v1",
)


st.header("Reasearch Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis",
    ],
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"],
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)",
    ],
)

template= load_prompt('template.json')

if st.button('Summarize'):
    chain= template | model
    response= chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })

    st.write(response.content)