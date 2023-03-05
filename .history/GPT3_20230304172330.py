import openai
api_key = "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"
openai.api_key = api_key
def send_message(message_log):
    # Use OpenAI's ChatCompletion API to get the chatbot's response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # The name of the OpenAI chatbot model to use
        messages=message_log,   # The conversation history up to this point, as a list of dictionaries
        max_tokens=3800,        # The maximum number of tokens (words or subwords) in the generated response
        stop=None,              # The stopping sequence for the generated response, if any (not used here)
        temperature=0.7,        # The "creativity" of the generated response (higher temperature = more creative)
    )

    # Find the first response from the chatbot that has text in it (some responses may not have text)
    for choice in response.choices:
        if "text" in choice:
            return choice.text

    # If no response with text is found, return the first response's content (which may be empty)
    return response.choices[0].message.content


def GPT_trans(message):
    message_log = [
        {"role": "system", "content": "You are an outstanding academic paper translation expert. Please translate the following text into English in a concise and accurate manner, so that it can be published in a top academic journal."}
    ]
    message_log.append({"role": "user", "content": message})
    message_log.append({"role": "assistant", "content": "You are an outstanding academic paper translation expert. Please translate the following text into English in a concise and accurate manner, so that it can be published in a top academic journal."})
    response = send_message(message_log)