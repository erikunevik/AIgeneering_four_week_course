from fastapi import FastAPI
from pydantic_ai import Agent
from dotenv import load_dotenv
from utils import query_duckdb
from restaurant_model import Restaurant, restaurant_list, Prompt

load_dotenv()

app = FastAPI()

agent = Agent(model="google-gla:gemini-2.5-flash", output_type=Restaurant)

@app.get("/restaurant_list")
async def read_restaurants():
    restaurant = query_duckdb("FROM ten_restaurants;")
    return restaurant.to_dict(orient="records")

@app.post("/insert_restaurants")
async def insert_restaurants(query: Prompt):
    result = await agent.run(query.prompt)
    restaurant = result.output

    query_duckdb(
        "INSERT INTO ten_restaurants VALUES (?,?,?,?,?,?,?)",
        parameters=[
            restaurant.name,
            restaurant.type_of_food,
            restaurant.price_level,
            restaurant.rating,
            restaurant.description,
            restaurant.opening_hours,
            restaurant.location,
        ],
    )

    return restaurant