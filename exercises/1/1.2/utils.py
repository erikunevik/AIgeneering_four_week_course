from pathlib import Path
import duckdb

DATAPATH = Path(__file__).parent / "data"



def query_duckdb (sql_code: str, parameters=None):
    with duckdb.connect(DATAPATH / "restaurants.duckdb") as conn:
        cursor = conn.execute(sql_code, parameters)
        
        lower = sql_code.strip().lower()
        if lower.startswith(("select", "from", "desc", "pragma")):
            
            return cursor.df()
    
