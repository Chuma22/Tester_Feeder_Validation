from Phidget22.Phidget import *
from Phidget22.Devices.DigitalInput import *
from Phidget22.Devices.DigitalOutput import *
from Phidget22.Devices.Stepper import *
from Phidget22.Devices.Encoder import *
from Phidget22.StepperControlMode import StepperControlMode
from Phidget22.PhidgetException import PhidgetException
from time import sleep
import asyncio
from concurrent.futures import ThreadPoolExecutor

device = "720523"
moveStepper = 6000 * 10
velocity = 25000
stepperTest = Stepper()
stepperTest.setDeviceSerialNumber(int(device))
stepperTest.openWaitForAttachment(1000)
stepperTest.setCurrentLimit(1.8)
stepperTest.setVelocityLimit(velocity)
stepperTest.addPositionOffset(0)
stepperTest.setControlMode(StepperControlMode.CONTROL_MODE_STEP)
stepperTest.setEngaged(True)
positionCurrent = 0
while True:
    while True:
        stepperTest.setTargetPosition(moveStepper)
        print(stepperTest.getPosition())
        if moveStepper <= stepperTest.getPosition():
            positionCurrent = stepperTest.getPosition()
            newMoveStepper = moveStepper-positionCurrent
            break
    while True:
        stepperTest.setTargetPosition(newMoveStepper)
        print(stepperTest.getPosition())
        if 0 >= stepperTest.getPosition():
            positionCurrent = stepperTest.getPosition()
            break
# stepperTest.setTargetPosition(-moveStepper * 10)
# positionCurrent = stepperTest.getPosition()
# print(positionCurrent)

# import sys
# from concurrent.futures import ThreadPoolExecutor
# from PySide6.QtCore import Qt, Slot
# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextBrowser

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setGeometry(100, 100, 400, 300)

#         self.start_button = QPushButton("Iniciar Tarea", self)
#         self.start_button.setGeometry(50, 50, 300, 50)
#         self.start_button.clicked.connect(self.start_task)

#         self.stop_button = QPushButton("Detener Tarea", self)
#         self.stop_button.setGeometry(50, 110, 300, 50)
#         self.stop_button.clicked.connect(self.stop_task)

#         self.text_browser = QTextBrowser(self)
#         self.text_browser.setGeometry(50, 170, 300, 100)

#         self.executor = ThreadPoolExecutor(max_workers=1)
#         self.running = False

#     @Slot()
#     def start_task(self):
#         if not self.running:
#             self.running = True
#             self.future = self.executor.submit(self.my_async_function)

#     @Slot()
#     def stop_task(self):
#         if self.running and not self.future.done():
#             self.running = False
#             self.future.cancel()
#             self.text_browser.append("Tarea detenida")

#     def my_async_function(self):
#         for i in range(10):
#             if not self.running:
#                 self.text_browser.append("Tarea detenida")
#                 return

#             # Simula una operación costosa
#             import time
#             time.sleep(1)
#             self.text_browser.append(f"Tarea en progreso {i + 1}")

#         self.text_browser.append("Tarea completada")
#         self.running = False

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec())