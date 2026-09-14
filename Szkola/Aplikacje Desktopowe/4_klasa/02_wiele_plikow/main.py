import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from main_window import MainWindow

app = QApplication(sys.argv)

window  = MainWindow()

window.show()
sys.exit(app.exec())