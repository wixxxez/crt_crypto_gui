import plotly.express as px
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

class PlotlyWidget(QtWidgets.QWidget):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.button = QtWidgets.QPushButton("Plot", self)
        self.browser = QtWebEngineWidgets.QWebEngineView(self)
        vlayout = QtWidgets.QVBoxLayout(self)
        vlayout.addWidget(self.button, alignment=QtCore.Qt.AlignHCenter)
        vlayout.addWidget(self.browser)
        self.button.clicked.connect(self.show_graph)
        self.resize(1000,800)
    def show_graph(self):
            df = px.data.tips()
            fig = px.box(df, x="day", y="total_bill", color="smoker")
            fig.update_traces(quartilemethod="linear") # or "inclusive", or "linear" by default
            self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))

app = QtWidgets.QApplication([])
widget = PlotlyWidget()
widget.show()
app.exec()


