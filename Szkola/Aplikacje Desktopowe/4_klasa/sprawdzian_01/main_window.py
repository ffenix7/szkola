from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QGridLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton,QScrollArea, QSizePolicy, QSplitter, QTextEdit, QVBoxLayout, QWidget

from book_card import BookCard
from loan_basket import LoanBasket
from rules_dialog import RulesDialog


class MainWindow(QMainWindow):
    loan_confirmed = Signal(int)

    BOOKS = [
        ("Pan Tadeusz", "Adam Mickiewicz", "lektura"),
        ("Lalka", "Bolesław Prus", "lektura"),
        ("Wesele", "Stanisław Wyspiański", "lektura"),
        ("Ferdydurke", "Witold Gombrowicz", "lektura"),
        ("Solaris", "Stanisław Lem", "fantastyka"),
        ("Wiedźmin. Ostatnie życzenie", "Andrzej Sapkowski", "fantastyka"),
        ("Hobbit", "J.R.R. Tolkien", "fantastyka"),
        ("Python. Wprowadzenie", "Mark Lutz", "informatyka"),
        ("Czysty kod", "Robert C. Martin", "informatyka"),
        ("Zrozumieć algorytmy", "Aditya Bhargava", "informatyka"),
    ]

    LIBRARIAN_PIN = "2468"
    LOAN_PERIODS = [7, 14, 30]
    GENRES = ["lektura", "fantastyka", "informatyka"]
    MAX_BOOKS = 3

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Biblioteka szkolna — wypożyczenia")
        self.resize(1000, 680)
        
        self.cards = []
        self.loan_period = 14
        self.rules_dialog = None

        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)

        header_layout = QHBoxLayout()
        self.header_label = QLabel("Biblioteka szkolna")
        self.header_label.setObjectName("headerTitle")

        self.counter_label = QLabel("Wypożyczono dziś: 0")
        
        rules_button = QPushButton("Regulamin")
        rules_button.setObjectName("rulesButton")
        rules_button.clicked.connect(self.show_rules)
        
        header_layout.addWidget(self.header_label)
        header_layout.addWidget(self.counter_label)
        header_layout.addWidget(rules_button)
        
        main_layout.addLayout(header_layout)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Szukaj po tytule lub autorze...")
        self.search_bar.textChanged.connect(self.filter_cards)
        main_layout.addWidget(self.search_bar)

        main_splitter = QSplitter(Qt.Orientation.Vertical)
        main_layout.addWidget(main_splitter)
        main_splitter.addWidget(self.create_shelf())

        lower_splitter = QSplitter(Qt.Orientation.Horizontal)
        lower_splitter.addWidget(self.create_form())
        
        self.cart_text = QTextEdit()
        self.cart_text.setReadOnly(True)
        
        lower_splitter.addWidget(self.cart_text)
        lower_splitter.setSizes([600, 400])
        main_splitter.addWidget(lower_splitter)
        main_splitter.setSizes([350, 300])

        self.messages_label = QLabel("Wybierz książki z listy.")
        main_layout.addWidget(self.messages_label)

        self.basket = LoanBasket(self.MAX_BOOKS, self)
        for card in self.cards:
            card.borrow_requested.connect(self.basket.add)
        
        self.basket.book_added.connect(self.add_book_to_cart)
        self.basket.book_added.connect(self.book_added_message)
        self.basket.count_changed.connect(self.update_count)
        self.basket.count_changed.connect(self.update_confirm_enabled)
        self.basket.rejected.connect(self.show_message)
        self.loan_confirmed.connect(self.update_daily_counter)
        
        self.update_confirm_enabled(0)

    def create_shelf(self):
        shelf = QWidget()
        shelf_layout = QGridLayout(shelf)
        rows = {genre: 1 for genre in self.GENRES}
        
        for column, genre in enumerate(self.GENRES):
            heading = QLabel(genre.capitalize())
            heading.setObjectName("genreHeader")
            
            heading.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            
            shelf_layout.addWidget(heading, 0, column)
        
        for title, author, genre in self.BOOKS:
            column = self.GENRES.index(genre)
            card = BookCard(title, author)
            card.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            
            shelf_layout.addWidget(card, rows[genre], column)
            rows[genre] += 1
            
            self.cards.append(card)
        
        for column in range(len(self.GENRES)):
            shelf_layout.setColumnStretch(column, 1)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(shelf)
        
        return scroll

    def create_form(self):
        form_widget = QWidget()
        form = QGridLayout(form_widget)
        
        form.addWidget(QLabel("Numer karty czytelnika:"), 0, 0)
        
        self.card_number_input = QLineEdit()
        self.card_number_input.setPlaceholderText("4 cyfry, np. 1234")
        
        form.addWidget(self.card_number_input, 0, 1)
        form.addWidget(QLabel("PIN bibliotekarza:"), 0, 2)
        
        self.pin_number_input = QLineEdit()
        self.pin_number_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.pin_number_input.returnPressed.connect(self.confirm_loan)
        
        form.addWidget(self.pin_number_input, 0, 3)
        form.addWidget(QLabel("Okres wypożyczenia:"), 1, 0)
    
        self.period_label = QLabel("14 dni")
        form.addWidget(self.period_label, 1, 1)

        self.teacher_button = QPushButton("Tryb nauczyciela (bez limitu): WYŁ")
        self.teacher_button.setCheckable(True)
        self.teacher_button.clicked.connect(self.toggle_teacher_mode)
        form.addWidget(self.teacher_button, 1, 2, 1, 2)

        periods = QHBoxLayout()
        for days in self.LOAN_PERIODS:
            button = QPushButton(f"{days} dni")
            button.clicked.connect(lambda checked=False, value=days: self.set_loan_period(value))
            
            periods.addWidget(button)

        form.addLayout(periods, 2, 0, 1, 3)

        self.confirm_button = QPushButton("Zatwierdź wypożyczenie")
        self.confirm_button.setObjectName("confirmButton")
        self.confirm_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.confirm_button.clicked.connect(self.confirm_loan)
        
        form.addWidget(self.confirm_button, 2, 3, 2, 1)
        
        form.addWidget(QLabel("W koszyku:"), 3, 0)
        
        self.count_label = QLabel("0 szt.")
        
        form.addWidget(self.count_label, 3, 1)
        
        return form_widget

    @Slot(str)
    def filter_cards(self, text):
        phrase = text.casefold()
        for card in self.cards:
            card.setVisible(not phrase or phrase in card.title.casefold() or phrase in card.author.casefold())

    @Slot(int)
    def set_loan_period(self, days):
        self.loan_period = days
        self.period_label.setText(f"{days} dni")

    @Slot(bool)
    def toggle_teacher_mode(self, checked):
        self.basket.set_unlimited(checked)
        state = "WŁ" if checked else "WYŁ"
        self.teacher_button.setText(f"Tryb nauczyciela (bez limitu): {state}")

    @Slot(str, str)
    def add_book_to_cart(self, title, author):
        self.cart_text.append(f"{title} — {author}")

    @Slot(str, str)
    def book_added_message(self, title, author):
        self.show_message(f"Dodano do koszyka: {title}")

    @Slot(int)
    def update_count(self, count):
        self.count_label.setText(f"{count} szt.")

    @Slot(int)
    def update_confirm_enabled(self, count):
        self.confirm_button.setEnabled(count > 0)

    @Slot(str)
    def show_message(self, message):
        self.messages_label.setText(message)

    @Slot()
    def confirm_loan(self):
        if self.basket.count() == 0:
            self.show_message("Koszyk jest pusty.")
            return
        
        try:
            card_number = int(self.card_number_input.text())
        except ValueError:
            self.show_message("Numer karty musi być liczbą.")
            return
        
        if not 1000 <= card_number <= 9999:
            self.show_message("Numer karty musi mieć 4 cyfry.")
            return
        
        if self.pin_number_input.text() != self.LIBRARIAN_PIN:
            self.show_message("Błędny PIN bibliotekarza!")
            return
        
        count = self.basket.count()
        
        self.cart_text.append(
            f"--- Karta {card_number}: {count} szt., zwrot za {self.loan_period} dni ---"
        )
        
        self.basket.clear()
        self.card_number_input.clear()
        self.pin_number_input.clear()
        
        self.show_message("Wypożyczenie zapisane.")
        self.loan_confirmed.emit(count)

    @Slot(int)
    def update_daily_counter(self, count):
        current = int(self.counter_label.text().rsplit(":", 1)[1].strip())
        self.counter_label.setText(f"Wypożyczono dziś: {current + count}")

    @Slot()
    def show_rules(self):
        if self.rules_dialog is None:
            self.rules_dialog = RulesDialog(self)

        self.rules_dialog.show()
        self.rules_dialog.raise_()
        self.rules_dialog.activateWindow()
