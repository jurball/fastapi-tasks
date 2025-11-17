from pydantic import BaseModel
from typing import Optional

class STaskAdd(BaseModel): # сущность таски
    name: str
    description: Optional[str] = None # как необязательный


class STask(STaskAdd):
    id: int