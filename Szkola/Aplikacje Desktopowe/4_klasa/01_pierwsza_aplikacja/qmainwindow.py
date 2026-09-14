import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

app = QApplication(sys.argv)

window = QMainWindow()

window.setWindowTitle("Główne okno")
window.setCentralWidget(QLabel("Witaj w PySide6!"))
window.resize(400, 300)

window.show()
sys.exit(app.exec())