from app.db.db import init_engine
from app.db import crud

def main():
    init_engine()
    cat1 = crud.create_category("Фантастика")
    cat2 = crud.create_category("Детективы")

    crud.create_book("Дюна", "Фантастика", 800, cat1.id)
    crud.create_book("Гиперион", "Космоопера", 750, cat1.id)
    crud.create_book("Убийство в Восточном экспрессе", "Классика", 600, cat2.id)
    crud.create_book("Шерлок Холмс", "Детектив", 900, cat2.id)

    print("База данных заполнена!")

if __name__ == "__main__":
    main()