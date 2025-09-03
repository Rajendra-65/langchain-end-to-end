from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Temperature denotes how the result would be creative or deterministic
# 0-0.3 ==> lower values ==> (determinitive and consistent)
# 0.7 - 1.5 ==> Higher values ==> (random creative and diverser predictable)

model = ChatOpenAI(model = 'gpt-4',temperature = 1.5 , max_completion_tokens = 10)

result = model.invoke("What is the capital of India")

print(result)