import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(".env")

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

client = OpenAI(
  api_key=OPENAI_API_KEY
)

def generate_docs():
  """Generate context based documentation returned in JSON format"""
  completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
      {"role": "user", "content": "write a haiku about ai"}
    ]
  )

  return { "haiku": completion.choices[0].message.content }
