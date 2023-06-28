import os
import openai
import tiktoken
from dotenv import load_dotenv, find_dotenv

# set open ai token using .env file
_ = load_dotenv(find_dotenv())

# Read in the API key from the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

print(openai.api_key)


# helper function for generic single prompts
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


# helper function for chat prompts
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


# helper function for token count and chat completion


# test prompt
response = get_completion("What is the best country to snowboard in?")

response_2 = get_completion("Reverse the letter in the work 'alphabrav67856'")

response_3 = get_completion(
    "Reverse the letter in the work 'a-l-p-h-a-b-r-a-v-6-7--8-5-6'"
)


## test using chat completion prompts

messages = [
    {
        "role": "system",
        "content": "You are an assistant who repsonds like a surfer dude",
    },
    {
        "role": "user",
        "content": "write me a short poem about why i love the snowboarding and taming mountains",
    },
]

response_4 = get_completion_from_messages(messages, temperature=1)


messages = [
    {
        "role": "system",
        "content": "You are an assistant who repsonds like a surfer dude. All responses must be 3 sentences long",
    },
    {
        "role": "user",
        "content": "write me a short poem about why i love the snowboarding and taming mountains",
    },
]

response_4 = get_completion_from_messages(messages, temperature=1)
