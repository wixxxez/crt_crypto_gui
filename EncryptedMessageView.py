from PyQt5.QtWidgets import QApplication,QLabel, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QTabBar, QPushButton, QLineEdit, QLabel, QHBoxLayout, QStylePainter, QStyleOptionTab, QStyle, QProxyStyle, QGraphicsDropShadowEffect, qApp
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import QRect, QPoint, Qt
import crt
class NavBarView(QVBoxLayout):
    
    def __init__(self):
        super().__init__()
        
        label = QLabel("<h4><center>Encrypted Message</center></h4>")
        label.setObjectName("NavBarLabel")
        
        self.addWidget(label)
        
        label_bot  = QLabel("<h4> <center> set your message in config window </center> </h4>")
        label_bot.setObjectName("NavBarText")
        self.label_bot = label_bot
        self.addWidget(self.label_bot)

    
    def update_label_bot_text(self, new_text, keys = None):
        text = crt.encrypt_message(new_text)
        self.label_bot.setText(f"<h4><center>{text}</center></h4>")
   