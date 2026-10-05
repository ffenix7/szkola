from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit

class LabeledField(QWidget):
    def __init__(self, label_text, placeholder="", password=False, parent=None):
        super().__init__()
        layout = QVBoxLayout()
        text_label = QLabel(label_text)
        if password:
            self.entry = QLineEdit(EchoMode=QLineEdit.Password)
        else:
            self.entry = QLineEdit()
        self.entry.setPlaceholderText(placeholder)

        layout.addWidget(text_label)
        layout.addWidget(self.entry)

        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)

    def text(self):
        return self.entry.text()
    
    def clear(self):
        self.entry.setText("")