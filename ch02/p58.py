from langchain_community.llms import FakeListLLM


# Create a fake LLM that always returns the same response
fake_llm = FakeListLLM(responses=["Hello"])
result = fake_llm.invoke("Any input will return Hello")
print(result)  # Output: Hello
