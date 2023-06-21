import sys
from PyQt5.QtWidgets import QApplication,QVBoxLayout, QWidget, QHBoxLayout, QTextEdit, QPushButton, QLabel
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtCore import Qt

class BottomBorderLabel(QLabel):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor("orange"), 2, Qt.SolidLine))
        painter.drawLine(0, self.height() - 2, self.width(), self.height() - 2)
        super().paintEvent(event)

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout(self)
        
        hbox = QHBoxLayout(self)

        # Create the label with the text "Keys for layer 2:"
        label1 = QLabel('Keys for layer 2:', self)
        vbox.addWidget(label1)
        
        # Create the second label with a bottom orange border
        label2 = BottomBorderLabel(self)
        label2.setStyleSheet("border-bottom: 2px solid orange;")
        vbox.addWidget(label2)

        # Create the first text area
        text_area1 = QTextEdit(self)
        text_area1.setReadOnly(True)
        hbox.addWidget(text_area1)

        # Create the button with a right-skewed arrow
        button = QPushButton('>', self)
        button.setFixedSize(30, 30)  # Set a fixed size for the button
        hbox.addWidget(button)

        # Create the second text area
        text_area2 = QTextEdit(self)
        text_area2.setReadOnly(True)
        hbox.addWidget(text_area2)
        vbox.addLayout(hbox)
        button = QPushButton("Go to the next layer: ")
        hhbox = QHBoxLayout(self)
        hhbox.addWidget(button)
        hhbox.addStretch(1)
        vbox.addLayout(hhbox)
        self.setLayout(hbox)
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('QHBoxView Example')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())
