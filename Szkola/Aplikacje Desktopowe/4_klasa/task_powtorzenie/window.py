from product_card import ProductCard
from labeled_field import LabeledField
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QSplitter,
    QVBoxLayout,
    QWidget,
    QTextEdit,
    QGridLayout
)
from PySide6.QtGui import QIcon



class MainWindow(QMainWindow):
    def __init__(self):
        self.PRODUCTS = [
            ("Drożdżówka z serem", 3.50, "Świeża, z piekarni obok szkoły"),
            ("Kanapka z szynką", 6.00, "Pieczywo pełnoziarniste, sałata, pomidor"),
            ("Kanapka wege", 6.50, "Hummus, ogórek, papryka"),
            ("Pizzerinka", 5.50, "Z serem i pieczarkami"),
            ("Woda mineralna 0,5 l", 2.50, "Niegazowana"),
            ("Sok jabłkowy", 3.00, "Karton 0,33 l"),
            ("Herbata w kubku", 2.00, "Czarna lub owocowa"),
            ("Baton zbożowy", 2.80, "Owies, miód, żurawina"),
            ("Jabłko", 1.50, "Z sadu pod Grójcem"),
            ("Zeszyt A5 w kratkę", 4.00, "60 kartek"),
            ("Długopis żelowy", 3.20, "Niebieski"),
            ("Korektor w taśmie", 7.50, "Szerokość 5 mm"),
        ]

        self.QUICK_AMOUNTS = [5, 10, 20, 50]

        super().__init__()
        self.setWindowTitle("Sklepik szkolny")
        self.resize(950, 620)
        self.windowIcon = QIcon("./icon.svg")

        central_widget = QWidget()
        main_layout = QVBoxLayout()

        #Header
        header_layout = QHBoxLayout()
        label_title = QLabel("Sklepik szkolny")
        header_layout.addWidget(label_title)

        label_turonover = QLabel("Utarg dzisiaj: 0zł")
        header_layout.addWidget(label_turonover)

        button_info = QPushButton("O programie")
        header_layout.addWidget(button_info)

        main_layout.addLayout(header_layout)

        #Search bar
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Szukaj produktu...")
        main_layout.addWidget(search_bar)

        products_widget = QWidget()
        products_layout = QVBoxLayout()

        for product in self.PRODUCTS:
            products_layout.addWidget(ProductCard(product[0], product[1], product[2]))

        products_layout.addStretch()
        
        products_widget.setLayout(products_layout)

        scroll_area = QScrollArea()

        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(products_widget)

        main_splitter = QSplitter(Qt.Orientation.Horizontal)
        
        main_splitter.addWidget(scroll_area)

        payment_widget = self.create_payment_panel()
        main_splitter.addWidget(payment_widget)

        main_splitter.setSizes([450, 250])

        main_layout.addWidget(main_splitter)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def create_payment_panel(self):
        payment_widget = QWidget()
        payment_layout = QVBoxLayout(payment_widget)

        receipt = QTextEdit(readOnly=True)
        receipt.setPlaceholderText("Paragon jest pusty")

        self.customer_field = LabeledField("Kupujący (opcjonalnie)", "Kamil Pawłowski")
        self.pin_field = LabeledField("Pin sprzedawcy", "", True)

        grid_layout = QGridLayout()
        grid_layout.addWidget(QLabel("Do zapłaty"), 0, 0)
        self.total_label = QLabel("0,00 zł")
        grid_layout.addWidget(self.total_label, 0, 1)
        grid_layout.addWidget(QLabel("W koszyku"), 1, 0)
        self.count_label = QLabel("0 produktów")
        grid_layout.addWidget(self.count_label, 1, 1)
        self.discount_button = QPushButton("Promocja -10%: WYŁ")
        grid_layout.addWidget(self.discount_button, 4, 0, 1, 2)
        grid_layout.addWidget(QLabel("Reszta: "), 5, 0)
        self.change_label = QLabel("-")
        grid_layout.addWidget(self.change_label, 5, 1)
        self.pay_button = QPushButton("Zatwierdź sprzedaż")
        grid_layout.addWidget(self.pay_button, 6, 0, 1, 2)
        self.clear_button = QPushButton("Wyczyść koszyk")
        grid_layout.addWidget(self.clear_button, 7, 0, 1, 2)

        fast_buttons_layout = QHBoxLayout()

        for amount in self.QUICK_AMOUNTS:
            fast_buttons_layout.addWidget(QPushButton(f"{amount} zł"))

        grid_layout.addLayout(fast_buttons_layout, 2, 0, 1, 2)

        payment_details = QWidget()
        payment_details_layout = QVBoxLayout(payment_details)
        payment_details_layout.setContentsMargins(0, 0, 0, 0)
        payment_details_layout.addWidget(self.customer_field)
        payment_details_layout.addWidget(self.pin_field)
        payment_details_layout.addLayout(grid_layout)

        vertical_splitter = QSplitter(Qt.Orientation.Vertical)
        vertical_splitter.addWidget(receipt)
        vertical_splitter.addWidget(payment_details)
        vertical_splitter.setSizes([300, 220])

        payment_layout.addWidget(vertical_splitter)

        return payment_widget