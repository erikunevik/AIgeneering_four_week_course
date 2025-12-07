
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

@app.get("/filter/glossary/")
async def filter_glossary(
    word: str = Query(None, description="Sök efter ett specifikt ord i gloslistan")
):
    if word is None:
        return words  
    
    
    filtered = [item for item in words if item.word.casefold() == word.casefold()]
    
    return filtered

#C)

@app.post("/Create/glossary")
async def create_new_glossary(query: api_glossary): 
    result = (query)
    created_glossary = result
    words.append(created_glossary)
    return created_glossary
    
@app.put("/update/glossary")
async def update_glossary(updated_glossary: api_glossary):
    for i, glossary in enumerate(words): # i är indexnumret, glossary innehållet i api_glossaryn för det numret
        if glossary.id == updated_glossary.id:
            words[i] = updated_glossary
    return updated_glossary

@app.delete("/delete/glossary/{id}")
async def delete_glossary(id: int):
    for i, glossary in enumerate(words):
        if glossary.id == id:
            del words[i]
            break
        
