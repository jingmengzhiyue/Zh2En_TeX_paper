import openai

# Define OpenAI API key 
openai.api_key = "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"

# Set up the model and prompt
model_engine = "gpt-3.5-turbo"
prompt = "You are an outstanding academic paper translation expert, please help me translate the following text into Chinese: If this is not the first request, get the user's input and add it to the conversation history"

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)