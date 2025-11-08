from config import set_environment
from langchain_openai import ChatOpenAI

set_environment()

llm = ChatOpenAI(
    model="deepseek-chat",  # 官方给出的聊天模型名
    temperature=0.7,
)

resp = llm.invoke("用一句话介绍一下 DeepSeek。")
print(resp.content)
