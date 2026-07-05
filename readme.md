# 🤖 IntelliDesk AI (Phase 1)

An AI assistant built with LangChain that demonstrates the fundamentals of Agentic AI including tool calling, prompt engineering, and modular architecture.

> This project is a learning project and serves as the foundation for more advanced Agentic AI concepts such as LangGraph, RAG, Guardrails, Memory, and Multi-Agent Systems.

---

## ✨ Features

- 🔢 Calculator Tool
- 🌦️ Weather Tool (OpenWeather API)
- 🕒 Current Time Tool
- 📚 FAQ Tool
- 📦 Order Lookup Tool
- 🧠 LLM-powered tool selection
- Modular project architecture
- Easy to extend with new tools

---

## 🏗️ Project Structure

```
IntelliDesk-AI/
│
├── agent/
│   └── agent.py
│
├── prompts/
│   └── system_prompt.py
│
├── tools/
│   ├── calculator.py
│   ├── weather.py
│   ├── time.py
│   ├── faq.py
│   ├── order.py
│   └── __init__.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🛠 Technologies Used

- Python
- LangChain
- Google Gemini 2.5 Flash
- OpenWeather API
- dotenv
- Requests

---

## Implemented Tools

### Calculator

Performs mathematical calculations.

Example:

```
What is 52 * 37?
```

---

### Weather

Fetches live weather information.

Example:

```
Weather in Delhi
```

Returns:

- Temperature
- Weather Condition
- Humidity

---

### Current Time

Returns the current local time.

Example:

```
What time is it?
```

---

### FAQ

Answers predefined business questions.

Example:

```
What are your working hours?
```

---

### Order Lookup

Looks up order status using an order ID.

Example:

```
Track order 1001
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env`

```
GOOGLE_API_KEY=YOUR_API_KEY
OPENWEATHER_API_KEY=YOUR_API_KEY
```

Run

```bash
python main.py
```

---

## Sample Conversation

```
You: Weather in Delhi

AI:
Temperature: 39°C
Condition: Overcast Clouds
Humidity: 33%
```

```
You: What is 50 * 80?

AI:
4000
```

```
You: Track order 1001

AI:
Status: Shipped
Expected Delivery: 2026-07-07
```

---

## Learning Outcomes

This project demonstrates:

- LangChain Agents
- Tool Calling
- Prompt Engineering
- Modular Python Project Structure
- External API Integration
- Custom Tool Development
- Agent Execution Flow

---

## Future Improvements

- Conversation Memory
- LangGraph
- RAG
- PostgreSQL Database
- Authentication
- Human-in-the-loop
- Guardrails
- LLM Evaluation
- Multi-Agent Workflow
- Web Interface
- Docker Deployment

---
