# Phidata LLM Chat App

A simple LLM chat app built with [Agno (Phidata)](https://github.com/agno-agi/agno), Groq, and Streamlit.

## Setup

### 1. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies
```bash
venv\Scripts\pip.exe install agno groq streamlit python-dotenv
```

### 3. Configure API Key
Add your Groq API key to `.env`:
```
GROQ_API_KEY="your_groq_api_key_here"
```
Get your key from: https://console.groq.com/keys

## Run

### Terminal app
```bash
venv\Scripts\python.exe app.py
```

### Streamlit app
```bash
venv\Scripts\streamlit.exe run app.py
```

## Tools Available

| Tool | Description | Example Query |
|------|-------------|---------------|
| `get_current_time` | Returns current date and time | "What time is it?" |
| `tell_a_joke` | Returns a random joke | "Tell me a joke" |
| `calculate` | Evaluates math expressions | "What is 25 * 4?" |
| `get_weather` | Mock weather report | "Weather in London?" |

## Project Structure

```
phidata/
├── agent.py        # Agno agent with tools and memory
├── app.py          # Streamlit chat UI
├── .env            # API keys
└── README.md       # This file
```

## Features
- Groq LLM (llama-3.3-70b-versatile)
- Custom tools (time, joke, calculator, weather)
- Conversation memory
- Streamlit chat UI
