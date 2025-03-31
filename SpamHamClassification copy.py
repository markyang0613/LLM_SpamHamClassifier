from fastapi import FastAPI
from pydantic import BaseModel

import openai

openai.api_key = '********************'

app = FastAPI()

class Message(BaseModel):
    message:str

@app.post("/classify")
async def classify_message(message: str):
    response = openai.chat.completions.create(
        model='ft:gpt-3.5-turbo-0125:personal::BGBqjRQe', 
        messages=[
            {"role": "user", "content": message}
        ],
        max_tokens=1,
        temperature=0
    )
    classification = response.choices[0].message.content.strip()
    return {
        "original_message": message,
        "classification": classification,
        "detail": f"This message is classified as '{classification.upper()}'."
    }



