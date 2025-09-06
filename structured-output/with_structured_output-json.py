from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import BaseModel,Field

load_dotenv()

#schema

model = ChatOpenAI()

json_schema = {
    "title" : "Review",
    "type" : "object",
    "Properties" : {
        "key_themes" : {
            "type" : "array",
            "items" : {
                "type" : "string"
            },
            "description" : "Write down all the key themes discussed in the review in a list"
        },
        "summary" : {
            "type" : "string",
            "description" : "A brief summary of the review"
        },
        "sentiment" : {
            "type" : "string",
            "enum" : ["pos","neg"],
            "description" : "Return sentiment of the review either negative, positive or neutral"
        },
        "pros" : {
            "type" : ["array","null"],
            "items" : {
                "type" : "string"
            },
            "description" : "write down all the pros inside a list"
        },
        "cons" : {
            "type" : ["array","null"],
            "items" : {
                "type" : "string"
            }
        },
        "name" : {
            "type" : ["string", "null"],
            "description" : "Write the name of the reciever"
        }
    }
}

class Review(BaseModel):
    key_themes : list[str] = Field(
        description = "Write down all the key themes discussed in the review in a list"
    )
    summary : str = Field(description = "A Breif Summary of the review")
    sentiment : Literal["pos","neg"] = Field(description = "Return sentiment of the review either negateive, positeive or neutral" )
    pros : Optional[list[str]] = Field(default = None, description = "Write down all the pros inside a list")
    cons : Optional[list[str]] = Field(default = None, )
    cons : Optional[list[str]] = Field(description = "Write down all the cons inside a list")
    name : Optional[str] = Field(default = None, description = "write the name of the reviewer")

structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke("""
    The hardware is great, but the software fells bloated. There are too many pre-installed apps that i Can't remove. Also the UI looks outdated compared to other brands. Hoping for a software update to fix this.
""")

print(type(result))
print(result.summary)
print(result.sentiment)