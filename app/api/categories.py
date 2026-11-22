
from fastapi import APIRouter
from app import crud, schemas

router = APIRouter(
    prefix="/categories",
    tags=["Категории"]
)


@router.get("/", response_model=list[schemas.CategoryResponse])
def read_categories():
    return crud.get_all_categories()
