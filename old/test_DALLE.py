from openai import OpenAI
import webbrowser

client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="a possum, wearing a trench coat, flashing",
  size="1024x1024",
  quality="standard",
  response_format="url",
  n=1,
)

image_url = response.data[0].url
webbrowser.open(image_url)
# print(image_url)