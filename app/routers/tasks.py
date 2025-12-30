from fastapi import APIRouter
from app.models.task import Task # Импортируем нашу модель из соседней папки

# Создаем роутер вместо app
router = APIRouter()

# Временная база данных (пока живет тут)
fake_db = []

# Важно: используем @router, а не @app
@router.get("/tasks")
async def get_tasks():
    return fake_db

@router.post("/tasks")
async def create_task(task: Task):
    fake_db.append(task)
    return {"status": "ok", "data": task}