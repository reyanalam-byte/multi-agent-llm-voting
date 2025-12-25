from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import difflib
import httpx
import asyncio

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Multi-Agent Backend Running"}

# Ollama config
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "phi3"

AGENTS = {
    "analyst": "Answer accurately and analytically.",
    "explainer": "Explain in simple language.",
    "critic": "Answer cautiously and check for errors."
}

class Query(BaseModel):
    question: str

# Call Ollama asynchronously
async def call_ollama_async(prompt, system):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "system": system,
        "stream": False
    }
    async with httpx.AsyncClient(timeout=300) as client:
        response = await client.post(OLLAMA_URL, json=payload)
        return response.json()["response"]

# Similarity
def similarity(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()

# Voting
def vote(answers):
    scores = {k: 0 for k in answers}
    for a1, ans1 in answers.items():
        for a2, ans2 in answers.items():
            if a1 != a2:
                scores[a1] += similarity(ans1, ans2)
    return scores

@app.post("/ask")
async def ask(query: Query):
    # 🔥 Parallel calls
    tasks = [call_ollama_async(query.question, system) for system in AGENTS.values()]
    results = await asyncio.gather(*tasks)

    answers = dict(zip(AGENTS.keys(), results))
    scores = vote(answers)
    winner = max(scores, key=scores.get)

    # Mark the most preferred answer
    marked_answers = {}
    for agent, ans in answers.items():
        marked_answers[agent] = {
            "answer": ans,
            "most_preferred": agent == winner
        }

    return {
        "winner": winner,
        "answers": marked_answers,
        "scores": scores
    }
