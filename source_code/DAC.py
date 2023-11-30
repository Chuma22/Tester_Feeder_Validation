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
global devicesSerialNumbersTester, devicesSerialNumbersValidation, ValidationRielSingle

devicesSerialNumbersTester = {
        "MOD": "TESTER",
        "Phidget1012_Control_01": "692542",
        "Phidget1012_Control_02": "692297",
        "Phidget1012_Securitas_03": "692302",
        "Phidgets1047_Encoder_01": "590298",
        "Phidgets1067_Stepper_Riel_01": "615358",
        "Phidgets1067_Stepper_Vertical_01": "720540",
        "Phidgets1067_Stepper_Riel_02": "615372",
        "Phidgets1067_Stepper_Vertical_02": "720511",
        "Phidgets1067_Stepper_Riel_03": "720491",
        "Phidgets1067_Stepper_Vertical_03": "615354",
        "Phidgets1067_Stepper_Riel_04": "720538",
        "Phidgets1067_Stepper_Vertical_04": "720436",
        # "MOD": "TESTER",
        # "Phidget1012_Control_01": "692538",
        # "Phidget1012_Control_02": "692440",
        # "Phidget1012_Securitas_03": "692552",
        # "Phidgets1047_Encoder_01": "590369",
        # "Phidgets1067_Stepper_Riel_01": "720437",
        # "Phidgets1067_Stepper_Vertical_01": "720489",
        # "Phidgets1067_Stepper_Riel_02": "720464",
        # "Phidgets1067_Stepper_Vertical_02": "720476",
        # "Phidgets1067_Stepper_Riel_03": "720493",
        # "Phidgets1067_Stepper_Vertical_03": "720583",
        # "Phidgets1067_Stepper_Riel_04": "720536",
        # "Phidgets1067_Stepper_Vertical_04": "615347",
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

def outputOn(digitalOutputs):
        for output in digitalOutputs:
            output.setState(True)
            sleep(0.1)    
    
def outputOff(digitalOutputs):
    for output in digitalOutputs:
        output.setState(False)
        sleep(0.1)

def readInputs(digitalInputs):
     while True:
        count = 0
        for input in digitalInputs:
            count= count + 1
            if  (input.getState() == True):
                print(f"Señal activa {count-1} lista para usar.")
        sleep(0.4)

def runOutput(digitalOutput):
        outputs = digitalOutput
        while True:
            outputOn(outputs)
            outputOff(outputs)

def testStepperEncoder(stepper_Test_Encoder,encoder_Test,digital_Inputs:list,first_board_Position:bool,move_Unit:int):
    stepperTest = stepper_Test_Encoder
    digitalInputs = digital_Inputs
    boardPosition = first_board_Position
    encoderTest = encoder_Test
    currenPosition = encoderTest.getPosition()
    changePistionHome = False
     
    if boardPosition == True:
        homeVertical  = digitalInputs[5]
        homeVerticalFlag = homeVertical.getState()
        velocity = 1500
        moveInt = currenPosition + (move_Unit* 14.48)

    else:
        homeVertical  = digitalInputs[13]
        homeVerticalFlag = homeVertical.getState() 
        velocity = -1500 
        moveInt = currenPosition - (move_Unit* 14.48)
    while True:
        if (homeVerticalFlag ==True and changePistionHome == True):
            stepperTest.setEngaged(False)            
            break
        else:
            stepperTest.setControlMode(StepperControlMode.CONTROL_MODE_RUN)
            if move_Unit > 0:
                stepperTest.setVelocityLimit(velocity)
            else:
                stepperTest.setVelocityLimit(-velocity)
            stepperTest.setEngaged(True)
            homeVerticalFlag = homeVertical.getState()
            encoder01_position = encoderTest.getPosition()
            print(encoder01_position)
            if boardPosition == True:
                if ((encoder01_position >= moveInt and move_Unit > 0) or (encoder01_position <= moveInt and move_Unit < 0)):
                    stepperTest.setEngaged(False)
                    print("llegue")
                    sleep(1) 
                    break
            else:
                if ((encoder01_position <= moveInt and move_Unit > 0) or (encoder01_position >= moveInt and move_Unit < 0)):
                    stepperTest.setEngaged(False)
                    print("llegue")
                    sleep(1) 
                    break
        if (homeVerticalFlag == False ):
            changePistionHome = True
        
    
def testStepperEncoderHome(stepper_Test_Encoder,encoder_Test,digital_Inputs:list,first_board_Position:bool):
    encoderTest = encoder_Test
    stepperTest = stepper_Test_Encoder
    digitalInputs = digital_Inputs
    boardPosition = first_board_Position
    if boardPosition == True:
        homeVertical  = digitalInputs[5]
        homeVerticalFlag = homeVertical.getState()
        velocity = -1500 
    else:
        homeVertical  = digitalInputs[13]
        homeVerticalFlag = homeVertical.getState() 
        velocity = 1500 

    while True:
        if homeVerticalFlag ==True:
            offsetM1 = -(stepperTest.getPosition())
           # print(offsetM1)
            stepperTest.addPositionOffset(offsetM1)
            position_Stepper = stepperTest.getPosition()
           # print(position_Stepper)
            stepperTest.setEngaged(False)            
            break
        else:
            stepperTest.setControlMode(StepperControlMode.CONTROL_MODE_RUN)
            stepperTest.setVelocityLimit(velocity)
            stepperTest.setEngaged(True)
            homeVerticalFlag = homeVertical.getState() 
    encoderTest.setPosition(0)
def testStepperHome(stepper_Test, digital_Inputs:list,first_board_Position:bool):
    
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
        stepperTest.setTargetPosition(-4200 * 10)

        homeVerticalFlag = homeVertical.getState() 
        if homeVerticalFlag == True:
            stepperTest.setEngaged(False)
            Position_Stepper = stepperTest.getPosition()
            offsetM4 = -(Position_Stepper)
            print(Position_Stepper)
            stepperTest.addPositionOffset(0)
            break


    # stepperTest.addPositionOffset(offsetM4)
    # Position_Stepper04 = stepperTest.getPosition()

    # stepperTest.setTargetPosition(3200 * -1)
    # stepperTest.setEngaged(True)
    # sleep(2)
    # Position_Stepper04 = stepperTest.getPosition()
    # stepperTest.setEngaged(True)

def testStepper(stepper_Test,digital_Inputs:list,first_board_Position:bool,move_Unit:int):
    stepperTest = stepper_Test
    stepper_position = stepperTest.getPosition()
    moveStepper = move_Unit
    changePistionHome = False

    stepperTest.setControlMode(StepperControlMode.CONTROL_MODE_STEP)
    stepperTest.setEngaged(True)
        
    while True:
        SHElevadorValidador01 = inputs2[14].getState()
        currenPosition = stepperTest.getPosition()
        if (SHElevadorValidador01 == True and changePistionHome == True) or currenPosition == (moveStepper*10) :
            break
        stepperTest.addPositionOffset(0)
        stepperTest.setTargetPosition(moveStepper * 10)
        

        positionCurrent = stepperTest.getPosition()
        print(positionCurrent)
        if SHElevadorValidador01 == False:
            changePistionHome = True
def testGrepper(digital_Outputs:list,digital_Inputs:list,first_board_Position:bool):
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

def testInputs(digital_Inputs:list,digital_Outputs : list,first_board_Position:bool):
    
        boardPosition = first_board_Position
        digitalInputs = digital_Inputs
        digitalOutputs = digital_Outputs
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
                        print("Se encendio interlock A")
                        digitalOutputs[8].setState(1)
                        
                        print("Sensor de Conveyor entrada ")
                        step = 3
                if step == 3:
                    readInput = digitalInputs[7].getState()
                    if readInput == True:
                        print("OK ")
                        print("Sensor de Conveyor salida")
                        step = 4
                        break
                # if step == 4:#TODO modificar este parte para dos Phidgets
                #     readInput = digitalInputs[8].getState()
                #     if readInput == True:
                #         print("OK ")
                #         step = 0
                #         break                                 
            else:
                if step == 0:
                    readInput = digitalInputs[8].getState()
                    if readInput == True:
                        print("OK")
                        print("Señal de pieza PASS")
                        step = 1
                if step == 1:
                    readInput = digitalInputs[9].getState()
                    if readInput == True:
                        print("OK")
                        print("Señal de pieza FAIL")
                        step = 2
                if step == 2:
                    readInput = digitalInputs[10].getState()
                    if readInput == True:
                        print("OK")
                        print("Se encendio interlock A")
                        digitalOutputs[9].setState(1)
                        print("Sensor de Conveyor entrada ")
                        step = 3
                if step == 3:
                    readInput = digitalInputs[15].getState()
                    if readInput == True:
                        print("°°°°°°°Sistema Validado°°°°°°°°°")
                        step = 4
                        break
                # if step == 4:#TODO modificar este parte para dos Phidgets
                #     readInput = digitalInputs[8].getState()
                #     if readInput == True:
                #         print("Sensor de Conveyor salida energizado ")
                #         step = 0 
                #         break  
            
def testSecurity(digital_Inputs : list,digital_Ouputs : list):
        digitalInputs = digital_Inputs
        digitalOuputs = digital_Ouputs
        position = False
        position2 = False
        step = 0
        
        print("Validando sensores reflectivos de salida")
        print("Señal de salida de conveyor 01")

        while True:
            if step == 0:
                readInput = digitalInputs[0].getState()
                if readInput == True:
                    print("OK")
                    print("Señal de salida de conveyor 02")
                    step = 1
            if step == 1:
                readInput = digitalInputs[1].getState()
                if readInput == True:
                    print("OK")
                    print("Señal de salida de conveyor 03")
                    step = 2
            if step == 2:
                readInput = digitalInputs[2].getState()
                if readInput == True:
                    print("OK")
                    print("Señal de salida de conveyor 04")
                    step = 3
            if step == 3:
                readInput = digitalInputs[3].getState()
                if readInput == True:   #TODO
                    print("OK ")
                    print("Puerta Nido 1 abrir puerta")
                    step = 4
            if step == 4:
                readInput = digitalInputs[4].getState()
                if readInput == True and not position:
                    print("Cerrar puerta")
                    position =  True
                if readInput == False and position:
                    print("OK")
                    digitalOuputs[8].setState(1)
                    print("Puerta Nido 2 abrir puerta")
                    position = False
                    step = 5
            if step == 5:
                readInput = digitalInputs[5].getState()
                if readInput == True  and not position:
                    print("Cerrar puerta")
                    position =  True
                if readInput == False and position:
                    print("OK")
                    digitalOuputs[9].setState(1)
                    print("Puerta Nido 3 abrir puerta")
                    position = False
                    step = 6
            if step == 6:
                readInput = digitalInputs[6].getState()
                if readInput == True  and not position:
                    print("Cerrar puerta")
                    position =  True
                if readInput == False and position:
                    print("OK")
                    digitalOuputs[10].setState(1)
                    print("Puerta Nido 4 abrir puerta")
                    position = False
                    step = 7
            if step == 7:
                readInput = digitalInputs[7].getState()
                if readInput == True  and not position:
                    print("cerrar puerta")
                    position = True
                if readInput == False and position:
                    print("OK")
                    digitalOuputs[11].setState(1)
                    print("Abrir guarda fija")
                    position = False
                    step = 8                    
            if step == 8:
                readInput = digitalInputs[8].getState()
                if readInput == True  and not position:
                    print("Cerrar guarda fija ")
                    position = True
                if readInput == False and position:
                    print("OK")
                    print("°°°°°°°°°°°Validado°°°°°°°°°°°°°")
                    position = False
                    step = 10
                    break
def initialization(devicesSerialNumbers: dict):
    
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
    serialNumberEncoderA = int(devicesSerialNumbers["Phidgets1047_Encoder_01"]) # Encoder
    EncoderA = startEncoder(serialNumberEncoderA)
    steppersEncoder,steppersSingle = startSteppers(devicesSerialNumbers)
    position = True
    testGrepper(outputs,inputs,first_board_Position = position)
    testGrepper(outputs,inputs,first_board_Position = False)
    # testGrepper(outputs2,inputs2,first_board_Position = position)
    testGrepper(outputs2,inputs2,first_board_Position = False)
    outputOn(outputs3)
    testStepperHome(steppersSingle[0],inputs,first_board_Position = position)
    testStepperHome(steppersSingle[1],inputs,first_board_Position = False)
    testStepperHome(steppersSingle[2],inputs2,first_board_Position = position)
    testStepperHome(steppersSingle[3],inputs2,first_board_Position = False)
    testStepperEncoderHome(steppersEncoder[0],EncoderA[0],inputs,first_board_Position = position)
    testStepperEncoderHome(steppersEncoder[1],EncoderA[1],inputs,first_board_Position = False)
    testStepperEncoderHome(steppersEncoder[2],EncoderA[2],inputs2,first_board_Position = position)
    testStepperEncoderHome(steppersEncoder[3],EncoderA[3],inputs2,first_board_Position = False)
    # sleep(2)
    # await testStepperEncoder(steppersEncoder[0],EncoderA[0],inputs,first_board_Position = True)
    outputOff(outputs3)
    testInputs(inputs,outputs,first_board_Position=True)
    testInputs(inputs,outputs,first_board_Position=False)
    testInputs(inputs2,outputs2,first_board_Position=True)
    testInputs(inputs2,outputs2,first_board_Position=False)
    testSecurity(inputs3,outputs3)
    print("Validado")


def testModTester(devicesSerialNumbers: dict):
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

def sequenceTestRiel(stepper_Single,stepper_Encoder,encoder_Test,digital_Inputs:list,digital_Outputs:list,move_Units:int,first_board_Position:bool):
    stepperTestEncoder = stepper_Encoder
    stepperTestSingle = stepper_Single
    encoderTest = encoder_Test
    digitalInputs = digital_Inputs
    digitalOutputs = digital_Outputs
    position =  first_board_Position 
    move = move_Units
    while True:
        testStepperEncoder(stepperTestEncoder,encoderTest,digitalInputs,position,move)
        testStepper(stepperTestSingle,digitalInputs,position,500)
        testGrepper(digitalOutputs,digitalInputs,first_board_Position = position)
        testStepper(stepperTestSingle,digitalInputs,position,-500)
        testStepperEncoder(stepperTestEncoder,encoderTest,digitalInputs,position,-move)    

def riel1():
    move = 100
    sequenceTestRiel(steppersSingle[0],steppersEncoder[0],EncoderA[0],inputs,outputs,move,first_board_Position=True)
def riel2():
    move = 100
    sequenceTestRiel(steppersSingle[1],steppersEncoder[1],EncoderA[1],inputs,outputs,move,first_board_Position=False)
def riel3():
    move = 100
    sequenceTestRiel(steppersSingle[2],steppersEncoder[2],EncoderA[2],inputs2,outputs2,move,first_board_Position=True)
def riel4():
    move = 100
    sequenceTestRiel(steppersSingle[3],steppersEncoder[3],EncoderA[3],inputs2,outputs2,move,first_board_Position=False)

# def value_parameter(runSequences:bool):
#     if runSequences == False:
        
async def main() :   
    global inputs, outputs, inputs2, outputs2,inputs3,outputs3,inputs4,outputs4,offsetB4,EncoderA,steppersEncoder,steppersSingle
    
    position = True
    move = 100
    initialization(devicesSerialNumbersTester)
 
    
    executor = ThreadPoolExecutor(max_workers=15)
    
    executor.submit(riel1)
    executor.submit(riel2)
    executor.submit(riel3)
    executor.submit(riel4)


if __name__ == "__main__":
    global outputs, inputs
    outputs = 0
    inputs = 0
    # loop = asyncio.get_event_loop()
#    loop.run_until_complete(main())

    asyncio.run(main())
