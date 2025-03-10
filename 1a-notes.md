For env variables we are creating a .env file and using a python module dotenv to load.
pip install python-dotenv

In .env define your key. We did ANTHROPIC_API_KEY = 'done forget the "" '

then create a config file config.python

Use this to pass our .env string to our environment. Then retreive it and assign it to a reference

from dotenv import load_dotenv
import os
load_dotenv
ref = os.getenv('ANTHROPIC_API_KEY')

This means that .env needs to be included in .gitignroe


---

Note when you import, it runs this.

---
Q:
what is the .contect on message
