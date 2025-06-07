from fastapi import FastAPI
from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain_core.runnables import Runnable
from typing import Dict
import uvicorn

app = FastAPI()

# Initialize LLM
llm = OllamaLLM(model="llama3")

# Define prompt
prompt = PromptTemplate.from_template("Write me a poem about {topic} with 100 words")

# Create chain with type hint for OpenAPI
chain: Runnable[Dict, str] = prompt | llm

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

@app.post("/test")
def test_chain(input: Dict):
    # Ensure input is a dict with a 'topic' key
    topic = input.get("topic", "")
    result = chain.invoke({"topic": topic})
    return {"output": result}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
