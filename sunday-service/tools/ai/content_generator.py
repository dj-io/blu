import os
import openai
from dotenv import load_dotenv

load_dotenv(".env")

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

openai.api_key = OPENAI_API_KEY

def generate_docs(message: str) -> dict:
  """Generate context based documentation returned in JSON format"""
  completion = openai.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
    {"role": "developer", "content": "You are an expert technical writer."},
    {"role": "user", "content": "generate a readme for a new project"}
   ]
  )

  return { "haiku": completion.choices[0].message.content }
