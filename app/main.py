from fastapi import FastAPI
from app.routers import tasks # Импортируем наш роутер из соседней папки
    
app = FastAPI(title="LifeOS API", version="0.2.0")

# Регистрируем роутер
# Все пути из tasks.py добавятся в приложение
app.include_router(tasks.router)
@app.get("/")
async def root():
    return {"message": "Welcome ot LifeOS API Sructure"}