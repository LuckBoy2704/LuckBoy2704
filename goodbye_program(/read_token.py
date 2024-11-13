import os
from dotenv import load_dotenv


def get_t():
    load_dotenv()
    token = os.environ['Token']
    return token
