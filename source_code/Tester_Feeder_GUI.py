import random
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow 
from ui.MainWindow import Ui_MainWindow


#import qdarktheme
#import qdarkstyle
#import resources.resources
class Application(QMainWindow, Ui_MainWindow):
  def __init__(self):
    super().__init__()
    self.setupUi(self)


class CustomApplication():
    """ Custom application definitions. """

    def __init__(self, app_widgets, app=None):
        ''' Constructor method for custom application.'''
        self.app = app
        if app == None:
            self.app = Application()
        self.resultsN =[self.app.resultN1Label,self.app.resultN2Label,
                        self.app.resultN3Label,self.app.resultN4Label,
                        self.app.resultN5Label,self.app.resultN6Label,
                        self.app.resultN7Label,self.app.resultN8Label
                        ]
        self.resultsValidationN =[self.app.resultValidationN1Label,self.app.resultValidationN2Label]

        self.connect_signals()
        self.app.show()

    def connect_signals(self):
            
        self.app.startPushButton.clicked.connect(self.set_Pass)
        self.app.stopPushButton.clicked.connect(self.set_Fail)
#        self.app.ui.RestartPushButton.clicked.connect(self.se)
        self.app.lower()
        print("connect signals")


    def set_Pass(self):
        for i in self.resultsN:
            i.setStyleSheet("background-color: green")
            i.setText("PASS")
            print("Green",i)

    def set_Fail(self):
        for i in self.resultsN:
          print("Red")
          i.setStyleSheet("background-color: red")
          i.setText("Fail")


   
if __name__ == '__main__':

    app_widgets = QApplication(sys.argv)

    app_root = Application()

    application_window = CustomApplication(app_widgets=app_widgets, app=app_root)

    app_widgets.exec()