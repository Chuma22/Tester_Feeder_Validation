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

def start(serialNumber):
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

async def testStepperEncoder(stepper_Test_Encoder,serial_Number_Stepper_Encoder,encoder_Test,channel_Encoder):
    encoderTest = encoder_Test
    stepperTest = stepper_Test_Encoder
    serialNumberStepper = serial_Number_Stepper_Encoder
    channelEncoder = channel_Encoder

    encoderTest.setChannel(channelEncoder)
    encoderTest.openWaitForAttachment(1000)
    encoderTest.setEnabled(True)
    encoderTest.setDataInterval(8)

    stepperTest.setDeviceSerialNumber(serialNumberStepper)
    stepperTest.openWaitForAttachment(1000)
    stepperTest.setCurrentLimit(2.8)
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

async def testStepperEncoderHome(stepper_Test_Encoder,serial_Number_Stepper_Encoder,encoder_Test,channel_Encoder):
    
    encoderTest = encoder_Test
    stepperTest = stepper_Test_Encoder
    serialNumberStepper = serial_Number_Stepper_Encoder
    channelEncoder = channel_Encoder

    encoderTest.setChannel(channelEncoder)
    encoderTest.openWaitForAttachment(1000)
    encoderTest.setEnabled(True)
    encoderTest.setDataInterval(8)

    stepperTest.setDeviceSerialNumber(serialNumberStepper)
    stepperTest.openWaitForAttachment(1000)
    stepperTest.setCurrentLimit(2.8)
    encoder01_position = encoderTest.getPosition()
    homeHorizontal2 = inputs2[13].getState()
    while True:
        if homeHorizontal2 ==True:
            stepperTest.setEngaged(False)            
            break
        else:
            stepperTest.setControlMode(StepperControlMode.CONTROL_MODE_RUN)
            stepperTest.setVelocityLimit(1500)
            stepperTest.setEngaged(True)
            homeHorizontal2 = inputs2[13].getState()

async def testStepperHome(stepper_Test,serial_Number_Stepper):
    global inputs,inputs2

    
    stepperTest = stepper_Test
    serialNumberStepper = serial_Number_Stepper

    stepperTest.setDeviceSerialNumber(serialNumberStepper)
    stepperTest.openWaitForAttachment(1000)
    stepperTest.setCurrentLimit(1.8)
    stepper_position = stepperTest.getPosition()

    SHElevadorValidador01 = inputs2[14].getState()
    while SHElevadorValidador01 == False:
        stepperTest.setControlMode(StepperControlMode.CONTROL_MODE_STEP)
        stepperTest.setEngaged(True)
        stepperTest.setTargetPosition(-3200 * 10)

        SHElevadorValidador01 = inputs2[14].getState()
        if SHElevadorValidador01 == True:
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

async def testStepper(stepper_Test,serial_Number_Stepper):
    global inputs,inputs2

    
    stepperTest = stepper_Test
    serialNumberStepper = serial_Number_Stepper

    stepperTest.setDeviceSerialNumber(serialNumberStepper)
    stepperTest.openWaitForAttachment(1000)
    stepperTest.setCurrentLimit(1.8)
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

async def testGrepper():
    global inputs2, outputs2

    grepper = outputs2[0]
    grepperOpen = inputs2[3]
    grepperClose = inputs2[4]
    stepCero = False
    grepper.setState(True)
    while True:
        if grepperOpen.getState() == True:
            sleep(0.5)
            grepper.setState(False)
            stepCero = True
        if grepperClose and stepCero:
            break

async def main() :   
    global inputs, outputs, inputs2, outputs2,offsetB4
    
    offsetB4=0

    serialNumber = 692552 # MOD D
    outputs,inputs = start(serialNumber)
    serialNumber = 692538 # MOD B
    outputs2,inputs2 = start(serialNumber)
    outputs[8].setState(True)
    outputs[9].setState(True)
    outputs[10].setState(True)
    outputs[11].setState(True)
    outputs[12].setState(True)
    outputs[13].setState(True)
    #await outputOn(outputs)
#movimiento de motores
    encoderA1 = Encoder()
    encoderA2 = Encoder()
    encoderA3 = Encoder()
    encoderA4 = Encoder()
    serialNumberEncoderA = 590369
    channelEncoderA1 = 0
    channelEncoderA2 = 1
    channelEncoderA3 = 2
    channelEncoderA4 = 3
    encoderA1.setDeviceSerialNumber(serialNumberEncoderA)
    encoderA2.setDeviceSerialNumber(serialNumberEncoderA)
    encoderA3.setDeviceSerialNumber(serialNumberEncoderA)
    encoderA4.setDeviceSerialNumber(serialNumberEncoderA)
# Motores de Riel
    stepper1B = Stepper()
    stepper3B = Stepper()
    stepper1C = Stepper()
    stepper3C = Stepper()
    serialNumberStepper1B = 720437
    serialNumberStepper3B = 720464
    serialNumberStepper1C = 720493
    serialNumberStepper3C = 720536
# Motores verticales
    stepper2B = Stepper()
    stepper4B = Stepper()
    stepper2C = Stepper()
    stepper4C = Stepper()
    serialNumberStepper2B = 720489
    serialNumberStepper4B = 720476
    serialNumberStepper2C = 720666
    serialNumberStepper4C = 615347
   

    with concurrent.futures.ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        await asyncio.gather(
            loop.run_in_executor(executor, lambda: asyncio.run(testGrepper())),
            #loop.run_in_executor(executor, lambda: asyncio.run(testStepper(stepper4B,serialNumberStepper4B))),
            #loop.run_in_executor(executor, lambda: asyncio.run(testStepperEncoder(stepper1B, serialNumberStepper1B, encoderA1, channelEncoderA1))),
            #loop.run_in_executor(executor, lambda: asyncio.run(testStepperEncoder(stepper3B, serialNumberStepper3B, encoderA2, channelEncoderA2))),
            # loop.run_in_executor(executor, lambda: asyncio.run(testStepperEncoder(stepper1C, serialNumberStepper1C, encoderA3, channelEncoderA3))),
            # loop.run_in_executor(executor, lambda: asyncio.run(testStepperEncoder(stepper3C, serialNumberStepper3C, encoderA4, channelEncoderA4)))
        )



if __name__ == "__main__":
    global outputs, inputs
    outputs = 0
    inputs = 0
    # loop = asyncio.get_event_loop()
#    loop.run_until_complete(main())
    asyncio.run(main())

