from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize Ollama with your chosen model
# 需要先执行 ollama server
local_llm = ChatOllama(
    model="deepseek-r1:1.5b",
    temperature=0,
)

# Create an LCEL chain using the local model
prompt = PromptTemplate.from_template("用简单的语言解释 {concept}")
local_chain = prompt | local_llm | StrOutputParser()
# Use the chain with your local model
result = local_chain.invoke({"concept": "量子计算"})
print(result)
