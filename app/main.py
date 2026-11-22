from fastapi import FastAPI
from app.api import books, categories

app = FastAPI(
    title="Bookstore API",
    description="API для работы с книгами и категориями",
    version="1.0.0"
)

# Подключаем роутеры
app.include_router(categories.router)
app.include_router(books.router)

# Эндпоинт для проверки, что сервис жив
@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok", "message": "API is running"}