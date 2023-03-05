import openai
api_key = "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"
openai.api_key = api_key
def send_message(message_log):
    # Use OpenAI's ChatCompletion API to get the chatbot's response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # The name of the OpenAI chatbot model to use
        messages=message_log,   # The conversation history up to this point, as a list of dictionaries
        max_tokens=4096,        # The maximum number of tokens (words or subwords) in the generated response
        stop=None,              # The stopping sequence for the generated response, if any (not used here)
        temperature=0.2,        # The "creativity" of the generated response (higher temperature = more creative)
    )

    # Find the first response from the chatbot that has text in it (some responses may not have text)
    for choice in response.choices:
        if "text" in choice:
            return choice.text

    # If no response with text is found, return the first response's content (which may be empty)
    return response.choices[0].message.content


if __name__ == "__main__":
    message_log = "You are an outstanding academic paper translation expert, please help me translate the following text into Chinese: If this is not the first request, get the user's input and add it to the conversation history"
    message_log = [
        {"role": "system", "content": "You are an outstanding academic paper translation expert, please help me translate the following text into Chinese."}
    ]
    response = send_message(message_log)
    print(f"AI assistant: {response}")