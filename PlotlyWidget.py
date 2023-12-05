import plotly.express as px
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
import config

class PlotlyWidget(QtWidgets.QWidget):
    def __init__(self, parent = None) -> None:
        super().__init__()
        self.browser = QtWebEngineWidgets.QWebEngineView(self)
        vlayout = QtWidgets.QVBoxLayout(self)
         
        vlayout.addWidget(self.browser)
        self.show_graph()
        self.resize(1000,800)
    def show_graph(self):
            df = config.dataset
            Layers_to_avoid = df.query('time == "NaN"').Layer.unique()
            df = df.query("Layer not in @Layers_to_avoid")
            df = df.drop_duplicates(['Layer','Type'])
            if len(df.query('Type == "Encrypted time"')) == len(df.query('Type == "Decrypted time"')):
                fig = px.line(df, x="Layer", y="time", color="Type")
                 
                self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))
            else:
                fig = px.line(df.query('Type == "Encrypted time"'), x="Layer", y="time", color="Type")
                
                self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))
            