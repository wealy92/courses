from config import api_key
from anthropic import Anthropic

client = Anthropic()

firstmessage = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    messages=[
        {"role": "user", 
        "content": "Hi there! Please write me a haiku about a pet chicken"
        }
    ]
)

print(firstmessage.content[0].text)