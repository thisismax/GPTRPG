import openai as o
import os
from pathlib import Path
from dotenv import load_dotenv

### Environment

p = Path('.')
ENV = p/"venv/.env"
load_dotenv(ENV)
APIKEY = os.getenv("OPENAI_API_KEY")
ORGID = os.getenv("OPENAI_ORG_ID")

### Openai setup

o.organization = ORGID
o.api_key = APIKEY


response = o.Completion.create(
  model="text-davinci-002",
  prompt="Say this is a test",
  max_tokens=6,
  temperature=0
)

print(response)

print("")

'''
To create a model I need to:
- build a prompt
- build a database structured for the prompt
- build a way to convert the database to JSONL
    - such as this: https://galea.medium.com/how-to-love-jsonl-using-json-line-format-in-your-workflow-b6884f65175b
    - or jsonlines module
- create the fine-tune model - can this only happen in the CLI?
    - lul - the cli is written in python. Just read how it reads the arguments and call it directly.
    - Or something

Make request:
openai.Completion.create(
    model=FINE_TUNED_MODEL,
    prompt=YOUR_PROMPT)

'''