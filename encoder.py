import time
from machine import Pin
from rotary_irq_esp import RotaryIRQ

print('start up')

p4 = Pin(21, Pin.IN, Pin.PULL_UP) # enable internal pull-up resistor

r = RotaryIRQ(pin_num_clk=18, 
              pin_num_dt=19, 
              min_val=0, 
              max_val=5, 
              reverse=False, 
              range_mode=RotaryIRQ.RANGE_UNBOUNDED)

pin_old = p4.value()
val_old = r.value()
while True:
    val_new = r.value()
    pin_new = p4.value()
    
    if val_old < val_new:
        print('down result =', val_new)
        val_old = val_new
    elif val_old > val_new: 
        print('up result =', val_new)
        val_old = val_new
        
    if pin_old != pin_new:
        if pin_new == 1:
            print("button pressed")
        pin_old = pin_new

    

    time.sleep_ms(50)