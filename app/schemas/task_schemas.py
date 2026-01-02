# 0. Schemas - Охрана и фейс-контроль 
# Посредник который проверяет данные на входе и отфильтрует на выходе
# Pydantic schemas

# 1. Импортируем BaseModel
# Это основа всех схем Pydantic. Как Base для SQLAlchemy.
from pydantic import BaseModel

# 2. Создаем Базовую схему (TaskBase)
# Сюда мы пишем поля , которые ОБЩИЕ для создания и для чтения.
# Чтобы не дублировать код.
class TaskBase(BaseModel):
    title: str
    description: str | None = None
    is_completed: bool = False

# 3. Схема для СОЗДАНИЯ (TaskCreate)
# Эту схему мы будем ждать от пользователя (в POST запросе).
# Она наследуется от TaskBase, значит , что в ней уже есть title, description, is_completed.
# Пока она пустая (pass) , но в будущем мы можем добавить сюда , например , пароль задачи ,
# который мы хотим принять , но не хотим отдавать обратно.
class TaskCreate(TaskBase):
    pass

# 4. Схема для чтения/ответа(task)
# Эту схему мы будем отдавать пользователю (в GET запросе).
class Task(TaskBase):
    # Самое важное: тут появляется ID!
    # При создании (TaskCreate) ID еще нет (его создает база).
    # А при чтении (Task) ID уже есть.
    id:int
    
    # Магическая настройка (для Pydantic v2)
    # Раньше это называлось orm_mode=True
    # Это говорит Pydantic'y: Ну ругайся если подсунут не словарь , а обьект SQLAlchemy
    # Без этого программа упадет с ошиюбкой валидации при попытке вернуть данные из БД
    class Config:
        from_attributes = True
     