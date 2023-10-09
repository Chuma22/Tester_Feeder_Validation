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
global devicesSerialNumbersTester, devicesSerialNumbersValidation, ValidationRielSingle

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
        "MOD": "VALIDATION",
        "Phidget1012_Securitas_03": "",
        "Phidget1012_Control_04": "",
        "Phidgets1067_Stepper_Riel_05": "",
        "Phidgets1067_Stepper_Vertical_05": "",
        "Phidgets1067_Stepper_Riel_06": "",
        "Phidgets1067_Stepper_Vertical_06": "",

}
ValidationRielSingle = {
        "MOD": "TESTER",
        "Phidget1012_Control_01": "670593",
        "Phidgets1067_Stepper_Riel_01": "720417",
        "Phidgets1067_Stepper_Vertical_01": "720415",
        "Phidgets1047_Encoder_01": "656814"


}


def startIO(serialNumber):
    digitalInputs = []
    digitalOutputs = []
    serialNumber = serialNumber
    inputs = 16
    outputs = 16

    for input  in range(inputs):
        digital_input = DigitalInput()
        digital_input.setDeviceSerialNumber(serialNumber)
        digital_input.setChannel(input)
        digital_input.open()
        digitalInputs.append(digital_input)
        print(f"Entrada digital en el puerto {input} lista para usar.")

    for output in range(outputs):
        digital_output = DigitalOutput()
        digital_output.setDeviceSerialNumber(serialNumber)
        digital_output.setChannel(output)
        digital_output.openWaitForAttachment(5000)
        digitalOutputs.append(digital_output)
        print(f"Salida digital en el puerto {output} lista para usar.")
    return digitalOutputs, digitalInputs

def startEncoder(serialnumber : int):

    encoderA= []
    port = 4
    for index in range(port) :
        encoderA1 = Encoder()
        encoderA1.setDeviceSerialNumber(serialnumber)
        encoderA1.setChannel(index)
        encoderA1.openWaitForAttachment(1000)
        encoderA1.setEnabled(True)
        encoderA1.setDataInterval(8)
        encoderA.append(encoderA1)
        print(f"Salida del Encoder {index} lista para usar.")

    return encoderA

def startSteppers(devicesSerialNumbers: dict):
    steppersEncoder = []
    steppers = []
    for device in devicesSerialNumbers:
        if ((device == "Phidgets1067_Stepper_Riel_01") or(device == "Phidgets1067_Stepper_Riel_02") or(device == "Phidgets1067_Stepper_Riel_03") or(device == "Phidgets1067_Stepper_Riel_04")or(device == "Phidgets1067_Stepper_Riel_05")or(device == "Phidgets1067_Stepper_Riel_06")):
            stepperTest = Stepper()
            stepperTest.setDeviceSerialNumber(int(devicesSerialNumbers[device]))
            stepperTest.openWaitForAttachment(1000)
            stepperTest.setCurrentLimit(2.8)
            steppersEncoder.append(stepperTest)
            print(f"Motor {device} lista para usar.")
        
        if ((device == "Phidgets1067_Stepper_Vertical_01") or(device == "Phidgets1067_Stepper_Vertical_02") or(device == "Phidgets1067_Stepper_Vertical_03") or(device == "Phidgets1067_Stepper_Vertical_04")or(device == "Phidgets1067_Stepper_Vertical_05")or(device == "Phidgets1067_Stepper_Vertical_06")):
            stepperTest = Stepper()
            stepperTest.setDeviceSerialNumber(int(devicesSerialNumbers[device]))
            stepperTest.openWaitForAttachment(1000)
            stepperTest.setCurrentLimit(1.8)
            steppers.append(stepperTest)
            print(f"Motor {device} lista para usar.")

    return steppersEncoder,steppers

async def outputOn(digitalOutputs):
        for output in digitalOutputs:
            output.setState(True)
            await asyncio.sleep(0.1)    
    
async def outputOff(digitalOutputs):
    for output in digitalOutputs:
        output.setState(False)
        await asyncio.sleep(0.1)

async def readInputs(digitalInputs):
     while True:
        count = 0
        for input in digitalInputs:
            count= count + 1
            if  (input.getState() == True):
                print(f"Señal activa {count-1} lista para usar.")
        await asyncio.sleep(0.4)

async def runOutput(digitalOutput):
        outputs = digitalOutput
        while True:
            await outputOn(outputs)
            await outputOff(outputs)

async def testStepperEncoder(stepper_Test_Encoder,encoder_Test,digital_Inputs:list,first_board_Position:bool):
    encoderTest = encoder_Test
    stepperTest = stepper_Test_Encoder

    encoder01_position = encoderTest.getPosition()
    giro = 0
    while True:
        encoder01_position = encoderTest.getPosition()
        print(encoder01_position)
        stepperTest.setEngaged(True)
        if giro == 0 :
            stepperTest.setControlMode(StepperControlMode.CONTROL_MODE_RUN)
            stepperTest.setVelocityLimit(1500)
            if encoder01_position >= 100 * 14.48:
                stepperTest.setEngaged(False)
                sleep(1)
                giro = 1
        else:
            stepperTest.setControlMode(StepperControlMode.CONTROL_MODE_RUN)
            stepperTest.setVelocityLimit(-1500)
            if encoder01_position <= 0:
                stepperTest.setEngaged(False)
                sleep(1)
                giro = 0
                break

async def testStepperEncoderHome(stepper_Test_Encoder,digital_Inputs:list,first_board_Position:bool):

    stepperTest = stepper_Test_Encoder
    digitalInputs = digital_Inputs
    boardPosition = first_board_Position
    if boardPosition == True:
        homeVertical  = digitalInputs[5]
        homeVerticalFlag = homeVertical.getState() 
    else:
        homeVertical  = digitalInputs[13]
        homeVerticalFlag = homeVertical.getState() 
    while True:
        if homeVerticalFlag ==True:
            stepperTest.setEngaged(False)            
            break
        else:
            stepperTest.setControlMode(StepperControlMode.CONTROL_MODE_RUN)
            stepperTest.setVelocityLimit(-1500)
            stepperTest.setEngaged(True)
            homeVerticalFlag = homeVertical.getState() 

async def testStepperHome(stepper_Test, digital_Inputs:list,first_board_Position:bool):
    
    stepperTest = stepper_Test
    digitalInputs = digital_Inputs
    boardPosition = first_board_Position
    if boardPosition == True:
        homeVertical  = digitalInputs[6]
        homeVerticalFlag = homeVertical.getState() 
    else:
        homeVertical  = digitalInputs[14]
        homeVerticalFlag = homeVertical.getState() 
    while homeVerticalFlag == False:
        stepperTest.setControlMode(StepperControlMode.CONTROL_MODE_STEP)
        stepperTest.setEngaged(True)
        stepperTest.setTargetPosition(-3200 * 10)

        homeVerticalFlag = homeVertical.getState() 
        if homeVerticalFlag == True:
            stepperTest.setEngaged(False)
            Position_Stepper04 = stepperTest.getPosition()
            offsetM4 = -(Position_Stepper04)
            break
    sleep(0.1)

    # stepperTest.addPositionOffset(offsetM4)
    # Position_Stepper04 = stepperTest.getPosition()

    # stepperTest.setTargetPosition(3200 * -1)
    # stepperTest.setEngaged(True)
    # sleep(2)
    # Position_Stepper04 = stepperTest.getPosition()
    # stepperTest.setEngaged(True)

async def testStepper(stepper_Test,digital_Inputs:list,first_board_Position:bool):
    stepperTest = stepper_Test
    stepper_position = stepperTest.getPosition()
    moveStepper = 500

    stepperTest.setControlMode(StepperControlMode.CONTROL_MODE_STEP)
    stepperTest.setEngaged(True)
        
    SHElevadorValidador01 = inputs2[14].getState()
    while SHElevadorValidador01 == False:
        while True:
            stepperTest.addPositionOffset(0)
            stepperTest.setTargetPosition(moveStepper * 10)
            
    
            positionCurrent = stepperTest.getPosition()
            print(positionCurrent)
            if positionCurrent >= moveStepper:
                stepperTest.addPositionOffset(0)
                stepperTest.setTargetPosition(-moveStepper * 10)
                sleep(0.2)

                break

            SHElevadorValidador01 = inputs2[14].getState()
            if SHElevadorValidador01 == True:
                stepperTest.setEngaged(False)
                Position_Stepper04 = stepperTest.getPosition()
                offsetM4 = -(Position_Stepper04)
                break
    sleep(0.1)

async def testGrepper(digital_Outputs:list,digital_Inputs:list,first_board_Position:bool):
    boardPosition = first_board_Position
    digitalOutputs = digital_Outputs
    digitalInputs = digital_Inputs
    if boardPosition == False:
        grepper = digitalOutputs[1]
        grepperOpen = digitalInputs[11]
        grepperClose = digitalInputs[12]        
    else:
        grepper = digitalOutputs[0]
        grepperOpen = digitalInputs[3]
        grepperClose = digitalInputs[4]

    stepCero = False
    grepper.setState(True)
    while True:
        if grepperOpen.getState() == True:
            sleep(0.5)
            grepper.setState(False)
            stepCero = True
        if grepperClose and stepCero:
            break

async def testInputs(digital_Inputs:list,first_board_Position:bool):
    
        boardPosition = first_board_Position
        digitalInputs = digital_Inputs
        step = 0
        print("Sensor de pieza en gripper")

        while True:
            if boardPosition == True:
                if step == 0:
                    readInput = digitalInputs[0].getState()
                    if readInput == True:
                        print("OK")
                        print("Señal de pieza PASS")
                        step = 1
                if step == 1:
                    readInput = digitalInputs[1].getState()
                    if readInput == True:
                        print("OK")
                        print("Señal de pieza FAIL")
                        step = 2
                if step == 2:
                    readInput = digitalInputs[2].getState()
                    if readInput == True:
                        print("OK")
                        print("Sensor de Conveyor entrada ")
                        step = 3
                if step == 3:
                    readInput = digitalInputs[7].getState()
                    if readInput == True:
                        print("OK ")
                        print("Sensor de Conveyor salida")
                        step = 4
                if step == 4:#TODO modificar este parte para dos Phidgets
                    readInput = digitalInputs[8].getState()
                    if readInput == True:
                        print("OK ")
                        step = 0
                        break                                 
            else:
                if step == 0:
                    readInput = digitalInputs[8].getState()
                    if readInput == True:
                        print("Sensor de pieza en gripe energizado")
                        step = 1
                if step == 1:
                    readInput = digitalInputs[9].getState()
                    if readInput == True:
                        print("Señal de pieza PASS")
                        step = 2
                if step == 2:
                    readInput = digitalInputs[10].getState()
                    if readInput == True:
                        print("Señal Pieza Fail")
                        step = 3
                if step == 3:
                    readInput = digitalInputs[15].getState()
                    if readInput == True:
                        print("Sensor de Conveyor entrada energizado ")
                        step = 4
                if step == 4:#TODO modificar este parte para dos Phidgets
                    readInput = digitalInputs[8].getState()
                    if readInput == True:
                        print("Sensor de Conveyor salida energizado ")
                        step = 0 
                        break  
            

    
async def initialization(devicesSerialNumbers: dict):
    
    global inputs, outputs, inputs2, outputs2,inputs3,outputs3,inputs4,outputs4,offsetB4,EncoderA,steppersEncoder,steppersSingle
    steppersEncoder = []
    steppersSingle = []

    offsetB4 = 0
    inputs4 = 0
    outputs4 = 0
    # Tester
    serialNumber = int(devicesSerialNumbers["Phidget1012_Control_01"]) # MOD B
    outputs,inputs = startIO(serialNumber)
    serialNumber = int(devicesSerialNumbers["Phidget1012_Control_02"]) # MOD C
    outputs2,inputs2 = startIO(serialNumber)
    serialNumber = int(devicesSerialNumbers["Phidget1012_Securitas_03"]) # MOD D
    outputs3,inputs3 = startIO(serialNumber)
    #movimiento de motores
    # serialNumberEncoderA = int(devicesSerialNumbers["Phidgets1047_Encoder_01"]) # Encoder
    # EncoderA = startEncoder(serialNumberEncoderA)
    # steppersEncoder,steppersSingle = startSteppers(devicesSerialNumbers)
    await outputOn(outputs)
    await outputOn(outputs3)
    # await testGrepper(outputs,inputs,first_board_Position = True)
    # await testStepperHome(steppersSingle[0],inputs,first_board_Position = True)
    # await testStepperEncoderHome(steppersEncoder[0],inputs,first_board_Position=True)
    sleep(2)
    # await testStepperEncoder(steppersEncoder[0],EncoderA[0],inputs,first_board_Position = True)
    # await testInputs(inputs,first_board_Position=True)

async def testModTester(devicesSerialNumbers: dict):
    global inputs, outputs, inputs2, outputs2,inputs3,outputs3,inputs4,outputs4,offsetB4,EncoderA,steppersEncoder,steppersSingle
    if devicesSerialNumbers["MOD"] == "TESTER":
        boardPosition = False
        for index in range(steppersEncoder):
            testStepperHome(steppersSingle[index],inputs,boardPosition)
            testStepperEncoderHome(steppersEncoder[index],inputs,boardPosition)
            if index <= 2 :
                boardPosition= True
        for index in range(steppersEncoder):
                if index <= 2 :
                    boardPosition= True
    #TODO Continiar aqui 
        
    if devicesSerialNumbers["MOD"] == "VALIDATION":
        pass

async def main() :   
   
    await initialization(devicesSerialNumbersTester)
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     loop = asyncio.get_event_loop()
    #     await asyncio.gather(
    #         loop.run_in_executor(executor, lambda: asyncio.run(testGrepper())),
    #         #loop.run_in_executor(executor, lambda: asyncio.run(testStepper(stepper4B,serialNumberStepper4B))),
    #         #loop.run_in_executor(executor, lambda: asyncio.run(testStepperEncoder(stepper1B, serialNumberStepper1B, encoderA1, channelEncoderA1))),
    #         #loop.run_in_executor(executor, lambda: asyncio.run(testStepperEncoder(stepper3B, serialNumberStepper3B, encoderA2, channelEncoderA2))),
    #         # loop.run_in_executor(executor, lambda: asyncio.run(testStepperEncoder(stepper1C, serialNumberStepper1C, encoderA3, channelEncoderA3))),
    #         # loop.run_in_executor(executor, lambda: asyncio.run(testStepperEncoder(stepper3C, serialNumberStepper3C, encoderA4, channelEncoderA4)))
    #     )



if __name__ == "__main__":
    global outputs, inputs
    outputs = 0
    inputs = 0
    # loop = asyncio.get_event_loop()
#    loop.run_until_complete(main())
    asyncio.run(main())
