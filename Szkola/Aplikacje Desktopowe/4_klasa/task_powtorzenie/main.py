import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from window import MainWindow

app = QApplication(sys.argv)

window  = MainWindow()
window.move(100, 100)

window.show()
sys.exit(app.exec())