# LangGraph ReAct AI Agent

A simple AI agent built with **LangGraph**, **LangChain**, and **Google Gemini 2.5 Flash**. This project demonstrates the ReAct (Reason + Act) pattern, allowing the model to use custom tools such as a calculator and greeting function while maintaining a conversational interface.

## Features

- 🤖 Gemini 2.5 Flash integration
- 🔧 Custom tool calling with LangChain
- 🧠 ReAct agent powered by LangGraph
- 💬 Interactive command-line chatbot
- ⚡ Streaming responses

## Project Structure

```
.
├── main.py
├── .env
├── pyproject.toml
├── uv.lock
└── README.md
```

## Prerequisites

- Python 3.11+
- A Google Gemini API Key

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/langgraph-react-ai-agent.git
cd langgraph-react-ai-agent
```

### Install dependencies using uv

If you don't have `uv` installed:

```bash
pip install uv
```

Install the project dependencies:

```bash
uv sync
```

Or, if there is no `pyproject.toml` yet:

```bash
uv pip install langchain langgraph langchain-google-genai google-genai python-dotenv
```

## Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

You can obtain a Gemini API key from Google AI Studio.

## Run the Project

```bash
python main.py
```

or

```bash
uv run python main.py
```

## Example

```
You: Add 25 and 17

Assistant:
Sum of 25.0 and 17.0 is 42.0
```

## Technologies Used

- Python
- LangChain
- LangGraph
- Google Gemini 2.5 Flash
- python-dotenv

## Environment Variables

Before running the project, create a `.env` file in the project root and add **your own** Google Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

> **Note:** This repository does **not** include an API key. You must generate your own Gemini API key from Google AI Studio and add it to the `.env` file before running the project.

## License

This project is intended for learning and educational purposes.
