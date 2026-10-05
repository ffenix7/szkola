import sys

from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import (
    QApplication,
    QDoubleSpinBox,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class TemperaturesSensor(QObject):
    alert = Signal(str)

    def __init__(self, minimum_temperature=18.0, maximum_temperature=25.0):
        super().__init__()
        self.minimum_temperature = minimum_temperature
        self.maximum_temperature = maximum_temperature

    def check_temperature(self, temperature):
        if not self.minimum_temperature <= temperature <= self.maximum_temperature:
            message = (
                f"Alert: temperatura {temperature:.1f}°C jest poza bezpiecznym "
                f"zakresem {self.minimum_temperature:.1f}-{self.maximum_temperature:.1f}°C."
            )
            self.alert.emit(message)

@Slot(str)
def aktualizuj_etykiete(message):
    etykieta_alertu.setText(message)


@Slot(str)
def dopisz_do_logu(message):
    log_alertow.append(message)


def main():
    global etykieta_alertu, log_alertow

    app = QApplication(sys.argv)
    okno = QWidget()
    okno.setWindowTitle("Czujnik temperatury")

    czujnik = TemperaturesSensor()
    temperatura = QDoubleSpinBox()
    temperatura.setRange(-50.0, 60.0)
    temperatura.setValue(21.0)
    temperatura.setSuffix(" °C")
    przycisk = QPushButton("Sprawdź temperaturę")
    etykieta_alertu = QLabel("Brak alertów")
    log_alertow = QTextEdit()
    log_alertow.setReadOnly(True)

    czujnik.alert.connect(aktualizuj_etykiete)
    czujnik.alert.connect(dopisz_do_logu)
    przycisk.clicked.connect(
        lambda: czujnik.check_temperature(temperatura.value())
    )

    layout = QVBoxLayout(okno)
    layout.addWidget(QLabel("Temperatura (bezpieczny zakres: 18-25 °C):"))
    layout.addWidget(temperatura)
    layout.addWidget(przycisk)
    layout.addWidget(etykieta_alertu)
    layout.addWidget(log_alertow)

    okno.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()