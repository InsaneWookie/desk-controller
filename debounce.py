import machine
import utime

pin = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_UP)
new_click_detected = False

def callback(p):
    global new_click_detected
    new_click_detected = True
    

#pin.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=callback, hard=True)
pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback)

# The code below will be replaced with uasyncio coro
value = 0
while True:
    while not new_click_detected:
        pass

    utime.sleep_ms(5)  
    if pin.value() == 0:
        value += 1
        print("New value: ", value)

    new_click_detected = False