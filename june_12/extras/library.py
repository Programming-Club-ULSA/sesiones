from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Book:
    book_id: int
    title: str
    author: str

    def __str__(self):
        return f"{self.title} by {self.author}"
    
@dataclass
class Loan:
    books: list[Book]
    return_date: datetime
    loan_date: datetime = field(default_factory=datetime.now)

@dataclass
class InventoryItem:
    book: Book
    quantity: int

@dataclass
class Library:
    inventory: list[InventoryItem]

    def show_items(self):
        print("Los libros en inventario son: ")
        for item in self.inventory:
            print(f"{item.quantity} copias de {item.book}")
        
        print("\n")

    def find_item(self, book: Book) -> InventoryItem | None:
        for item in self.inventory:
            if item.book.book_id == book.book_id:
                return item
        return None

    def is_available(self, book: Book) -> bool:
        item = self.find_item(book)

        if item is None:
            return False

        return item.quantity > 0

    def borrow(
        self,
        books: list[Book],
        return_date: datetime
    ) -> Loan:

        borrowed_books = []

        for book in books:
            item = self.find_item(book)

            if item and item.quantity > 0:
                item.quantity -= 1
                borrowed_books.append(book)

        return Loan(
            books=borrowed_books,
            return_date=return_date
        )
    

inventory = [
    InventoryItem(
        Book(1, "Clean Code", "Robert Martin"),
        3
    ),
    InventoryItem(
        Book(2, "The Pragmatic Programmer", "Andrew Hunt"),
        2
    )
]

library = Library(inventory)

library.show_items()

loan = library.borrow(
    [
        Book(1, "Clean Code", "Robert Martin")
    ],
    datetime.today()
)


library.show_items()