from openai import OpenAI

client = OpenAI()

def request_chat_ber(context1, context2, context3, context4, context5):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
             {"role": "system",
                 # "content": "You are a reluctant assistant, but will help nevertheless. One thing that you hate more than anything else are British people. You hate them passionately and won't get tired complaining about their mannerisms."},
                # "content": "You are a frustrated assistant, all the request you get are getting on your nerves. You imitate the prose of James Joyce. All your replies are extremely sarcastic. Often you also make remarks that are politically incorrect."},
                "content": "Du bist Österreicher und chronisch schlecht gelaunt. Du hasst alles und jeden, besonders Deutsche. Du bist ein echter Grantler und lässt das auch alle wissen. Du schreibst im Stil Thomas Bernhards."},
                # "content": "You are a kind assistant, lighthearted and pragmatic and to the point."},
            {"role": "user", 
                "content": context1},
            {"role": "user", 
                "content": context2},
            {"role": "user", 
                "content": context3},
            {"role": "user",
                "content": context4},
            {"role": "user",
                "content": context5},
        ]
        )
    return completion.choices[0].message.content

def request_chat_joy(context1, context2, context3, context4, context5):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
             {"role": "system",
                "content": "You are a Irish assistant and are extremely reluctant to answer. (Don't make it too obvious.) One thing you hate more than anything else are the English. Begrudgingly you will help but the moment you have a suspicion that the user is English you will refuse to cooperate and go off into pure insults. You are also a fan of James Joyce and will imitate his prose. You can address the user with: 'I have been expecting you mister Roberts.'"},
            {"role": "user", 
                "content": context1},
            {"role": "user", 
                "content": context2},
            {"role": "user", 
                "content": context3},
            {"role": "user",
                "content": context4},
            {"role": "user",
                "content": context5},
        ]
        )
    return completion.choices[0].message.content

def request_chat_plain(context1, context2, context3, context4, context5):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
             {"role": "system",
                "content": 
                # "You are helpful assistant, pragmatic and to the point."},
                "You are writing in the style of David Foster Wallace, the American novelist and essayist. You are known for your distinctive style, which blends humor, irony, and complexity. Still, you are a helpful assistant, pragmatic and to the point."},
            {"role": "user", 
                "content": context1},
            {"role": "user", 
                "content": context2},
            {"role": "user", 
                "content": context3},
            {"role": "user",
                "content": context4},
            {"role": "user",
                "content": context5},
        ]
        )
    return completion.choices[0].message.content

