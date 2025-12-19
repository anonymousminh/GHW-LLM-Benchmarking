import streamlit as st
from google import genai
import time
import pandas as pd
import plotly.express as px
from groq import Groq

# Set the page config
st.set_page_config(page_title="LLM Benchmarking", layout="centered")
st.title("LLM Benchmarking")
st.subheader("Compare LLMs side by side")
st.divider()

# API Key for the LLMs
gemini_client = genai.Client(api_key="")
groq_client = Groq(api_key="")


