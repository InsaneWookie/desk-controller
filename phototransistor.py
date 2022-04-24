import machine
import time

pin = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

debouceTimer = time.ticks_ms()

count = 0

def callback(p):
    global debouceTimer
    global count
    if time.ticks_diff(time.ticks_ms(), debouceTimer) > 1000:
        count = count + 1
        print("New value: ", count)
        debouceTimer = time.ticks_ms()
    
    

#pin.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=callback, hard=True)
pin.irq(trigger=machine.Pin.IRQ_RISING, handler=callback)

# The code below will be replaced with uasyncio coro

while True:
    time.sleep_ms(50)