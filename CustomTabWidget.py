import typing
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QTabBar, QPushButton, QLineEdit, QLabel, QHBoxLayout, QStylePainter, QStyleOptionTab, QStyle, QProxyStyle, qApp
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import QRect, QPoint, Qt
from LayerMainLayout import LayerMainLayout
from VerticalTabBar import VerticalTabWidget
from bs4 import BeautifulSoup

import crt 

class CustomTabWidget(VerticalTabWidget):
    
    def __init__(self, parent) -> None:
        super().__init__()
        self.parent = parent
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
            
    def add_tab(self):
        # Create a new tab and add it to the tab widget
        new_tab = QWidget()
        tab_number = self.count()
        cur_index = self.currentIndex()
        if (cur_index == self.count()-1):
            
            self.addTab(new_tab, f"Layer {tab_number + 1}")
            self.createLayoutForTab(new_tab,tab_number ) 
            
        self.next_tab()
           
    def createLayoutForTab(self,tab, tab_number):
            label = QLabel(f"Layer {tab_number+1}: {tab}")
            label.setAlignment(Qt.AlignCenter)
            prev_tab = self.widget(tab_number-1)
            content = None
            if prev_tab:
                layer = prev_tab.layout().layer
                print(self.parent.keys_per_layer)
                layer, keys = crt.init_layer(layer,self.parent.keys_per_layer )
            else:
                html_string = self.parent.nav_layout.encypted_message_layout.label_bot.text()
                soup = BeautifulSoup(html_string, 'html.parser')
                text = soup.get_text()
                integer_value = int(text)
                
                layer ,keys = crt.init_1_layer(integer_value, self.parent.keys_per_layer)
            
            content = [layer, keys]
            tab1_layout = LayerMainLayout(tab, tab_number+1, self, content)
            
    def next_tab(self):
        cur_index = self.currentIndex()
        if cur_index < len(self)-1:
            self.setCurrentIndex(cur_index+1)

