@echo off
cmd /k "cd /d C:\LTS\Tester_Feeder_Validation\virtualenv\Scripts & activate & cd C:\LTS\Tester_Feeder_Validation\source_code\ui & pyside6-uic Mainwindow.ui -o MainWindow.py & cd C:\LTS\Tester_Feeder_Validation\virtualenv\Scripts & activate & cd C:\LTS\Tester_Feeder_Validation\source_code\resources & pyside6-rcc resources.qrc -o resources.py & exit"