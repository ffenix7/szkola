from PySide6.QtCore import QObject, Signal, Slot


class Cart(QObject):
    item_added = Signal(str, float)
    total_changed = Signal(float)
    
    def __init__(self):
        super().__init__()
        self.items = []
        self.promotion = False
    
    @Slot(str,float)
    def add(self, name, price):
        self.items.append((name,price))
        self.item_added.emit((name,price))
        
