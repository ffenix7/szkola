from PySide6.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget, QLabel, QPushButton
import sys

def result(operation):
    try:
        num1 = float(entry_1.text())
        num2 = float(entry_2.text())
        match operation:
            case 'plus':
                result = num1 + num2
                result_label.setText(f"Wynik: {result}")        
            case 'minus':
                result = num1 - num2
                result_label.setText(f"Wynik: {result}")
            case 'multiply':
                result = num1 * num2
                result_label.setText(f"Wynik: {result}")
            case 'divide':
                if num2 == 0:
                    result_label.setText("Nie można dzielić przez zero!")
                    return
                result = num1 / num2
                result_label.setText(f"Wynik: {result}")
            case _:
                result_label.setText("Podaj obie liczby!")
    except ValueError:
        result_label.setText("Podaj obie liczby!")

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Kalkulator")

layout = QVBoxLayout()
window.setLayout(layout)

entry_1 = QLineEdit()
label_1 = QLabel("Pierwwsza liczba:")

entry_2 = QLineEdit()
label_2 = QLabel("Druga liczba:")

button_plus = QPushButton("Dodaj")
button_minus = QPushButton("Odejmij")
button_multiply = QPushButton("Pomnóż")
button_divide = QPushButton("Podziel")

result_label = QLabel('')

button_plus.clicked.connect(lambda: result('plus'))
button_minus.clicked.connect(lambda: result('minus'))
button_multiply.clicked.connect(lambda: result('multiply'))
button_divide.clicked.connect(lambda: result('divide'))

layout.addWidget(label_1)
layout.addWidget(entry_1)
layout.addWidget(label_2)
layout.addWidget(entry_2)
layout.addWidget(button_plus)
layout.addWidget(button_minus)
layout.addWidget(button_multiply)
layout.addWidget(button_divide)
layout.addWidget(result_label)

window.show()

sys.exit(app.exec())