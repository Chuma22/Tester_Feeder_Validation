import random
import sys
from PySide6.QtCore import Qt, QTimer, Slot
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLCDNumber, QLabel,
    QLayout, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QWidget)
from PySide6.QtGui import QTextCharFormat, QFont
from ui.MainWindow import Ui_MainWindow
import time
from concurrent.futures import ThreadPoolExecutor
import DAC

timeCurrent = None

#import qdarktheme
#import qdarkstyle
#import resources.resources
class Application(QMainWindow, Ui_MainWindow):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.timer = QTimer(self)

class CustomApplication():
    """ Custom application definitions. """

    def __init__(self, app_widgets, app=None):
        ''' Constructor method for custom application.'''
        self.app = app
        self.timeCurrent = None
        if app == None:
            self.app = Application()
        self.resultsN =[self.app.resultN1Label,self.app.resultN2Label,
                        self.app.resultN3Label,self.app.resultN4Label,
                        self.app.resultN5Label,self.app.resultN6Label,
                        self.app.resultN7Label,self.app.resultN8Label
                        ]
        self.resultsValidationN =[self.app.resultValidationN1Label,self.app.resultValidationN2Label]
        self.executor = ThreadPoolExecutor(max_workers=15)
        self.running = False
        self.connect_signals()        
        self.app.timer.timeout.connect(self.get_Time)
        self.app.show()

    def connect_signals(self):
            
        self.app.startPushButton.clicked.connect(self.run_Program)
        self.app.stopPushButton.clicked.connect(self.stop_Program)
        
#        self.app.ui.RestartPushButton.clicked.connect(self.se)
        self.app.lower()
        print("connect signals")


    def set_Pass(self):
        for i in self.resultsN:
            i.setStyleSheet("background-color: green")
            i.setText("PASS")
            print("Green",i)

    def set_Fail(self):
        self.app.timer.start(1000)
        for i in self.resultsN:
          print("Red")
          i.setStyleSheet("background-color: red")
          i.setText("Fail")
    
    def get_Time(self):
    # Guarda el tiempo inicial cuando se llama por primera vez
            
        if self.timeCurrent is None:
            self.timeCurrent = time.time()

        timeRealy= time.time()
        timeTmp = int(timeRealy - self.timeCurrent)
        hours = timeTmp // 3600
        minutes = (timeTmp % 3600) // 60
        seconds = timeTmp % 60
        timeText = f"{hours} : {minutes} : {seconds} s"
        
        format = QTextCharFormat()
        format.setFontWeight(QFont.Bold)
        self.app.timeProductionTextBrowser.setCurrentCharFormat(format)
        self.app.timeProductionTextBrowser.setPlainText(timeText)
        self.app.timeProductionTextBrowser.setAlignment(Qt.AlignCenter)
    
    @Slot()
    def run_Program(self):
        if not self.running:
            self.running = True
            self.future = self.executor.submit(DAC.main)
        
        self.set_Pass()
    @Slot()
    def stop_Program(self):
        if self.running and not self.future.done():
            self.running = False
            self.future.cancel()
        self.set_Fail()

   
if __name__ == '__main__':

    app_widgets = QApplication(sys.argv)

    app_root = Application()

    application_window = CustomApplication(app_widgets=app_widgets, app=app_root)

    
    

    app_widgets.exec()