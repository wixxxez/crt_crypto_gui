
from PyQt5.QtWidgets import  QPushButton, QLabel,QVBoxLayout, QHBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt, QObject, QEvent
from ConfigDialog import ConfigDialog
from DarkOrangePalette import DarkOrangePalette
from ShadowEffect import NavBarShadow
from EncryptedMessageView import NavBarView
class NavBarButton(QPushButton):
    def __init__(self, name, callback):
        QPushButton.__init__(self, name)
        self.clicked.connect(callback)
        self.setMouseTracking(True)
        self.setObjectName("ConfigButton") 
        self.setAutoFillBackground(True)
        self.setPalette(DarkOrangePalette())
        shadow_effect = NavBarShadow(name)
        self.shadow_effect = shadow_effect
        self.setGraphicsEffect(self.shadow_effect)
        
    def event(self, event):
        if event.type() == QEvent.HoverEnter:
            self.hoverEnterEvent(event)
        elif event.type() == QEvent.HoverLeave:
            self.hoverLeaveEvent(event)

        return super().event(event)

    def hoverEnterEvent(self, event):
        self.shadow_effect.setColor(QColor(0,162, 232, 100))  # Adjust the shadow color for hover effect

    def hoverLeaveEvent(self, event):
        self.shadow_effect.setColor(QColor(0, 0, 0, 100))  # Reset the shadow color

        
class NavigationBar(QHBoxLayout):
    def __init__(self, main_layout):
        super().__init__()

        self.setObjectName("NavBar")
        palette = DarkOrangePalette()
        # Create the "Config" button
        self.parent_l = main_layout
        config_button = NavBarButton("Config",self.open_config_dialog)
        self.config_button = config_button
        self.addWidget(self.config_button)
        self.encypted_message_layout = NavBarView()
        self.addStretch(1)
        self.addLayout(self.encypted_message_layout)
        self.addStretch(1)
        close_button = NavBarButton("Close",main_layout.close)
    
        self.close_button = close_button
        self.addWidget(self.close_button)
        
    def open_config_dialog(self):
        dialog = ConfigDialog(self.parent_l.initUI)
        dialog.exec_()