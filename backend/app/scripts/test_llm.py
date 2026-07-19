from app.llms.factory import LLMFactory

model = LLMFactory.getLlm("ollama")

response = model.invoke("what is islam")
print(response)
# print(dict(response)['content'])
# print(dict(response)['metadata'])