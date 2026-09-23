from PySide6.QtWidgets import QLineEdit, QVBoxLayout, QWidget, QLabel

class LabeledField(QWidget):
    def __init__(self, label_text, parent=None):
        super().__init__(parent)
        self.entry = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(QLabel(label_text))
        layout.addWidget(self.entry)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        
    def set_text(self, text):
        self.entry.setText(text)

    def get_text(self):
        return self.entry.text()