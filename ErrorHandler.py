
from PyQt5.QtWidgets import QPushButton,QMessageBox, QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox


class WarningMessage(QMessageBox):
    
    def __init__(self,title,text):
        super().__init__()
        self.setWindowTitle(title)
        self.setText(text)
        self.setStyleSheet("color: white; ")
        self.exec_()