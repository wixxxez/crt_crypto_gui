import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QTabBar, QPushButton, QLineEdit, QLabel, QHBoxLayout, QStylePainter, QStyleOptionTab, QStyle, QProxyStyle, QGraphicsDropShadowEffect, qApp
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import QRect, QPoint, Qt
import CustomTabWidget
import DarkOrangePalette
from Navbar import NavigationBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chinese remainder theorem")
        self.resize(700, 600)
        ## Create components
        
        main_widget = QWidget(self)
        layout = QVBoxLayout(main_widget)
        tab_widget = CustomTabWidget.CustomTabWidget()
        palette = DarkOrangePalette.DarkOrangePalette()
        
        self.nav_layout = NavigationBar(self)
        ## Set relations 
        
        self.setPalette(palette)
        layout.addLayout(self.nav_layout)
        
        layout.addWidget(tab_widget)
        

        self.setCentralWidget(main_widget)
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Set the dark-orange style for the application
    app.setStyle("Fusion")
    palette = DarkOrangePalette.DarkOrangePalette()
    
    app.setStyleSheet("""
      
        #ConfigButton {
            background-color: rgb(236,156,76);
            border-top-left-radius: 5px;
            border-bottom-right-radius: 5px;
            
            width:100%;
            height: 40%;
           
        }
        #ConfigButton:hover {
            background-color: rgb(255,169,82);
        }
        
        #NavBarLabel {
            color:orange;
        }
        #NavBarText {
            color:rgba(255,255,255,0.8);
            border: 2px solid rgb(236,156,76);
            border-top-style: none;
            border-left-style: none;
            border-right-style: none;
            
        }
        #SubmitButton {
            
        }
                """)
    app.setPalette(palette)


    # Apply the shadow effect to the buttons
    
    window = MainWindow()
   
    window.show()

    sys.exit(app.exec())