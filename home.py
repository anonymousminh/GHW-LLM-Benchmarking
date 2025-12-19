import streamlit as st
from google import genai
import time
import os
import pandas as pd
import plotly.express as px
from groq import Groq

# Set the page config
st.set_page_config(page_title="LLM Benchmarking", layout="centered")
st.title("LLM Benchmarking")
st.subheader("Compare LLMs side by side")
st.divider()

# API Key for the LLMs
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
GROQ_API_KEY=os.getenv("GROQ_API_KEY")

gemini_client = genai.Client(GOOGLE_API_KEY)
groq_client = Groq(GROQ_API_KEY)

def call_gemini(prompt):
    start = time.time()
    response = gemini_client.models.generate_content(model='gemini-3-flash', 
                                                     contents=prompt)
    
    end = time.time()
    if response.usage_metadata:
        token_count = response.usage_metadata.total_token_count
    else:
        token_count = len(response.text) // 4

    return response.text, end - start, token_count





