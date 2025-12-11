import os, sys
import PyQt5.QtWidgets as Q

class MainWindow(Q.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finder")
        self.setGeometry(500,500,500,500)