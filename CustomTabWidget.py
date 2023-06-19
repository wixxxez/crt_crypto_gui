import typing
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QTabBar, QPushButton, QLineEdit, QLabel, QHBoxLayout, QStylePainter, QStyleOptionTab, QStyle, QProxyStyle, qApp
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import QRect, QPoint, Qt

from VerticalTabBar import VerticalTabWidget

class CustomTabWidget(VerticalTabWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.createTabs()
        self.createLayouts()
        
    def createTabs(self):
        
        tab1 = QWidget()
        tab2 = QWidget()
        
        self.addTab(tab1, "Layer 1")
        self.addTab(tab2, "Layer 2")
        

    def createLayouts(self):
        for i in range(self.count()):
            tab = self.widget(i)
            self.createLayoutForTab(tab,i)
            
    def createLayoutForTab(self,tab, tab_number):
            label = QLabel(f"Layer {tab_number+1}: {tab}")
            label.setAlignment(Qt.AlignCenter)
            tab1_layout = QVBoxLayout(tab)
            tab1_layout.addWidget(label)