import openai
import os

message1 = {'role': 'system', 'content': 'tell a silly joke about bike-stealing thieves'}
message2 = {'role': 'user', 'content': 'im so mad right now. my bike got stolen.'}

messages = [message1, message2]

response = openai.ChatCompletion.create(
    messages = messages,
    model = 'gpt-4',
    max_tokens = 500,
    user = 'testing_tokens'
)

print(response)