import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QGridLayout")

grid = QGridLayout()
grid.addWidget(QLabel("Imię:"), 0, 0)
grid.addWidget(QLineEdit(), 0, 1)
grid.addWidget(QLabel("Nazwisko:"), 1, 0)
grid.addWidget(QLineEdit(), 1, 1)

window.setLayout(grid)
window.show()
sys.exit(app.exec())