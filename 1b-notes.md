
In the prompt we send a message. The message is a list of dictionaries.
Each dictionary holds, who sent the message, what type it is and what the content was.

e.g.

send message = client.messages.create(
    models='model name'
    maxtokens=int
    message[
        {'role':'user','content':'this is first message'},
        {'role':'assistant','content':"I'm good thanks, what do you want to talk about?"}
    ]
)

Quiz:

What are the 2 keys required in each message?

Role, content B

EVERYTHING IS STORED IN CONTENT