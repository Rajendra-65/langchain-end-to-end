from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal

load_dotenv()

#schema

model = ChatOpenAI()

class Review(TypedDict):
    key_themes : Annotated[list[str],"Write down all the key themes discussed in the review in a list"]
    summary : Annotated[str,"A Breif Summary of the review"]
    sentiment : Annotated[Literal["pos","neg"],"Return sentiment of the review either negateive, positeive or neutral"] 
    pros : Annotated[Optional[list[str]],"Write down all the pros inside a list"]
    cons : Annotated[Optional[list[str]],"Write down all the cons inside a list"]
    name : Annotated[Optional[str],"Write the name of the reviewer"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
    The hardware is great, but the software fells bloated. There are too many pre-installed apps that i Can't remove. Also the UI looks outdated compared to other brands. Hoping for a software update to fix this.
""")

print(type(result))
print(result['summary'])
print(result['sentiment'])