# 📘 Project Development Journey: Multi-Agent LLM Voting System

---

## Step 1: Initial Setup
I began by setting up a Python Flask web application that called a single LLM model to generate answers from user prompts. This initial setup was intended to verify that the model integration worked correctly and that the API returned responses as expected. During this phase, the system successfully generated answers, but they were inconsistent and lacked the ability to provide multiple perspectives.

Screenshot:  
docs/screenshots/response 1.png

---

## Step 2: First Results
After running the initial setup, the application successfully displayed outputs from the single model. While the Flask app executed correctly and API calls returned valid responses, only one answer was generated per prompt. This highlighted that the system could not yet perform multi-agent comparison, and response times were noticeably slow when sequentially calling multiple models.

---

## Step 3: Identified Problems
The limitations of the initial system became clear. Using only a single model prevented comparison of different perspectives. Sequential calls to multiple models increased latency, and some outputs were redundant or inconsistent. These issues were critical because they prevented the implementation of the voting mechanism and could negatively affect the user experience due to slow responses.

---

## Step 4: Major Changes
To address these issues, three LLM agents were integrated to generate responses in parallel. A voting mechanism was implemented to select the most preferred answer, ensuring that the final output represented the consensus among agents. Additionally, asynchronous requests were used to optimize performance and reduce response times. These changes allowed the system to provide multiple perspectives efficiently and improve the overall user experience.

Screenshot:  


---

## Step 5: Errors and Debugging
During implementation, asynchronous API calls initially caused race conditions, and some module imports, such as `utils.safe_max`, failed. These problems were due to incorrect import paths and improperly awaited asynchronous calls. The issues were resolved by correcting the imports, using `asyncio.gather` to safely handle parallel API requests, and adding error handling to retry failed requests. After these fixes, the system became stable and reliable.

Screenshot:  
docs/screenshots/error_after_using_httpx.png

---

## Step 6: Final Working System
The final system features three independent LLM agents generating responses simultaneously. The voting mechanism identifies and highlights the most preferred answer, and all responses are displayed clearly on the interface. Asynchronous execution ensures fast and consistent results. Users can now submit a prompt, receive multiple answers from different agents, and see the consensus response highlighted for clarity.

Screenshot:  

