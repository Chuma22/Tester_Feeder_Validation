from Phidget22.Phidget import *
from Phidget22.Devices.DigitalInput import *
from Phidget22.Devices.DigitalOutput import *
from Phidget22.Devices.Stepper import *
from Phidget22.Devices.Encoder import *
from Phidget22.StepperControlMode import StepperControlMode
from Phidget22.PhidgetException import PhidgetException
from time import sleep
import asyncio
import concurrent.futures

phidgetsDAC = {
    "DAC01" : {
        "equimentName": "",
        "serialNumber": "",
        "DI00PickupGrepper": "",
        "DI01Pass": "",
        "DI02Fail": "",
        "DI03GripperOpen": "",
        "DI04GripperClose": "",
        "DI05HomeHorizontal": "",
        "DI06HomeVertical": "",
        "DI07ConveyotInt": "",
        "DI08PickupGripper2": "",
        "DI09Pass": "",
        "DI10Fail": "",
        "DI11GripperOpen2": "",
        "DI12GripperClose2": "",
        "DI13HomeHorizontal2": "",
        "DI14HomeVertical2": "",
        "DI15ConveyorInt2": "",
        "equimentName": "",
        "equimentName": "",
        

    },
    "DAC02" : {

    },
    "DAC03" : {

    },
    "DAC04" : {

    },    
}

devicesSerialNumbersTester = {
        "MOD": "TESTER",
        "Phidget1012_Control_01": "692538",
        "Phidget1012_Control_02": "692440",
        "Phidget1012_Securitas_03": "692552",
        "Phidgets1047_Encoder_01": "590369",
        "Phidgets1067_Stepper_Riel_01": "720437",
        "Phidgets1067_Stepper_Vertical_01": "720489",
        "Phidgets1067_Stepper_Riel_02": "720464",
        "Phidgets1067_Stepper_Vertical_02": "720476",
        "Phidgets1067_Stepper_Riel_03": "720493",
        "Phidgets1067_Stepper_Vertical_03": "720666",
        "Phidgets1067_Stepper_Riel_04": "720536",
        "Phidgets1067_Stepper_Vertical_04": "615347",
}
devicesSerialNumbersValidation = {
        "Phidget1012_Securitas_03": "",
        "Phidget1012_Control_04": "",
        "Phidgets1067_Stepper_Riel_05": "",
        "Phidgets1067_Stepper_Vertical_05": "",
        "Phidgets1067_Stepper_Riel_06": "",
        "Phidgets1067_Stepper_Vertical_06": "",

}

cont = Stepper
phidgetsDAC["serialNumber"] = 12
for serial in devicesSerialNumbersTester:
    print(devicesSerialNumbersTester[serial])


