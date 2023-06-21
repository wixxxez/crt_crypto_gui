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
        
        
class LayerMainLayout(QVBoxLayout):
    
    def __init__(self, parent, i, parent_layout):
        super().__init__(parent)
        
     

        # Create the label with the text "Keys for layer 2:"s
        hbox = QHBoxLayout()
        label1 = QLabel(f'<center>Keys for layer {i}:</center>')
        label1.setStyleSheet("font-size:20px;")
        self.addWidget(label1)
        
        # Create the second label with a bottom orange border
        label2 = QLabel("Keys is ... ")
        label2.setObjectName("LayerNavBarNew")
        label2.setAlignment(Qt.AlignCenter)
        self.label2 = label2
        self.addWidget(self.label2)

        # Create the first text area
        text_area1 = QTextEdit()
        text_area1.setReadOnly(True)
        text_area1.setText("Encrypted text")
        text_area1.setObjectName("TextAreaLayer")
        self.text_area1 = text_area1
        hbox.addWidget(self.text_area1)
        
        
        # Create the button with a right-skewed arrow
        buttond = QPushButton('Decrypt message >' )
        buttond.setObjectName("DecryptButton")
        buttond.clicked.connect(self.decrypt_config)
        # button.setFixedSize(30, 30)  # Set a fixed size for the button
        hbox.addWidget(buttond)

        # Create the second text area
        text_area2 = QTextEdit( )
        text_area2.setReadOnly(True)
        text_area2.setObjectName("TextAreaLayer")
        self.text_area2 = text_area2
        hbox.addWidget(self.text_area2)
        hhbox = QHBoxLayout()
        button = QPushButton("Go to the next layer: ")
        button.clicked.connect(parent_layout.add_tab)
        button.setObjectName("AddLayerButton")
        hhbox.addWidget(button)
        hhbox.addStretch(0.7)
        self.addLayout(hbox)
        self.addLayout(hhbox)
    
    def decrypt_config(self):
        
        self.text_area2.setText("Decrypted text")
        
    def setKeys(self, keys):
        
        self.label2.setText(keys)
        