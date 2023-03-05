import openai
api_key = "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"
openai.api_key = api_key
def send_message(message_log):
    # Use OpenAI's ChatCompletion API to get the chatbot's response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # The name of the OpenAI chatbot model to use
        messages=message_log,   # The conversation history up to this point, as a list of dictionaries
        max_tokens=2048,        # The maximum number of tokens (words or subwords) in the generated response
        stop=None,              # The stopping sequence for the generated response, if any (not used here)
        temperature=0.2,        # The "creativity" of the generated response (higher temperature = more creative)
    )

    # Find the first response from the chatbot that has text in it (some responses may not have text)
    for choice in response.choices:
        if "text" in choice:
            return choice.text

    # If no response with text is found, return the first response's content (which may be empty)
    return response.choices[0].message.content


def GPT_trans(message):
    # message_log = [
    #     {"role": "system", "content": "You are an outstanding academic paper translation expert. Please translate the following text into English in a concise and accurate manner, so that it can be published in a top academic journal."}
    # ]
    # response = send_message(message_log)
    message_log  = [{"role": "user", "content": "please translate to english"+message}]
    # message_log.append({"role": "assistant", "content": "You are an outstanding academic paper translation expert. Please translate the following text into English in a concise and accurate manner, so that it can be published in a top academic journal."})
    response = send_message(message_log)
    return response
# if __name__ == "__main__":
#     response = GPT_trans("由于高光谱图像仅包含有限数量的物质，因此可以将其视为嵌入高维空间的一系列低维子流形。 通常来说位于同一子流形中的像素有更高的相似性，而不同子流形之间的像素相似度更低。通过对高空间分辨率的多光谱图像施加流形正则化可以有效提升重构图像的空间分辨率。对多光谱图像进行空间聚类可以得到K个子流形A和每个子流形对应的聚类中心B。")
#     print(f"AI assistant: {response}")