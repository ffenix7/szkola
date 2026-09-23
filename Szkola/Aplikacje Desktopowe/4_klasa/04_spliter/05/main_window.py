import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from labeled_field import LabeledField

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rejestracja")
        self.resize(400, 300)

        self.first_name_field = LabeledField("Imię:")
        self.last_name_field = LabeledField("Nazwisko:")
        self.email_field = LabeledField("Email:")

        self.register_button = QPushButton("Zarejestruj")
        self.register_button.setStyleSheet("""
        QPushButton {
            background-color: #4CAF50;
            color: white;
            padding: 8px;
            border-radius: 10px;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
""")


        self.result_label = QLabel()
        layout = QVBoxLayout()
        layout.addWidget(self.first_name_field)
        layout.addWidget(self.last_name_field)    
        layout.addWidget(self.email_field)
        layout.addWidget(self.register_button)
        layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(layout)

        window_layout = QVBoxLayout()
        window_layout.addWidget(container)
        self.setLayout(window_layout)
        self.register_button.clicked.connect(self.register)

    def register(self):
        first_name = self.first_name_field.get_text()
        last_name = self.last_name_field.get_text()
        email = self.email_field.get_text()

        self.result_label.setText(f"Zarejestrowano: {first_name} {last_name}, Email: {email}")