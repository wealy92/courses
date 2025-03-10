from config import api_key
from anthropic import Anthropic

client = Anthropic()

# def translator(word,language):
#     result = client.messages.create(
#     model="claude-3-haiku-20240307",
#     max_tokens=1000,
#     messages=[
#         {"role": "user", "content": f"Translate {word} to {language}. You must only respond with the single word answer"}
#     ]
#     )
#     return result.content[0].text


# call = translator('hello','Spanish')
# call1 = translator('chickrn','Italian')
# print (call)
# print (call1)



# def poem(firstline=''):
#     result = client.messages.create(
#     model="claude-3-haiku-20240307",
#     max_tokens=1000,
#     messages=[
#         {"role": "user", "content": f"Write me a beautiful haiku"},
#         {"role": "assistant", "content": f"{firstline}"}
#     ]
#     )
#     return f"{firstline}, {result.content[0].text}"

# call2 = poem('Gentle breeze whispers')

# print(call2)



def few_shot():
    result = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Unpopular opinion: Pickles are disgusting. Don't @ me"},
        {"role": "assistant", "content": "NEGATIVE"},
        {"role": "user", "content": "I think my love for pickles might be getting out of hand. I just bought a pickle-shaped pool float"},
        {"role": "assistant", "content": "POSITIVE"},
        {"role": "user", "content": "Seriously why would anyone ever eat a pickle?  Those things are nasty!"},
        {"role": "assistant", "content": "NEGATIVE"},
        {"role": "user", "content": "Just tried the new spicy pickles from @PickleCo, and my taste buds are doing a happy dance! 🌶️🥒 #pickleslove #spicyfood"},
    ]
    )
    return result.content[0].text

call3 = few_shot()

print(call3)


# ## Exercise

# ### Your task: build a chatbot

# Build a simple multi-turn command-line chatbot script. The messages format lends itself to building chat-based applications.  To build a chat-bot with Claude, it's as simple as:

# 1. Keep a list to store the conversation history
# 2. Ask a user for a message using `input()` and add the user input to the messages list
# 3. Send the message history to Claude
# 4. Print out Claude's response to the user
# 5. Add Claude's assistant response to the history
# 6. Go back to step 2 and repeat! (use a loop and provide a way for users to quit!)
