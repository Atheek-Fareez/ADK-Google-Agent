🚀 Agentic AI Lead Research System (Google ADK)

An intelligent multi-agent AI system built using Google Agent Development Kit (ADK) and Gemini API to perform automated research and structured lead generation.

This project demonstrates how to build modular AI agents that collaborate to solve real-world research problems.

🧠 Project Overview

This system takes a natural language query such as:

"Find me 10 Sri Lankan IT companies that might hire AI interns in Colombo."

It then:

Extracts structured intent

Discovers relevant hiring patterns

Generates structured company leads

Outputs clean JSON and CSV results

🏗️ Architecture (Multi-Agent Design)

The system consists of three AI agents:

1️⃣ Intent Extractor Agent

Converts user query into structured JSON

Identifies:

Country

City

Role

Company type

Required count

2️⃣ Pattern Discovery Agent

Analyzes hiring signals

Identifies:

Common AI job titles

Skills keywords

Hiring indicators

Expansion signals

3️⃣ Lead Generation Agent

Uses structured intent + patterns

Generates:

Company name

Why it matches

Target roles

Contact suggestion

Confidence score

🛠️ Tech Stack

Python 3.11+

Google Agent Development Kit (ADK)

Gemini API (Google Generative AI)

Asyncio

Pydantic

JSON-based structured outputs

CSV export

📂 Project Structure
Google_ADK/
│
├── main.py
├── test_adk.py
├── requirements.txt
├── .env
│
├── sub_agents/
│   ├── intent_extractor/
│   │   └── agent.py
│   ├── pattern_discovery/
│   │   └── agent.py
│   └── lead_generation/
│       └── agent.py
│
└── tools/

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/agentic-ai-lead-research.git
cd agentic-ai-lead-research

2️⃣ Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Add API Key

Create a .env file:

GOOGLE_API_KEY=your_api_key_here

▶️ Run the System
python main.py


The system will:

Generate structured JSON output

Save results to leads.csv

📊 Example Output (JSON)
{
  "company_name": "Sysco Labs Sri Lanka",
  "why_match": "Strong focus on AI and data science...",
  "target_roles": ["AI/ML Intern", "Data Science Intern"],
  "confidence": 95
}

🎯 Key Concepts Demonstrated

Agentic AI design

Multi-agent collaboration

Structured LLM outputs

Asynchronous execution

JSON validation & parsing

AI-driven automation workflow

💡 Real-World Applications

AI-powered recruitment research

Market intelligence automation

Sales lead generation

Competitive company analysis

Hiring trend discovery

🚀 Future Improvements

Web search tool integration

Vector database for company knowledge

Memory-enabled sessions

Agent chaining with orchestration

Deployment as API service

👨‍💻 Author

Atheek Fareez
BSc (Hons) IT – Specializing in Artificial Intelligence
Focused on ML, LLM systems, RAG pipelines, and Agentic AI architectures.

🔥 Why This Project Is Valuable

This project demonstrates:

✔ Real-world AI system design
✔ Structured multi-agent architecture
✔ Practical LLM orchestration
✔ Industry-relevant AI automation

It shows ability beyond simple chatbot development — it demonstrates system-level AI engineering.
