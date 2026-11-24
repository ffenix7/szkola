import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow

app = QApplication(sys.argv)
app.setStyleSheet("""
    QPushButton {
        background-color: #4CAF50;
        color: white;
        padding: 5px;
    }
    
    QPushButton:hover { 
        background-color: #45a049;
        
    }

    QPushButton:checked {
        background-color: #1976D2; 
    }

    QPushButton:disabled {
        background-color: #cccccc;
        color: #666666;
    }

    QLabel#headerTitle { 
        font-size: 18px;
        font-weight: bold; 
    }
    
    QLabel#genreHeader {
        background-color: #27cab3;
        color: white;
        font-weight: bold;
        padding: 5px;
    }

    QFrame#bookCard {
        background-color: white;
        border: 1px solid #d0d0d0;
        border-radius: 5px;
        padding: 5px;
    }

    QFrame#bookCard QLabel {
        color: black; 
    }
""")

window = MainWindow()
window.show()


sys.exit(app.exec())