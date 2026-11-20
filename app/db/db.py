import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = str(os.getenv("DB_PORT", "5432")).strip()
DB_NAME = os.getenv("DB_NAME", "octagon_db")
DB_USER = os.getenv("DB_USER", "octagon")
DB_PASSWORD = os.getenv("DB_PASSWORD", "12345")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_session():
    return SessionLocal()

def init_engine():
    from app.db import models
    Base.metadata.create_all(bind=engine)

def reset_engine():
    from app.db import models
    print("Удаляем старые таблицы...")
    Base.metadata.drop_all(bind=engine)
    print("Создаем новые таблицы...")
    Base.metadata.create_all(bind=engine)
    print("Таблицы успешно созданы!")