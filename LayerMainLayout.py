import sys
from PyQt5.QtWidgets import QApplication, QScrollArea, QLineEdit,QVBoxLayout, QWidget, QHBoxLayout, QTextEdit, QPushButton, QLabel
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtCore import Qt
import numpy as np
import crt
from ErrorHandler import WarningMessage

class BottomBorderLabel(QLabel):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor("orange"), 2, Qt.SolidLine))
        painter.drawLine(0, self.height() - 2, self.width(), self.height() - 2)
        super().paintEvent(event)
        
        
class LayerMainLayout(QVBoxLayout):
    
    def __init__(self, parent, i, parent_layout, content=None):
        super().__init__(parent)
        # Create the label with the text "Keys for layer 2:"s
        hbox = QHBoxLayout()
        
        label1 = QLabel(f'<center>Keys for layer {i}:</center>')
        label1.setStyleSheet("font-size:20px;")
        self.addWidget(label1)
        self.keys = None
        self.layer = None
        if content:
            self.layer = content[0]
            self.keys = content[1]
        # Create the second label with a bottom orange border
        
        label2 = QLineEdit()
        label2.setReadOnly(True)
        label2.setText(f" {self.keys} ")
        label2.setObjectName("LayerNavBarNew")
        label2.setAlignment(Qt.AlignCenter)
        self.label2 = label2
        self.addWidget(self.label2)

        vvbox = QVBoxLayout()
        # Create the first text area
        label_encr = QLabel("Encrypted values:")
        label_encr.setObjectName("LayerLabel")
        text_area1 = QTextEdit()
        text_area1.setReadOnly(True)
        text_area1.setText(f"{self.layer}")
        text_area1.setObjectName("TextAreaLayer")
        self.text_area1 = text_area1 
        vvbox.addWidget(label_encr)
        vvbox.addWidget(self.text_area1)
        hbox.addLayout(vvbox)
        
        # Create the button with a right-skewed arrow
        buttond = QPushButton('Decrypt message >' )
        buttond.setObjectName("DecryptButton")
        buttond.clicked.connect(self.decrypt_config)
        # button.setFixedSize(30, 30)  # Set a fixed size for the button
        hbox.addWidget(buttond)

        # Create the second text area
        vv2box = QVBoxLayout()
        label_dec = QLabel("Decrypted values:")
        label_dec.setObjectName("LayerLabel")
        text_area2 = QTextEdit( )
        text_area2.setReadOnly(True)
        text_area2.setObjectName("TextAreaLayer")
        self.text_area2 = text_area2
        vv2box.addWidget(label_dec)
        vv2box.addWidget(self.text_area2)
        hbox.addLayout(vv2box)
        hhbox = QHBoxLayout()
        button = QPushButton("Go to the next layer: ")
        button.clicked.connect(parent_layout.add_tab)
        button.setObjectName("AddLayerButton")
        hhbox.addWidget(button)
        hhbox.addStretch(1)
        self.addLayout(hbox)
        self.addLayout(hhbox)
    
    def decrypt_config(self):
        integers = []
        for i in self.layer : 
            integers.append(int(i))
        
        integers = np.array(integers).reshape(-1, len(self.keys))
        prev_layer = []
        print("Keys", self.keys)
        print(integers)
        try:
            for i in integers:
                
                prev_layer_value = crt.chinese_remainder_theorem(self.keys, i.tolist())
                prev_layer.append(prev_layer_value)
        except ValueError as e :
            WarningMessage("Error",f"{e}")
        
        self.text_area2.setText(f"{prev_layer}")
        
    def setKeys(self, keys):
        
        self.label2.setText(keys)
        