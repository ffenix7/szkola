from PySide6.QtCore import QObject, Signal, Slot

class LoanBasket(QObject):
    book_added = Signal(str, str)
    count_changed = Signal(int)
    rejected = Signal(str)

    def __init__(self, max_books, parent=None):
        super().__init__(parent)
        self.max_books = max_books
        self.books = []
        self.unlimited = False

    @Slot(str, str)
    def add(self, title, author):
        book = (title, author)

        if book in self.books:
            self.rejected.emit(f"„{title}” jest już w koszyku.")
            return
        
        if not self.unlimited and len(self.books) >= self.max_books:
            self.rejected.emit(
                f"Limit: najwyżej {self.max_books} książki naraz."
            )
            return
        
        self.books.append(book)
        self.book_added.emit(title, author)
        self.count_changed.emit(len(self.books))

    def clear(self):
        self.books.clear()
        self.count_changed.emit(0)

    def count(self):
        return len(self.books)

    def set_unlimited(self, enabled):
        self.unlimited = enabled