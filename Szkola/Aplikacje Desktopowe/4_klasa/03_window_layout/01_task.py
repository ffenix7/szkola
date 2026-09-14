import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QVBoxLayout

def show_email_name():
    user_name = name.text()
    user_email = email.text()
    label.setText(f"{user_name} <{user_email}>" if user_name and user_email else "Wpisz imię i email!")

app = QApplication(sys.argv)
window = QWidget()
window.resize(600, 400)

main_layout = QVBoxLayout()

name = QLineEdit()
name.setPlaceholderText("Wpisz swoje imię")

email = QLineEdit()
email.setPlaceholderText("Wpisz swój email")

label = QLabel('')

button = QPushButton("Pokaż dane")
button.clicked.connect(show_email_name)

main_layout.addWidget(name)
main_layout.addWidget(email)
main_layout.addWidget(button)
main_layout.addWidget(label)
window.setLayout(main_layout)

window.show()
sys.exit(app.exec())