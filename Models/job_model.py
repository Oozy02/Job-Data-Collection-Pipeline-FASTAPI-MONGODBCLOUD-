from pydantic import BaseModel
from typing import List

class jobs(BaseModel):
    Company: str
    Role: str
    Location: str
    Type: str
    
# class manyjobs(BaseModel):
#     data : List[str]