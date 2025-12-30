from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="LifeOS API")

class Task(BaseModel):
    # The title of the task , which is really important
    title:str
    # A detailed description of the task
    description:str | None = None
    # The status of the task, whether it's completed or not
    completed: bool = False
#  WE will store tasks im memory , cause we don't have PostreSQL(for now)
#  If the server will overload we will loose all the tasks(for now it's ok)
fake_db = []
#  ENDPOINTS
@app.get("/tasks")
async def get_tasks():
    return fake_db

# Create a new task
# Самое интересное тут : task : Task
# FastAPI увидит что , прочиатет json от пользователя
# проверит его через Pydantic , и превратит в обьект task
@app.post("/tasks")
async def create_task(task: Task):
    fake_db.append(task)
    return {"status": "ok", "data": task}
