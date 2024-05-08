from pydantic import BaseModel

# User data model
class User(BaseModel):
    id: int
    name: str
    age: int