import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Formularz")

label = QLabel("")
entry = QLineEdit()
entry.setPlaceholderText("Wpisz coś imie...")
button = QPushButton("Wyślij")
button.setStyleSheet("""
    QPushButton {
        background-color: #1a73e8;
        color: white;
        padding: 8px;
        border-radius: 4px;
    }
    QPushButton:hover {
        background-color: #1557b0;
    }
""")

def show_greeting():
    name = entry.text()
    if name:
        label.setText(f"Witaj, {name}!")
    else:
        label.setText("Wpisz swoje imię.")

button.clicked.connect(show_greeting)

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(entry)
layout.addWidget(button)

window.setLayout(layout)
window.resize(300, 150)

window.show()
sys.exit(app.exec())