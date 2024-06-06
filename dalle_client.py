from openai import OpenAI

client = OpenAI()

def request_dalle(user_message):
    response = client.images.generate(
    model="dall-e-3",
    prompt=user_message + "and make sure that there's plenty of possums in the background, some of them on rollerblades wearing neon colored shorts. Also, somewhere in the picture there should be a framed picture of Thomas Bernhard.",
    size="1024x1024",
    quality="standard",
    response_format="url",
    n=1,
    )

    return response.data[0].url