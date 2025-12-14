import os, sys
import PyQt5.QtWidgets as Q

class MainWindow(Q.QMainWindow):
    def __init__(self, op, path, items):
        super().__init__()
        self.__system = op
        self.setWindowTitle("Finder")
        self.setGeometry(500,500,500,500)
    
    @property
    def system(self):
        return self.__system