from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from config import set_environment

set_environment()

# Initialize the model
llm = ChatOpenAI(model="deepseek-chat")

# First chain generates a story
story_prompt = PromptTemplate.from_template("写一个关于以下主题的故事：{topic}")
story_chain = story_prompt | llm | StrOutputParser()
# Second chain analyzes the story
analysis_prompt = PromptTemplate.from_template("分析以下故事的情绪:\n{story}")
analysis_chain = analysis_prompt | llm | StrOutputParser()

# Combine chains
story_with_analysis = story_chain | analysis_chain
# Run the combined chain
story_analysis = story_with_analysis.invoke({"topic": "下雨天"})
print("\nAnalysis:", story_analysis)
