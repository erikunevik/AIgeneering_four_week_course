from pydantic import BaseModel, Field


class Movie(BaseModel):
    title: str
    year: int = Field(gt=1970)
    genre: str = Field(
            description="Genre of the movie, if there are many genres, take the dominating one"
    )
    rating: int = Field(gt=0, lt=6, description="Higher rating the better, keep ratings realistic")


class Prompt(BaseModel):
    prompt: str
