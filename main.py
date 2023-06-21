import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QTabBar, QPushButton, QLineEdit, QLabel, QHBoxLayout, QStylePainter, QStyleOptionTab, QStyle, QProxyStyle, QGraphicsDropShadowEffect, qApp
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import QRect, QPoint, Qt
import CustomTabWidget
import DarkOrangePalette
from Navbar import NavigationBar
from LayerMainLayout import LayerMainLayout
from ConfigDialog import ConfigDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        dialog = ConfigDialog(self.initUI)
        dialog.exec_()
        
    def initUI(self, text = None, keys_per_layer = None):
        self.setWindowTitle("Chinese remainder theorem")
        self.resize(1000, 800)
        ## Create components
        
        self.keys_per_layer = keys_per_layer
        main_widget = QWidget(self)
        layout = QVBoxLayout(main_widget)
        self.nav_layout = NavigationBar(self)
        self.nav_layout.encypted_message_layout.update_label_bot_text(text,keys_per_layer)
        tab_widget = CustomTabWidget.CustomTabWidget(self)
        palette = DarkOrangePalette.DarkOrangePalette()
        
        
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
        #AddLayerButton {
            background-color: rgb(255,169,82);
            border: 1px solid black;
            border-top-left-radius: 10px;
            border-bottom-right-radius:10px;
            padding:10px;
            width:120%;
            height: 40%;
           
        }
        #AddLayerButton:hover {
            background-color: rgb(236,156,76);
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
        #TextAreaLayer {
            color: white;
        }
        #DecryptButton {
            background-color: rgb(51, 51, 51);
            border : 1px solid white;
            border-top-left-radius: 10px;
            border-bottom-right-radius: 10px;
            color:white;
            width:120%;
            height:50%
        }
        #DecryptButton:hover{
            background-color: grey;
        }
        #LayerNavBarNew {
            font-size:18px;
            padding-bottom:10px;
            background-color:rgb(255,169,82);
            border: none;
        }
        
                """)
    app.setPalette(palette)


    # Apply the shadow effect to the buttons
    
    window = MainWindow()
   
    window.show()

    sys.exit(app.exec())