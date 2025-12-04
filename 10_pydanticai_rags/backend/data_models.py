from pydantic import BaseModel, Field
from lancedb.embeddings import get_registry # För att hämta embedding modeller
from lancedb.pydantic import LanceModel, Vector # Speciella Pydantic-klasser för LanceDB som stöder vektorer
from dotenv import load_dotenv

load_dotenv()

embedding_model = get_registry().get("gemini-text").create(name="gemini-embedding-001")

EMBEDDING_DIM = 3072

class Article(LanceModel):
    """ Represents a wikipedia article with its corresponding embeddings"""
    doc_id: str 
    filepath: str
    filename: str = Field(descrption="the stem of the file i.e without suffix")
    content: str = embedding_model.SourceField() #Baserat på den räknar vi ut embeddingskolumner
    embedding: Vector(EMBEDDING_DIM) = embedding_model.VectorField()
    
class Prompt(BaseModel):
    prompt: str = Field(description="prompt from user, if empty consider it as missing")
    
    # För att vi vill strukturera outputen från chatboten
class RagResponse(BaseModel):
    filename: str = Field(description="filename of retrieved file without suffix")
    filepath: str = Field(description="absolute path to the retrieved file") 
    answer: str = Field(description="answer based on the retrieved file") 
