import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QTabBar, QPushButton, QLineEdit, QLabel, QHBoxLayout, QStylePainter, QStyleOptionTab, QStyle, QProxyStyle, qApp
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import QRect, QPoint, Qt
import CustomTabWidget
import DarkOrangePalette

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chinese remainder theorem")
        self.resize(700, 600)
        main_widget = QWidget(self)
        layout = QVBoxLayout(main_widget)
        tab_widget = CustomTabWidget.CustomTabWidget()
        palette = DarkOrangePalette.DarkOrangePalette()
        self.setPalette(palette)
        layout.addWidget(tab_widget)


        self.setCentralWidget(main_widget)
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Set the dark-orange style for the application
    app.setStyle("Fusion")
    palette = DarkOrangePalette.DarkOrangePalette()
    app.setPalette(palette)
    

    window = MainWindow()
    window.show()

    sys.exit(app.exec())