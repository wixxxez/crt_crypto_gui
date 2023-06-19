import sys
from PyQt5.QtWidgets import QApplication,QGraphicsDropShadowEffect, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPalette, QColor 
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chinese remainder theorem")
        self.resize(700, 600)

        main_widget = QWidget(self)
        layout = QVBoxLayout(main_widget)
        button = QPushButton("Click me")

        # Apply box shadow effect to the button
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(50)
        shadow_effect.setColor(QColor(243,165, 80, 100))
        shadow_effect.setOffset(2, -6)
        button.setGraphicsEffect(shadow_effect)

        layout.addWidget(button)
        self.setCentralWidget(main_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
