import sys
from PySide6.QtWidgets import QApplication, QLineEdit, QLabel, QVBoxLayout, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Licznik znaków")

def on_text_changed(text):
    count_label.setText(f"Liczba znaków: {len(text)}")


entry = QLineEdit()
count_label = QLabel("Liczba znaków: 0")

entry.textChanged.connect(on_text_changed)

layout = QVBoxLayout()
layout.addWidget(entry)
layout.addWidget(count_label)

window.setLayout(layout)
window.show()
sys.exit(app.exec())