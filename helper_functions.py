import os
import openai
import tiktoken
from dotenv import load_dotenv, find_dotenv

# set open ai token using .env file
_ = load_dotenv(find_dotenv())

# Read in the API key from the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

print(openai.api_key)


# generic single prompts
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.Completion.create(
        model=model,
        messages=messages,
        temperature=0,
        # max_tokens=100,
        # top_p=1,
        # frequency_penalty=0,
    )

    output = response.choices[0].message["content"]

    print(f"Prompt: {prompt} \n Response: {output}")
    return output


# chat prompts
def get_completion_from_messages(
    messages, model="gpt-3.5-turbo", temperature=0, max_tokens=500
):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    output = response.choices[0].message["content"]

    print(f"Prompt: {messages} \n Response: {output}")
    return output


# chat prompt + token evaluations


def get_completion_and_token_count(
    messages, model="gpt-3.5-turbo", temperature=0, max_tokens=500
):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    content = response.choices[0].message["content"]

    token_dict = {
        "prompt_token": response["usage"]["prompt_tokens"],
        "completion_tooken": response["usage"]["completion_tokens"],
        "total_tokens": response["usage"]["total_tokens"],
    }

    print(f"Response: {content} \n tokens: {token_dict}")

    return content, token_dict
