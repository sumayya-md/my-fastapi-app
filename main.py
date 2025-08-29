from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List
import re
from datetime import datetime
import json

app = FastAPI()

# Replace with your details
FULL_NAME = "john_doe"
DOB = "17091999"   # ddmmyyyy
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

class InputData(BaseModel):
    data: List[str]

def alternating_caps(s: str) -> str:
    """Return string in reverse order with alternating caps"""
    result = []
    upper = True
    for ch in reversed(s):
        if ch.isalpha():
            result.append(ch.upper() if upper else ch.lower())
            upper = not upper
    return "".join(result)

@app.post("/bfhl")
async def bfhl_endpoint(request: Request):
    try:
        # read raw body
        raw_body = await request.body()
        body_str = raw_body.decode("utf-8")

        # replace curly quotes with normal quotes
        body_str = body_str.replace("“", '"').replace("”", '"')

        # parse JSON manually
        data_dict = json.loads(body_str)
        input_data = InputData(**data_dict)

        numbers = []
        alphabets = []
        specials = []

        for item in input_data.data:
            if item.isdigit():  # numeric string
                numbers.append(item)
            elif item.isalpha():  # alphabets
                alphabets.append(item.upper())
            else:  # special chars (anything else)
                specials.append(item)

        # classify odd/even
        odd_numbers = [n for n in numbers if int(n) % 2 != 0]
        even_numbers = [n for n in numbers if int(n) % 2 == 0]

        # sum of numbers
        total_sum = str(sum(int(n) for n in numbers))

        # concat reversed alternating caps
        concat_string = alternating_caps("".join(alphabets))

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME.lower()}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": specials,
            "sum": total_sum,
            "concat_string": concat_string
        }
        return response
    except Exception as e:
        return {"is_success": False, "error": str(e)}
