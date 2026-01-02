# 0. Routers ( Пульт управления )
# 1. Imports from FastAPI
# APIRouter - это "мини-приложение". Мы используем его вместо 'app = FastAPI()'.
# Depends - это 'Магия' которая дает нам сессию БД
# HTTPException - чтобы выдавать ошибки (404 , 400).
from fastapi import APIRouter, Depends, HTTPException

# 2. Import for session typification
from sqlalchemy.orm import Session


# Import our blanks
from app.database import get_db          # Функция дающая сессию 
from app.models import task_model as models    # Таблицы (Алиас models для удобства)
from app.schemas import task_schemas as schemas  # Схемы (Алиас schemas)

# Создаем роутер.
# prefix="/tasks" - значит все пути будут начинаться с /tasks
# tags=["Tasks"] - для красивой ггруппировки в документации Swagger
router = APIRouter(prefix="/tasks", tags=["tasks"])


#  ENDPOINT 1 : Create a task
@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    # 1. Превращаем Pydantic-схему в Модель SQLAlchemy
    # Мы берем данные из task (title="...", description="...")
    # И создаем обьект для базы данных.
    # **task.model_dump() - распаковка словаря (как title=task.title, ...)
    # Если python старый или Pydantic v1, используют task.dict()
    new_task = models.Task(**task.model_dump())

    # 2. Кладем в сессию
    db.add(new_task)

    # 3. Сохраняем(Commit)
    db.commit()

    # 4. Обновляем(Refresh), чтобы получить ID, который создала база
    db.refresh(new_task)

    # 5. Возвращаем готовую задачу(Pudantic сам превратит ее в json)
    return new_task

#  ENDPOINT 2 : Get all tasks (Read all)
#  response_model=list[schemas.Task] - тут мы возвращаем список задач
@router.get("/", response_model=list[schemas.Task])
def read_tasks(skip: int = 0,  limit: int = 100, db: Session = Depends(get_db)):
    # Делаем запрос к базе через новый стиль 
    # db.query - это старый стиль, но самый понятный для старта
    # offset(skip) - пропустить первые N 
    # limit(limit) - взять не боьше N штук
    tasks = db.query(models.Task).offset(skip).limit(limit).all()
    return tasks
# HTTPExceptions
@router.get("/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task.id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task

# ENDPOINT 4: Update the task
@router.put("/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task_data: schemas.TaskCreate, db: Session = Depends(get_db)):
    # 1. Ищем задачу в базе
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    # 2. Проверяем, существует ли она
    if task is None:
        raise HTTPException(status_code=404, detail="The task is not found")
    # 3. Обновляем поля
    # Мы берем title из присланных данных и ставим его в нашу задачу
    task.title = task_data.title
    task.description = task_data.description
    task.is_completed = task_data.is_completed

    # 4. Сохраняем изменения
    db.commit()

    # 5. Обновляем данные в переменной
    db.refresh(task)
    return task

# ENDPOINT 5: Удалить задачу 
@router.delete("/{task_id}")
def delete_task(task_id:int, db:Session = Depends(get_db)):
    # 1. Ищем задачу 
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    # 2. Проверяем существование
    if task is None:
        raise HTTPException(status_code=404, detail="The task is not found")
    # 3. Delete
    db.delete(task)

    # 4. Фиксируем удаление
    db.commit()

    # 5. Success
    return {"message": "The task is succesfully deleted"}