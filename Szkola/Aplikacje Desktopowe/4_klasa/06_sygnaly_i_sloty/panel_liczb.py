import sys
from PySide6.QtWidgets import QApplication, QPushButton, QLabel, QHBoxLayout, QWidget, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Panel Liczb")
window.resize(300, 200)

total = 0
total_label = QLabel(f"Suma: 0")

def add_to_total(number):
    global total
    total += number
    total_label.setText(f"Suma: {total}")

buttons_layout = QHBoxLayout()
for numbers in range(1,6):
    button = QPushButton(str(numbers))
    button.clicked.connect(lambda checked, n=numbers: add_to_total(n))
    buttons_layout.addWidget(button)

main_layout = QVBoxLayout()
main_layout.addLayout(buttons_layout)
main_layout.addWidget(total_label)

window.setLayout(main_layout)

window.show()
sys.exit(app.exec())