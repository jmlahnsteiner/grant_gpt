import anthropic

response = anthropic.Anthropic().messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": ""},
        {"role": "assistant", "content": "Hi there! How can I help you today?"},
        {"role": "user", "content": "I'm looking for a recipe for a good pasta sauce."},
    ]
)

print(response.content[0].text)