
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import  QPushButton, QVBoxLayout, QHBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt, QObject, QEvent


class NavBarShadow(QGraphicsDropShadowEffect):
    
    def __init__(self, name ) -> None:
        super().__init__()
        
        self.setBlurRadius(10)
        self.setColor(QColor(0, 0, 0, 100))
        if name == "Close":
            
            self.setOffset(-2, 2)
        else : 
            self.setOffset(2, 2)
        