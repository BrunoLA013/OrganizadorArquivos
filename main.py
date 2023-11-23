import os
import shutil
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from ui_main import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("PYTAx - File Organizer")
        appIcon = QIcon("_imgs/icone.png")
        self.setWindowIcon(appIcon)
        
        self.file = ''
        
        self.btn_open.clicked.connect(self.open_path)
        self.btn_exec.clicked.connect(self.organizador)
                
    def open_path(self):
        
        self.file = QFileDialog.getExistingDirectory(self, str("pasta xml"),
                                                    '/home',
                                                    QFileDialog.ShowDirsOnly |
                                                    QFileDialog.DontResolveSymlinks)
        
        
        self.text_path.setText(self.file)
        self.file = str(self.file)
        
    def organizador(self):
        path = self.file
        files = os.listdir(path)
        
        for file in files:
            filename, extension = os.path.splitext(file)
            extension = extension[1:]
            if os.path.exists(path + '/' + extension):
                shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
            else:
                os.makedirs(path + '/' + extension)
                shutil.move(path + '/' + file, path + '/' + extension)
            
        # Move a exibição da caixa de mensagem para fora do loop
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Arquivos organizados com sucesso!")
        msg.exec()
            
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    app.exec()