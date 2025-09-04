from pydantic import BaseModel

class Item(BaseModel):
    title: str
    description : str
    price: float = None
    count:int
    
