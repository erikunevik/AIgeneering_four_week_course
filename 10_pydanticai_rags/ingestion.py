import lancedb
from backend.constants import VECTOR_DATABASE_PATH, DATA_PATH
from backend.data_models import Article
import time


def setup_vector_db(path):
    vector_db = lancedb.connect(uri = path)
    vector_db.create_table("articles", schema=Article, exist_ok=True)
    
    return vector_db


def ingest_docs_to_vector_db(table):
    for file in DATA_PATH.glob("*.txt"):
        with open(file, "r") as f:
            content = f.read()
            
        doc_id = file.stem
        table.delete(f"doc_id = '{doc_id}'")
        
        table.add([
            
            {
                
                "doc_id": doc_id,
                "filepath": str(file),
                "filename": file.stem,
                "content": content
                
                
            }
            
        ])
        
        time.sleep(30)