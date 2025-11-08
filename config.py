import os

OPENAI_API_KEY = "sk-a470a09d0f08457590322b7e81c7becd"
OPENAI_API_BASE = "https://api.deepseek.com/v1"


def set_environment():
    variable_dict = globals().items()
    for key, value in variable_dict:
        if "API" in key or "ID" in key:
            os.environ[key] = value
