# 0. Database.py - Сердце проекта 

# 1. Импортируем "Движок" (создает соединение)
from sqlalchemy import create_engine
# 2. Импортируем инстурменты для создания сессий и моделей
from sqlalchemy.orm import sessionmaker, declarative_base


# 3. Адрес нашей базы данных
# sqlite:/// - протокол , ./lifeos.db - файл будет лежать в папке проекта
SQLALCHEMY_DATABASE_URL = "sqlite:///./lifeos.db"

# 4. Создаем движок (Engine)
# Эта "розетка". Она держит постоянную связь с файлом.
# connect_args={"ckeck_same_thread": False} - НУЖНО ТОЛЬКО ДЛЯ SQLite!
# Потому что SQLite по умолчанию запрещает доступ из разных потоков , а FastAPI многопоточный                           
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


# 5. Создаем Фабрику Сессий (Seccion Local)
# Это "станок", который штампует новые сесии для каждого запроса.
# autocommit=False - мы сами будем говорить "Сохрани" , чтобы не накосячить.
# autoflush=False - мы сами будем говорить 'Отправь в базу" , когда готовы.
# bind=engiine - связываем сесси с нашим движком.
SessionLocal = sessionmaker(autocommit=False , autoflush=False, bind=engine)

# 6. Базовый класс (Base)
# Это "генетический предок"
# Все наши модели (Таблицы) будут наследоваться от этого класса : class Task(Base)
# Благодоря этому SQLAlchemy поймет: "Ага, этот класс - это таблица".
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()