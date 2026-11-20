from app.db import crud

def main():
    print("=== КАТЕГОРИИ И КНИГИ ===")
    for cat in crud.get_all_categories():
        print(f"\n[{cat.id}] {cat.title}:")
        for book in crud.get_books_by_category(cat.id):
            print(f"  - {book.title} ({book.price} руб.)")

if __name__ == "__main__":
    main()