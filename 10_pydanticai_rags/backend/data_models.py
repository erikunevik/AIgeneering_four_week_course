from pydantic import BaseModel, Field
from lancedb.embeddings import get_registry
from lancedb.pydatic import Lancemodel, Vector
from dotenv import load_dotenv

load_dotenv()
embedding_model = get_registry().get("gemini-text".create(name="gemini-embedding-001"))

EMBEDDING_DIM = 3072

class Article(LanceModel):
    doc_id: str
    filepath: str
    filename: str = Field(descrption="the stem of the file i.e without suffix")
    content: str = embedding_model.SourceField()
    embedding: Vector(EMBEDDING_DIM) = embedding_model.VectorField()
    
