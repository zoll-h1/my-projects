from fastapi import FastAPI
#  Импортируем создание таблицы
from app.database import engine, Base
# Имопртируем наш роутер
from app.routers import task_router

# 1. Создаем таблицы в базе данных(если их нет)
# При запуске этот код посмотрит на все модели и создаст файл lifos.db
Base.metadata.create_all(bind=engine)

app = FastAPI(title="LIfeOS")

# 2.Подключаем роутер к приложению
app.include_router(task_router.router)

@app.get("/")
def root():
    return {"message": "Welcome to LifeOS"}