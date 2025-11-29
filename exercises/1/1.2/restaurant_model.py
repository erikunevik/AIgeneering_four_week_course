from pydantic import BaseModel, Field
from typing import Literal
from pydantic_ai import Agent

# agent = Agent(model="google-gla:gemini-2.5-flash")

class Restaurant(BaseModel):
    name: str 
    type_of_food: str = Field(description="short description of the type of food the restaurant serves")
    price_level: Literal["Cheap", "Medium", "Exclusive"] = Field(
    description="Name price level of the restaurants into categories: 'Cheap', 'Medium', 'Exclusive'"
    )
    rating: int = Field(gt=0, lt=10, description="Rate the restaurants between 0-10")
    description: str = Field(description="describe the resturant with a short description")
    opening_hours: str = Field(description="Opening hours for the restaurant") 
    location: str = Field(description="The location and adress for the restuarant")  
    
    
restaurant_list = list[Restaurant]

class Prompt(BaseModel):
    prompt: str
    
    
# result = await agent.run(
#     "Create 10 different resturants that were located in Stockholm in the 1920's",
#     output_type=restaurant_list,
# )

# result