# product_card.py
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QSizePolicy,
)


class ProductCard(QWidget):
    add_requested = Signal(str, float)

    def __init__(self, name: str, price: float, description: str, parent=None):
        super().__init__(parent)

        self.name = name
        self.price = price

        #układy
        layout = QHBoxLayout(self)
        layout_left = QVBoxLayout()
        layout_right = QVBoxLayout()

        label_name = QLabel(self.name)
        label_description = QLabel(description)
        label_description.setWordWrap(True)

        label_price = QLabel(f"{self.price:.2f} zł")

        self.add_button = QPushButton("Dodaj")
        self.add_button.setSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed
        )

        self.add_button.clicked.connect(
            lambda: self.add_requested.emit(self.name, self.price)
        )

        # Lewa strona
        layout_left.addWidget(label_name)
        layout_left.addWidget(label_description)

        # Prawa strona
        layout_right.addWidget(label_price)
        layout_right.addWidget(self.add_button)

        layout.addLayout(layout_left)
        layout.addLayout(layout_right)