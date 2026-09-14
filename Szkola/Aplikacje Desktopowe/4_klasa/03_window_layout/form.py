import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QVBoxLayout

def show_greeting():
    name = entry.text()
    label.setText(f"Witaj, {name}!" if name else "Wpisz imię!")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Formularz powitalny")
window.resize(400, 200)

label = QLabel("")

entry= QLineEdit()

entry.setPlaceholderText("Wpisz swoje imię")
button = QPushButton("Powitaj mnie!")

layout = QVBoxLayout()
layout.addWidget(entry)
layout.addWidget(button)
window.setLayout(layout)

window.show()
sys.exit(app.exec())