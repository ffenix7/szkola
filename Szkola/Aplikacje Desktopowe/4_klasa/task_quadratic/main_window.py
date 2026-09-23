from PySide6.QtWidgets import QLineEdit, QVBoxLayout, QWidget, QLabel, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kwadratówka")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label_1 = QLabel("Współczynnik a:")
        self.entry_1 = QLineEdit()

        self.layout.addWidget(self.label_1)
        self.layout.addWidget(self.entry_1)

        self.label_2 = QLabel("Współczynnik b:")
        self.entry_2 = QLineEdit()
        self.layout.addWidget(self.label_2)
        self.layout.addWidget(self.entry_2)

        self.label_3 = QLabel("Współczynnik c:")
        self.entry_3 = QLineEdit()
        self.layout.addWidget(self.label_3)
        self.layout.addWidget(self.entry_3)

        self.button = QPushButton("Oblicz")
        self.button.setStyleSheet("""
            QPushButton{
                background-color: #1144ff;
            }
        """)
        self.button.clicked.connect(self.calculate)
        self.layout.addWidget(self.button)

        self.result_label = QLabel()
        self.layout.addWidget(self.result_label)

    def calculate(self):
        sqrt_delta = (float(self.entry_2.text()) ** 2) - 4 * (float(self.entry_1.text()) * float(self.entry_3.text()))**0.5
        if (sqrt_delta < 0):
            self.result_label.setText("Brak pierwiastków rzeczywistych")
        elif(sqrt_delta == 0):
            x = -float(self.entry_2.text()) / (2 * float(self.entry_1.text()))
            self.result_label.setText(f"Jeden pierwiastek: {x}")
        else:
            x1 = (-float(self.entry_2.text()) - sqrt_delta) / (2 * float(self.entry_1.text()))
            x2 = (-float(self.entry_2.text()) + sqrt_delta) / (2 * float(self.entry_1.text()))
            self.result_label.setText(f"Dwa pierwiastki: x1 = {x1} i x2 = {x2}")