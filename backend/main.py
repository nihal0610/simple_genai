from fastapi import FastAPI
from pydantic import BaseModel
import os
from groq import Groq

# Load Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_groq(query: Query):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # Groq's fast LLaMA3 model
            messages=[{"role": "user", "content": query.question}],
            max_tokens=200
        )
        answer = response.choices[0].message.content
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}

