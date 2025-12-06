
from pydantic import BaseModel
from fastapi import FastAPI, Query
from pathlib import Path
import json

class api_glossary (BaseModel):
    
    id: int
    word: str
    meaning: str
    
class word_list (BaseModel):
    total_list: list[api_glossary] 
    
    
PATH = Path(__file__).resolve().parent.parent / "data"


def get_json(file_path: Path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def transform_file(filename: str):
    full_file_path = PATH / filename
    data = get_json(full_file_path)
    validated_data = word_list.model_validate({"total_list": data})
    return validated_data



function_list = transform_file("fastapi_glossary.json") 
words = function_list.total_list



app = FastAPI()

#A)

@app.get("/glossary")
async def read_books():
    return words  

#B)

@app.get("/glossary/")
async def filter_glossary(
    word: str = Query(None, description="Sök efter ett specifikt ord i gloslistan")
):
    if word is None:
        return words  
    
    
    filtered = [item for item in words if item.word.casefold() == word.casefold()]
    
    return filtered