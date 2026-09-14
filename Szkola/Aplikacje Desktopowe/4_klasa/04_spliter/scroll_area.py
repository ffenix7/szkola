import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QScrollArea, QVBoxLayout, QWidget

app = QApplication(sys.argv)

content = QWidget()
content_layout = QVBoxLayout(content)

for i in range(1, 31):
    card = QLabel(f"Card {i}")
    card.setStyleSheet("background-color: lightgray; border: 1px solid black; padding: 10px;")
    content_layout.addWidget(card)
content.setLayout(content_layout)

scroll_area = QScrollArea()
scroll_area.setWindowTitle("Scroll Area Example")
scroll_area.setWidget(content)
scroll_area.setWidgetResizable(True)
scroll_area.resize(400, 300)

scroll_area.show()
sys.exit(app.exec())