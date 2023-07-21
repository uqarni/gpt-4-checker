import openai
import os

openai.api_key = os.environ.get('OPENAI_API_KEY')

messages = [
  {'role': 'user', 'content': 'tell me a one liner joke'}
]

response = openai.ChatCompletion.create(model="gpt-4", messages=messages, max_tokens=600)
