from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/generate_business_name")
async def generate_business_name(prompt: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a creative business name generator."},
            {"role": "user", "content": f"Generate a business name based on this description: {prompt}"}
        ],
        max_tokens=50
    )
    return {"business_name": response.choices[0].message.content.strip()}