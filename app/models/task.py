from pydantic import BaseModel

# Здесь живет ТОЛЬКО описание данных. Никакой логики.
class Task(BaseModel):
    title: str
    description: str | None = None 
    is_completed: bool = False