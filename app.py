from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QWidget
from PyQt5.uic import loadUi
import sys


class MainWindow(QDialog):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        loadUi('gui.ui', self)
    
        self.search_file_btn.clicked.connect(self.browsefiles)
    # 
    def brousefiles(self):
        self.file_path = QFileDialog.getOpenFileName(self,'Procurar Arquivo')
        self.path.setText(self.file_path[0])
    
    def run(self):
        self.app = QApplication(sys.argv)
        self.mainWindow = MainWindow()
        self.widget = QtWidgets.QStackedWidget()
        self.widget.addWidget(self.mainWindow)
        self.widget.setFixedWidth(500)
        self.widget.setFixedHeight(300)
        self.widget.show()
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    MainWindow().run()