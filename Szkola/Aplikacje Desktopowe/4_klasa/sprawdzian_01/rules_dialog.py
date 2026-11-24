from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout


class RulesDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Regulamin biblioteki")

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(
            "1. Oddaj książki w terminie \n"
            "2. Nie zniszcz książki \n"
            "3. Musisz podać poprawny PIN karty"
        ))
        close_button = QPushButton("Zamknij")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)
