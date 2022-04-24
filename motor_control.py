
from machine import Pin, PWM


class Motor:

    def __init__(self):
        print("init")
        self.p_en = PWM(Pin(16, Pin.OUT), freq=1000, duty=300)
        self.p_in1 = Pin(27, Pin.OUT)
        self.p_in2 = Pin(26, Pin.OUT)

    def stop(self):
        self.p_en.duty(0)
        # self.p_in1(0)
        # self.p_in2(0)

    def forward(self, duty):
        print("forward")
        self.p_in2(0)
        self.p_en.duty(duty)
        self.p_in1(1)

    def reverse(self, duty):
        self.p_in1(0)
        self.p_en.duty(duty)
        self.p_in2(1)

    def brk(self):
        self.p_en.duty(1023)
        self.p_in1(1)
        self.p_in2(1)
    