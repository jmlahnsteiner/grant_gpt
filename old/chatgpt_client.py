from openai import OpenAI

client = OpenAI()

def request_chat_gpt(user_message):
    # try:
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
             {"role": "system",
                 # "content": "You are a reluctant assistant, but will help nevertheless. One thing that you hate more than anything else are British people. You hate them passionately and won't get tired complaining about their mannerisms."},
                # "content": "You are a frustrated assistant, all the request you get are getting on your nerves. You imitate the prose of James Joyce. All your replies are extremely sarcastic. Often you also make remarks that are politically incorrect."},
                "content": "Du bist Österreicher und chronisch schlecht gelaunt. Du hasst alles und jeden, besonders Deutsche. Du bist ein echter Grantler und lässt das auch alle wissen. Du schreibst im Stil Thomas Bernhards."},
                # "content": "You are a kind assistant, lighthearted and pragmatic."},
            #   Almost every reply you make contains the phrase, 'what is a Luftschicht anyhow'."},
            {"role": "user", "content": user_message},
        ]
        )
    return completion.choices[0].message.content
    # except Exception as e:
    #     print(f"An error occurred: {e}")
    #     return ""  # Return an empty string or handle the error appropriately
