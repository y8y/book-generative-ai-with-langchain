import os
from config import set_environment
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

os.environ["LANGCHAIN_DEBUG"] = "true"  # 启用调试输出
os.environ["LANGCHAIN_TRACING_V2"] = "false"  # 关闭 LangSmith 远程追踪

set_environment()

# Create a template
template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an experienced programmer and mathematicalanalyst."),
        ("user", "{problem}"),
    ]
)
# Initialize with reasoning_effort parameter
chat = ChatOpenAI(
    model="deepseek-reasoner",
    reasoning_effort="high",  # Options: "low", "medium", "high"
)

chain = template | chat
response = chain.invoke({"problem": "帮我计算一下从深圳到法兰克福的最佳出行策略"})
print(response.content)
