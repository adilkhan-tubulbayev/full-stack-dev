import os

from dotenv import load_dotenv
load_dotenv()

gpt = os.getenv('API_KEY')
test = os.getenv('TEST')
print(gpt)
print(test)