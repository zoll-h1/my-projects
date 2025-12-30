from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Ссылка на локальную SQLite базу данных
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# Создаем движок базы данных
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Создаем сессию для взаимодействия с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Базовый класс для наших моделей
Base = declarative_base()