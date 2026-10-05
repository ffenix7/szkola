from PySide6.QtCore import QObject, Signal


class Cart(QObject):
    def __init__(self):
        super().__init__()
        

    item_added = Signal(str, float)
    total_changed = Signal(float)