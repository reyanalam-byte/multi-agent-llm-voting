# multi-agent-llm-voting
Multi-agent LLM system using consensus-based voting
# 🗳️ Multi-LLM Voting Web App

## 📌 One-Line Summary
A web application that collects responses from multiple LLMs and identifies the most preferred answer using a voting mechanism.

---

## 📖 Problem Statement
Single-model approaches can be biased or inconsistent. Aggregating outputs from multiple models improves reliability and accuracy.

---

## 🎯 Objective
Create a system that queries multiple LLMs simultaneously, displays responses independently, and highlights the most preferred answer based on voting.

---

## 🧩 High-Level Idea
The system sends a user query to multiple language models. Each model generates its response independently. A voting mechanism selects the best answer and presents it clearly to the user.

---

## ⚙️ How the System Works
1. User submits a query through the web interface.  
2. Backend sends the query to multiple LLM agents.  
3. Each agent generates its response independently.  
4. Responses are displayed side by side to the user.  
5. Voting mechanism marks the most preferred answer.

---

## 🚀 Key Features
- Displays answers from multiple LLMs side by side.  
- Highlights the most preferred answer based on votes.  
- Optimized for faster multi-model query handling.

---

## ⚡ Performance
- Before optimization: ~5–6 seconds per query  
- After optimization: ~2–3 seconds per query  
- Technique used: Asynchronous API calls and response caching

---

## 📘 Documentation
- [Project Development Journey](docs/00_project_journey.md)  
- [Voting Mechanism](docs/05_voting_mechanism.md)  
- [Performance Optimization](docs/07_performance_optimization.md)

---

## 🛠️ Tech Stack
- Python  
- Flask  
- OpenAI API / Other LLM APIs  
- JavaScript, HTML, CSS (Frontend)

---

## ⚠️ Limitations
- Dependent on external LLM APIs, which may have rate limits.  
- Voting mechanism may not always capture nuanced correctness.

---

## 🔮 Future Work
- Support for more than three LLMs.  
- Implement user feedback integration to improve voting accuracy.  
- Introduce model weighting based on past performance.

---

## 📌 One-Line Takeaway
> Aggregating multiple LLM responses with a voting system produces more reliable and accurate answers.

