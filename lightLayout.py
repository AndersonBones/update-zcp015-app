from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QWidget, QMessageBox, QProgressBar
from PyQt5.uic import loadUi
import sys
from Export import Export_ZCP015
from Base import    Base_ZCP015 
import threading
from time import sleep


class MainWindow(QDialog):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        loadUi('gui.ui', self)

        self.search_file_btn.clicked.connect(self.browsefiles)
        self.run_process_btn.clicked.connect(self.run_thread)
        self.popup_status = False
        
        self.n = 500
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(self.n)
        self.statusRunning = True
    
    def success_msg(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle('Tarefa concluida')
        self.msg.setText('Tarefa concluida com sucesso.')
        #self.msg.setIcon(QMessageBox.SP_DialogApplyButton)
        self.msg.exec_()
        
    def close_success_msg(self):
        self.msg.close()
    
    def browsefiles(self):
        self.file_path = QFileDialog.getOpenFileName(self,'Procurar Arquivo','C:\\TEMP', 'Excel Files (*.xls *.xlsx)')
        self.input_path.setText(self.file_path[0])
    
  
    def run_process(self):
        i = 0
        while self.statusRunning:
            sleep(0.02)
            i+=1
            self.progressBar.setValue(i)

        Export_ZCP015(self.file_path[0]).update()
        self.statusRunning = False
        #Base_ZCP015(self.file_path[0]).start_update()
    
        self.success_msg()
        
    def run_thread(self):
        
        self.thr = threading.Thread(target=self.run_process, daemon=True)
        self.thr.start()
    
        
        
    
def run():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainWindow)
    widget.setFixedWidth(665)
    widget.setFixedHeight(340)
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
