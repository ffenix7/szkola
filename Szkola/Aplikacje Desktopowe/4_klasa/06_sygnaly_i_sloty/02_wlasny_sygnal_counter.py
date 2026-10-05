import sys
from PySide6.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Signal, QObject

class Counter(QObject):
    value_changed = Signal(int)

    def __init__(self):
        super().__init__()
        self._value = 0

    def increment(self):
        self._value += 1
        self.value_changed.emit(self._value)

    def decrement(self):
        self._value -= 1
        self.value_changed.emit(self._value)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Counter - custom signal")
window.resize(300, 200)

counter = Counter()
button = QPushButton("+1")
button_minus = QPushButton("-1")
label = QLabel("Liczba znaków: 0")



def on_value_changed(value):
    label.setText(f"Liczba znaków: {value}")

button.clicked.connect(counter.increment)
button_minus.clicked.connect(counter.decrement)
counter.value_changed.connect(on_value_changed)
layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(button_minus)
layout.addWidget(label)
window.setLayout(layout)

window.show()
sys.exit(app.exec())