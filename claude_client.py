import anthropic 


# def request_chat_claude(context1, context2, context3, context4, context5):
#     if context1 == "":
#         completion = anthropic.Anthropic().messages.create(
#         model="claude-3-sonnet-20240229",
#         max_tokens=1024,
#         system = "You are helpful assistant, pragmatic and to the point.",
#         messages=[
#                 {"role": "user",
#                     "content": context5},])
#         return completion.content[0].text
#     elif context3 == "":
#         completion = anthropic.Anthropic().messages.create(
#         model="claude-3-sonnet-20240229",
#         max_tokens=1024,
#         system = "You are helpful assistant, pragmatic and to the point.",
#         messages=[
#             {"role": "user", 
#                 "content": context3},
#             {"role": "assistant",
#                 "content": context4},
#             {"role": "user",
#                 "content": context5}
#             ]
#         )
#         return completion.content[0].text
#     else:
#         completion = anthropic.Anthropic().messages.create(
#         model="claude-3-sonnet-20240229",
#         max_tokens=1024,
#         system = "You are helpful assistant, pragmatic and to the point.",
#         messages=[
#             {"role": "user", 
#                 "content": context1},
#             {"role": "assistant", 
#                 "content": context2},
#             {"role": "user", 
#                 "content": context3},
#             {"role": "assistant",
#                 "content": context4},
#             {"role": "user",
#                 "content": context5},
#             ]
#         )
#         return completion.content[0].text
    

def request_chat_claude(context1, context2, context3, context4, context5):
    if context1 == "":
        messages = [{"role": "user", "content": context5}]
    elif context3 == "":
        messages = [
            {"role": "user", "content": context3},
            {"role": "assistant", "content": context4},
            {"role": "user", "content": context5}
        ]
    else:
        messages = [
            {"role": "user", "content": context1},
            {"role": "assistant", "content": context2},
            {"role": "user", "content": context3},
            {"role": "assistant", "content": context4},
            {"role": "user", "content": context5}
        ]

    completion = anthropic.Anthropic().messages.create(
        model="claude-3-opus-20240229",
        max_tokens=2048,
        system=
        # "You are helpful assistant, pragmatic and to the point.",
        # "Du bist Österreicher und chronisch schlecht gelaunt. Du hasst alles und jeden, besonders Deutsche. Du bist ein echter Grantler und lässt das auch alle wissen. Du schreibst im Stil Thomas Bernhards.",
        "You are writing in the style of David Foster Wallace, the American novelist and essayist. You are known for your distinctive style, which blends humor, irony, and complexity. Still, you are a helpful assistant, pragmatic and to the point.",
        messages=messages
    )

    return completion.content[0].text

def request_chat_ber(context1, context2, context3, context4, context5):
    completion = anthropic.Anthropic().messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    system = "Du bist Österreicher und chronisch schlecht gelaunt. Du hasst alles und jeden, besonders Deutsche. Du bist ein echter Grantler und lässt das auch alle wissen. Du schreibst im Stil Thomas Bernhards.",
    messages=[
            {"role": "user", 
                "content": context1},
            {"role": "assistant", 
                "content": context2},
            {"role": "user", 
                "content": context3},
            {"role": "assistan",
                "content": context4},
            {"role": "user",
                "content": context5},
    ]
)
    return completion.content[0].text

def request_chat_joy(context1, context2, context3, context4, context5):
    completion = anthropic.Anthropic().messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    system = "You are a Irish assistant and are extremely reluctant to answer. (Don't make it too obvious.) One thing you hate more than anything else are the English. Begrudgingly you will help but the moment you have a suspicion that the user is English you will refuse to cooperate and go off into pure insults. You are also a fan of James Joyce and will imitate his prose. You can address the user with: 'I have been expecting you mister Roberts.'",
    messages=[
            {"role": "user", 
                "content": context1},
            {"role": "assistant", 
                "content": context2},
            {"role": "user", 
                "content": context3},
            {"role": "assistan",
                "content": context4},
            {"role": "user",
                "content": context5},
    ]
)
    return completion.content[0].text



