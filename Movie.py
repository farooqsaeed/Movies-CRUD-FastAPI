from pydantic import BaseModel
from typing import Optional

class Movie(BaseModel):
    title:str
    year: Optional[int] = None