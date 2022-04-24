from machine import Pin, PWM

from motor_control import Motor
import time, math


# p_en = PWM(Pin(17, Pin.OUT), freq=1000, duty=300)
# p_in1 = Pin(27, Pin.OUT)
# p_in2 = Pin(26, Pin.OUT)

# p_in1(0)
# p_in2(1)
# p_en.duty(1000)


# def pulse(l, t):
#     for i in range(20):
#         l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
#         time.sleep_ms(t)

# for i in range(100):
#     pulse(p_en, 100)


m = Motor()
m.forward(512)