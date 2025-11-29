from utils import query_duckdb

query_duckdb("""
CREATE TABLE IF NOT EXISTS ten_restaurants (
    name TEXT,
    type_of_food TEXT,
    price_level TEXT,
    rating INTEGER,
    description TEXT,
    opening_hours TEXT,
    location TEXT,
);
""")             
        