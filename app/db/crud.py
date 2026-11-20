from app.db.db import get_session
from app.db.models import Category, Book

def create_category(title: str):
    with get_session() as session:
        cat = Category(title=title)
        session.add(cat)
        session.commit()
        session.refresh(cat)
        return cat

def get_all_categories():
    with get_session() as session:
        return session.query(Category).all()

def create_book(title, description, price, category_id, url=""):
    with get_session() as session:
        book = Book(title=title, description=description, price=price, category_id=category_id, url=url)
        session.add(book)
        session.commit()
        session.refresh(book)
        return book

def get_all_books():
    with get_session() as session:
        return session.query(Book).all()

def get_books_by_category(category_id):
    with get_session() as session:
        return session.query(Book).filter(Book.category_id == category_id).all()