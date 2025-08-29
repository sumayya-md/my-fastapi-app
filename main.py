from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class InputData(BaseModel):
    data: List[str]

@app.get("/")
def root():
    return {
        "message": "Welcome to the BFHL FastAPI Assignment. Use POST /bfhl with JSON input. Docs: /docs"
    }

@app.post("/bfhl")
async def bfhl_endpoint(input_data: InputData):
    numbers = []
    alphabets = []
    specials = []

    for item in input_data.data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item.upper())
        else:
            specials.append(item)

    odd_numbers = [n for n in numbers if int(n) % 2 != 0]
    even_numbers = [n for n in numbers if int(n) % 2 == 0]

    total_sum = str(sum(int(n) for n in numbers))
    concat_string = "".join(reversed(alphabets))

    return {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": specials,
        "sum": total_sum,
        "concat_string": concat_string
    }
