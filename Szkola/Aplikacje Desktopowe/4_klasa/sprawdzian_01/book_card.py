from PySide6.QtWidgets import QFrame, QGridLayout, QLabel, QPushButton
from PySide6.QtCore import Signal, Slot


class BookCard(QFrame):
    borrow_requested = Signal(str, str)

    def __init__(self, title, author, parent=None):
        super().__init__(parent)
        self.title = title
        self.author = author
        self.setObjectName("bookCard")

        layout = QGridLayout(self)
        title_label = QLabel(title)

        title_label.setObjectName("bookTitle")
        title_label.setWordWrap(True)
        
        layout.addWidget(title_label, 0, 0, 1, 2)

        layout.addWidget(QLabel(author), 1, 0)
        borrow_button = QPushButton("Wypożycz")
        borrow_button.clicked.connect(self.on_borrow_requested)
        layout.addWidget(borrow_button, 1, 1)

    @Slot()
    def on_borrow_requested(self):
        self.borrow_requested.emit(self.title, self.author)
