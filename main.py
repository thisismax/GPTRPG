import openai as o
from os import getenv
from pathlib import Path
from dotenv import load_dotenv


def setup():
    ### Environment

    p = Path('.')
    ENV = p/"venv/.env"
    load_dotenv(ENV)
    APIKEY = getenv("OPENAI_API_KEY")
    ORGID = getenv("OPENAI_ORG_ID")

    ### Openai setup
    o.organization = ORGID
    o.api_key = APIKEY


def test():
    response = o.Completion.create(
        model="text-davinci-002",
        prompt="Say this is a test",
        max_tokens=6,
        temperature=0
    )

    print(response)

    
if __name__ == '__main__':
    setup()
    test()


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