import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton

app = QApplication(sys.argv)
window = QWidget()

main_layout = QVBoxLayout()

header_layout = QVBoxLayout()
header_layout.addWidget(QLabel("Nagłówek"))
header_layout.addWidget(QPushButton("Ustawienia."))

main_layout.addLayout(header_layout)
main_layout.addWidget(QLabel("Treść"))

window.setLayout(main_layout)
window.show()

sys.exit(app.exec())