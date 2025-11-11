from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from config import set_environment

set_environment()

# Create components
prompt = PromptTemplate.from_template("Tell me a joke about {topic}")
llm = ChatOpenAI(model="deepseek-chat")
output_parser = StrOutputParser()

# Chain them together using LCEL
chain = prompt | llm | output_parser
# Execute the workflow with a single call
result = chain.invoke({"topic": "programming"})
print(result)
