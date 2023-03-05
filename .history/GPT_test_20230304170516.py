
import openai
import os

openai.api_key = os.environ["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"]
response = openai.Completion.create(
    engine="davinci",
    prompt="Once upon a time",
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.5,
)

print(response.choices[0].text)
