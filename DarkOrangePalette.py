from PyQt5.QtGui import QPalette, QColor 

class DarkOrangePalette(QPalette):
   
   def __init__(self)-> None:
        super().__init__()
        self.setColor(QPalette.Window, QColor(51, 51, 51))
        self.setColor(QPalette.Button, QColor(255, 128, 0))
        self.setColor(QPalette.ButtonText, QColor(25, 25, 25))
        self.setColor(QPalette.Base, QColor(25, 25, 25))
        self.setColor(QPalette.AlternateBase, QColor(51, 51, 51))

