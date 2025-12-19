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

gemini_client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def call_gemini(prompt):
    start = time.time()
    response = gemini_client.models.generate_content(model='gemini-2.5-flash', 
                                                     contents=prompt)
    
    end = time.time()
    if response.usage_metadata:
        token_count = response.usage_metadata.total_token_count
    else:
        token_count = len(response.text) // 4

    return response.text, end - start, token_count

def call_llama(prompt):
    start = time.time()
    groq_response = groq_client.chat.completions.create(model='llama-3.3-70b-versatile',
                                                        messages=[
                                                            {
                                                                "role": "user",
                                                                "content": prompt
                                                            }
                                                        ], temperature=0.5)
    
    end  = time.time()
    content = groq_response.choices[0].message
    token_count = groq_response.usage.total_tokens
    return content, end - start, token_count

with st.sidebar:
    st.title("Choose models")
    use_gemini = st.checkbox("Gemini 2.5 Flash", value=True)
    use_groq = st.checkbox("Llama 3.3 70B", value=True)

prompt = st.chat_input("Enter your prompt")

if prompt:
    comparisons = []
    if use_gemini:
        comparisons.append("Gemini 2.5 Flash")
    if use_groq:
        comparisons.append("Llama 3.3 70B")

    cols = st.columns(len(comparisons))
    results = []

    for i, comparison_name in enumerate(comparisons):
        with cols[i]:
            st.subheader(comparison_name)
            if comparison_name == "Gemini 2.5 Flash":
                content, latency, tokens = call_gemini(prompt)
            else:
                content, latency, tokens = call_llama(prompt)
        st.caption(f"Latency: {latency:.2f} seconds | Tokens: {tokens} tokens")
        st.write(content)

        if latency > 0:
            results.append({
                "Model": comparison_name,
                "Latency": latency,
                "Tokens": tokens,
                "Throughput (tokens/s)": tokens / latency 
            })
        if results:
            df = pd.DataFrame(results)
            st.subheader("Benchmark results")
            st.dataframe(df)

            fig = px.bar(df, x="Model", y="Throughput (tokens/s)", title="Benchmarking LLM")
            st.plotly_chart(fig, use_container_width=True)




