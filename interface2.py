from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QWidget, QMessageBox
from PyQt5.uic import loadUi
import sys
from Export import Export_ZCP015
from Base import    Base_ZCP015 
import threading


class MainWindow(QDialog):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        loadUi('gui.ui', self)

        self.search_file_btn.clicked.connect(self.browsefiles)
        self.run_process_btn.clicked.connect(self.run_thread)
        self.popup_status = False
    
    def success_msg(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle('Tarefa concluida')
        self.msg.setText('Tarefa concluida com sucesso.')
        #self.msg.setIcon(QMessageBox.SP_DialogApplyButton)
        self.msg.exec_()
        
    def close_success_msg(self):
        self.msg.close()
    
    def browsefiles(self):
        self.file_path = QFileDialog.getOpenFileName(self,'Procurar Arquivo','./', 'Excel Files (*.xls *.xlsx)')
        self.input_path.setText(self.file_path[0])
    
    def run_thread(self):
        if not self.popup_status:
            self.thr = threading.Thread(target=self.run_process, daemon=True)
            self.thr.start()
    
    def run_process(self):
        
        Export_ZCP015(self.file_path[0]).update()
        #Base_ZCP015(self.file_path[0]).start_update()
        self.popup_status = True
        
        if self.popup_status:
            self.success_msg()
            self.popup_status = False
        
        
        
    
def run():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainWindow)
    widget.setFixedWidth(665)
    widget.setFixedHeight(300)
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
