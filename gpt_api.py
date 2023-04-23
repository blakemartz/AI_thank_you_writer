import openai

MODEL = "gpt-3.5-turbo"
MAX_TOKENS = 1000
TEMPERATURE = 0.8


# fetch api_key
def get_api_key():
    with open("openai_api_key.txt", "r") as file:
        key = file.read()
    return key


# api helper function
def generate_text(chat_thread, api_key):
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=chat_thread,
        max_tokens=MAX_TOKENS,
        n=1,
        temperature=TEMPERATURE,
    )

    if response.choices:
        generated_text = response.choices[0].message['content']
        return generated_text.strip()
    else:
        return None


def write_thank_you(guest, gift, signature, occasion):
    chat_thread = [{
        "role": "system",
        "content": f"You are a writing assistant to help write heartfelt and personal thank you letters for gifts."
                   f"The occasion was '{occasion}'."
                   f"Don't be too formal. "
                   f"Please thank them for their thoughtfulness. "
                   f"Do not use the phrase 'we hope this letter finds you'."
                   f"Please sign the letters {signature}."
    },
        {
        "role": "user",
        "content": f"Generate a thank you letter to our guest '{guest}'. "
                   f"Please thank them for '{gift}'. "
         }]

    # Call the helper function to generate response
    generated_text = generate_text(chat_thread=chat_thread, api_key=get_api_key())

    return generated_text
