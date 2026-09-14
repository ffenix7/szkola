import sys
from PySide6.QtWidgets import QApplication
from main import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.setWindowTitle("Logowanie")
window.resize(300, 200)

def send():    
    if not window.login.text() or not window.haslo.text():
        window.wynik.setText("Wypełnij oba pola!")
    else:
        window.wynik.setText(f"Zalogowano jako {window.login.text()}")

window.wyslij.clicked.connect(send)

window.show()

sys.exit(app.exec())