from config import set_environment
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

set_environment()
chat = ChatOpenAI(model="deepseek-chat")
messages = [
    SystemMessage(content="You're a helpful programming assistant"),
    HumanMessage(content="Write a Python function to calculate factorial")
]

response = chat.invoke(messages)
print(response)