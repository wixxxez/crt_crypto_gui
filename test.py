import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QTabBar, QPushButton, QLineEdit, QLabel, QHBoxLayout
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import QRect, QPoint, Qt
from PyQt5.QtWidgets import QTabWidget, QTabBar, QStylePainter, QStyleOptionTab, QStyle, QProxyStyle, qApp, \
    QApplication, QWidget

import DarkOrangePalette

class TabBar(QTabBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def tabSizeHint(self, index):
        s = QTabBar.tabSizeHint(self, index)
        if s.width() < s.height():
            s.transpose()
        s.scale(s.width() * 2, s.height() * 2, Qt.KeepAspectRatio)
        return s

    # Make text visible adequately
    def paintEvent(self, event):
        painter = QStylePainter(self)
        style_option = QStyleOptionTab()

        for i in range(self.count()):
            self.initStyleOption(style_option, i)
            painter.drawControl(QStyle.CE_TabBarTabShape, style_option)
            painter.save()

            s = style_option.rect.size()
            s.scale(s.width() * 2, s.height() * 2, Qt.KeepAspectRatio)
            rect = QRect(QPoint(), s)
            rect.moveCenter(style_option.rect.center())
            style_option.rect = rect

            center = self.tabRect(i).center()
            painter.translate(center)
            painter.rotate(90)
            painter.translate(center*-1)
            painter.drawControl(QStyle.CE_TabBarTabLabel, style_option)
            painter.restore()


class VerticalTabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setTabBar(TabBar(self))
        self.setTabPosition(QTabWidget.West)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title and size
        self.setWindowTitle("Chinese remainder theorem")
        self.resize(700, 600)

        # Create the main widget and set its layout
        main_widget = QWidget(self)
        layout = QVBoxLayout(main_widget)
        
        # Create the tab widget
        tab_widget = VerticalTabWidget()
        
        # Add tabs to the tab widget
        tab1 = QWidget()
        tab2 = QWidget()
        label = QLabel("Layer 1")
        label.setAlignment(Qt.AlignCenter)
        tab_widget.addTab(tab1, "Tab 1")
        tab_widget.addTab(tab2, "Tab 2")
        

        # Add the QLineEdit widget to the layout of tab1
        tab1_layout = QVBoxLayout(tab1)
        tab1_layout.addWidget(label)

        # Create the buttons widget
        buttons_widget = QWidget()
        buttons_layout = QHBoxLayout(buttons_widget)
 
       
        # Set the dark-orange style
        palette = DarkOrangePalette.DarkOrangePalette()
        self.setPalette(palette)
        self.tab_widget = tab_widget
        # Add widgets to the layout
        tab_buttons_widget = QWidget()
        tab_buttons_layout = QHBoxLayout(tab_buttons_widget)

        # Create buttons for each tab
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")

        # Add buttons to the tab buttons layout
        tab_buttons_layout.addWidget(button1)
        tab_buttons_layout.addWidget(button2)

        # Create the "Add Tab" button
        add_tab_button = QPushButton("Add Tab")
        add_tab_button.clicked.connect(self.add_tab)

        # Add the tab buttons and "Add Tab" button to the main layout
        layout.addWidget(self.tab_widget)
        layout.addWidget(tab_buttons_widget)
        layout.addWidget(add_tab_button)

        # Set the main widget
        self.setCentralWidget(main_widget)
        
    
        # Set the main widget
        self.setCentralWidget(main_widget)
        
    def add_tab(self):
            new_tab = QWidget()
            tab_count = self.tab_widget.count() + 1
            tab_text = f"Tab {tab_count}"
            self.tab_widget.addTab(new_tab, tab_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyle("Fusion")
    palette = DarkOrangePalette.DarkOrangePalette()
    app.setPalette(palette)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())