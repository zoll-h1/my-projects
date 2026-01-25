# 0. Models - строим Фундамент Таблицы

# 1. Импортируем типы данных SQL
# Обратим внимание это не типы Python(int,str), это типы Базы Данных.
from sqlalchemy import Column, Integer, String, Boolean
# 2. Импортируем нашего предка Base из database.py
from app.database import Base

# Создаем класс , который берет импортированный
class Task(Base):
    # 3. Название таблицы в базе данных
    __tablename__ = "tasks"

    # 4. Колонки (Поля таблицы)

    # id: Уникальный номер. primary_key=True значит "это главный идентификатор"
    id = Column(Integer, primary_key=True, index=True) 

# title : Заголов задачи.
    title = Column(String, index=True)

# description: Описание, nullable=True значит "Может быть пустым

    description = Column(String, nullable=True)

# is_completet: Выполено или нет.
# default=False значит, если мы не скажем иначе, задача считается НЕвыполненной.
    is_completed = Column(Boolean, default=False)
