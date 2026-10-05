import sys
from PySide6.QtWidgets import QApplication, QLineEdit, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QObject, Signal

class PasswordMeter(QObject):
    def __init__(self):
        super().__init__()
        self.password_strength_changed = Signal(int)

    def evaluate_password_strength(self, password):
        strength = 0
        if len(password) >= 8:
            strength += 1
        if any(char.isdigit() for char in password):
            strength += 1
        if any(char.isupper() for char in password):
            strength += 1
        if any(char.islower() for char in password):
            strength += 1
        if any(char in "!@#$%^&*()" for char in password):
            strength += 1
        
        label.setText(f"Sila hasla: {strength}/5")

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Miernik sily hasla")

password_meter = PasswordMeter()
entry = QLineEdit(EchoMode=QLineEdit.Password)
label = QLabel("Sila hasla: ")

def on_text_changed(text):
    password_meter.evaluate_password_strength(text)

entry.textChanged.connect(on_text_changed)

layout = QVBoxLayout()
layout.addWidget(entry)
layout.addWidget(label)
window.setLayout(layout)

window.show()
sys.exit(app.exec())