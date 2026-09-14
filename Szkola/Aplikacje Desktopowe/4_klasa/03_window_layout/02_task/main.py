from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Główne okno")
        self.resize(400, 300)
        self.login = QLineEdit()
        self.login.setPlaceholderText("Login")

        self.haslo = QLineEdit()
        self.haslo.setPlaceholderText("Hasło")
        self.haslo.setEchoMode(QLineEdit.EchoMode.Password)

        self.wyslij = QPushButton("Zaloguj")
        self.wynik = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.login)
        layout.addWidget(self.haslo)
        layout.addWidget(self.wyslij)
        layout.addWidget(self.wynik)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)