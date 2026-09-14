import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QTextEdit, QSplitter, QListWidget

app = QApplication(sys.argv)
spliter = QSplitter(Qt.Orientation.Horizontal)
spliter.setWindowTitle("Splitter Example")

list_widget = QListWidget()
list_widget.addItems(["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"])

spliter.addWidget(list_widget)
spliter.addWidget(QTextEdit())
spliter.setSizes([150, 350])
spliter.resize(500, 300)
spliter.show()

sys.exit(app.exec())