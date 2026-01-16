# LLM-Benchmarking

A small Streamlit app to benchmark and compare LLM responses and throughput (tokens/sec) side-by-side. The app calls Google Gemini and Groq Llama models and displays latency, token usage, and a simple bar chart. (will add more models in the future)

## Features

- Compare multiple models side-by-side in the browser.
- Measure latency, tokens and compute throughput (tokens/sec).
- Simple fallback and error messages when APIs are unavailable.

## Prerequisites

- Python 3.11+ (the included virtualenv in `benchmark/` targets Python 3.13)
- `pip` available to install dependencies
- Streamlit installed in the environment used to run the app

## Setup (recommended quick start)

1. Create or activate a Python virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install runtime dependencies. If a `requirements.txt` is not present, install at least:

```bash
pip install streamlit google-genai groq-client plotly pandas
```

3. Provide API keys. The app reads keys from Streamlit secrets or environment variables. Create a file at `.streamlit/secrets.toml` with the following TOML content (no extra characters):

```toml
GEMINI_API_KEY = "sk_your_gemini_key_here"
GROQ_API_KEY = "gr_your_groq_key_here"
```

Or set environment variables instead (useful for local testing or CI):

```bash
export GEMINI_API_KEY="sk_..."
export GROQ_API_KEY="gr_..."
```

Note: Streamlit will parse `.streamlit/secrets.toml` using TOML—ensure the file is valid TOML (no stray BOM or invalid characters).

## Running the app

From the repository root run:

```bash
streamlit run home.py
```

Open the URL printed by Streamlit (usually http://localhost:8501).

## Troubleshooting

- Error "'Secrets' object is not callable": use `st.secrets["KEY"]` or `st.secrets.get("KEY")` rather than calling `st.secrets(...)`. The app in this repo has been updated to read secrets safely.
- Error parsing `.streamlit/secrets.toml`: ensure the file is valid TOML. Example TOML is shown above.
- API 503 / model overloaded: the model may be temporarily unavailable. Retry later or add retries/exponential backoff. The app shows warnings/errors on request failures.
- Missing API keys: the app will show an error in the UI if keys are not found in either `st.secrets` or environment variables.



