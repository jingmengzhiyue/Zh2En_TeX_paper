
import openai
import os

openai.api_key = os.environ["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"]
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Hello, what's your name?",
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.5,
)

print(response.choices[0].text)