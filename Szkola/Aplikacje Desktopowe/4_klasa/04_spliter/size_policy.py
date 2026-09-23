import sys 
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSizePolicy, QTextEdit

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QSizePolicy Example")

button = QPushButton("Przycisk o stałym rozmiarze")
button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

text_edit = QTextEdit()
text_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(text_edit)

window.setLayout(layout)
window.resize(350, 250)
window.show()

sys.exit(app.exec())