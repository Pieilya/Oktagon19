
from fastapi import APIRouter
from app import crud, schemas

router = APIRouter(
    prefix="/books",
    tags=["Книги"]
)


@router.get("/", response_model=list[schemas.BookResponse])
def read_books():
    return crud.get_all_books()


@router.get("/category/{category_id}")
def read_books_by_category(category_id: int):
    return crud.get_books_by_category(category_id)


@router.post("/", response_model=schemas.BookResponse)
def create_new_book(book: schemas.BookCreate):
    return crud.create_book(
        title=book.title,
        description=book.description,
        price=book.price,
        category_id=book.category_id,
        url=book.url
    )
