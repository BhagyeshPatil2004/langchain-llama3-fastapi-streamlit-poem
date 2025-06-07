# LangChain + FastAPI + Streamlit + Ollama + LLaMA 3 🦙

This is a lightweight AI-powered poem generator built using [LangChain](https://github.com/langchain-ai/langchain), [FastAPI](https://fastapi.tiangolo.com/), [Streamlit](https://streamlit.io/), and [Ollama](https://github.com/ollama/ollama). It uses the locally running **LLaMA 3** model served via Ollama to generate 100-word poems based on a user-provided topic.

---

## 🔧 Features

- Local LLM inference using **Ollama** (\`llama3\` model)
- Prompt templating and chaining using **LangChain**
- REST API built with **FastAPI**
- Interactive frontend using **Streamlit**
- Completely offline — no OpenAI API required

---

## 🚀 How to Run

### 1. Prerequisites
- Python 3.10+
- [Ollama installed](https://ollama.com/)
- Pull the LLaMA 3 model:

\`\`\`bash
ollama pull llama3
\`\`\`

### 2. Setup

\`\`\`bash
git clone https://github.com/BhagyeshPatil2004/langchain-fastapi-ollama.git
cd langchain-fastapi-ollama
python -m venv .venv
source .venv/bin/activate  # or .venv\\Scripts\\activate on Windows
pip install -r requirements.txt
\`\`\`

### 3. Run FastAPI backend

\`\`\`bash
uvicorn main:app --reload
\`\`\`

### 4. Run Streamlit frontend

\`\`\`bash
streamlit run client.py
\`\`\`

Then open your browser at [http://localhost:8501](http://localhost:8501)

---

## 📁 Project Structure

\`\`\`

├── main.py          # FastAPI + LangChain + Ollama backend

├── client.py        # Streamlit frontend

├── requirements.txt # Python dependencies

└── README.md        # Project documentation

\`\`\`

---

## 📌 Notes
- The \`/test\` API endpoint takes input as JSON: \`{"topic": "your subject here"}\`
- Ensure the \`llama3\` model is running via Ollama **before** using the app
- Everything runs 100% locally

---

## 🧑‍💻 Author
[Bhagyesh Patil](https://github.com/BhagyeshPatil2004)

---
