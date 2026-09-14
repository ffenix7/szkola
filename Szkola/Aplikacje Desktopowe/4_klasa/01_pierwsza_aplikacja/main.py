import sys
from PySide6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Moja pierwsza aplikacja")

window.show()
sys.exit(app.exec())