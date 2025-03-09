from anthropic import Anthropic
from config import api_key

client = Anthropic()

firstmessage = client.messages.create(
    model='claude-3-haiku-20240307',
    max_tokens=1000,
    messages= [
        {"role": "user",
        "content":"Tell me a joke about a cute dog."
        }
    ]
)

print(firstmessage.content[0].text)