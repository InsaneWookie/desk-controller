import micropython, machine
import time
from machine import Pin


micropython.alloc_emergency_exception_buf(100)

print('start up')


DESK_UP = 1
DESK_DOWN = -1



deskEncoderPin = Pin(19, Pin.IN, Pin.PULL_UP) # enable internal pull-up resistor
controllerButtonPin = Pin(21, Pin.IN, Pin.PULL_UP)

deskEncoderPulses = 0 #TODO: read this out of non vol
deskDirection = DESK_DOWN #TODO read from non vol
motorEnabled = False

deskBottomPosition = 0
deskTopPosition = 50

def desk_encoder_interupt(pin):
    global deskEncoderPulses
    global deskDirection
    deskEncoderPulses = deskEncoderPulses + deskDirection
    print("pulse", deskEncoderPulses)


buttonDebouceTimer = time.ticks_ms()
BUTTON_DEBOUCE_TIME = 100
def controller_button_interupt(pin):
    global buttonDebouceTimer
    if time.ticks_diff(time.ticks_ms(), buttonDebouceTimer) > BUTTON_DEBOUCE_TIME:
        controller_button_pressed()
        buttonDebouceTimer = time.ticks_ms()
    

def controller_button_pressed():
    global deskDirection    
    invertDeskDirection()
    print("button pressed", deskDirection)
    enableMotor()
    

def enableMotor():
    global deskDirection
    global motorEnabled
    print("running motor", deskDirection)
    motorEnabled = True

def disableMotor():
    global deskDirection
    global motorEnabled
    print("stoping motor", deskDirection)
    motorEnabled = False

def invertDeskDirection():
    global deskDirection 
     
    if deskDirection == DESK_DOWN: 
        deskDirection = DESK_UP 
    else: 
        deskDirection = DESK_DOWN

#interupts
deskEncoderPin.irq(trigger=Pin.IRQ_RISING, handler=desk_encoder_interupt)
controllerButtonPin.irq(trigger=Pin.IRQ_RISING, handler=controller_button_interupt)


while True:
    time.sleep_ms(50)

    #simlute encoder interupts
    if motorEnabled:
        desk_encoder_interupt(0)


    if motorEnabled: 
        if deskDirection == DESK_UP and deskEncoderPulses >= deskTopPosition:
            disableMotor()
        elif deskDirection == DESK_DOWN and deskEncoderPulses <= deskBottomPosition:
            disableMotor()
    

# Interupt for photo encoder
# Keep track of pulses when riasing or lowing desk
# Store pulses for height
