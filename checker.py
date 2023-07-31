import openai
import os

openai.api_key = os.environ.get('OPENAI_API_KEY')

messages = [
  {'role': 'user', 'content': 'tell me a 100 one liner jokes'}
]

for i in range(11):
  response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=1000)
  print(response)