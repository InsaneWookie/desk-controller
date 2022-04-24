# Author: Olivier Lenoir - <olivier.len02@gmail.com>
# Created: 2020-06-14 21:05:12
# Project: L298 Dual H-bridge, MicroPython
# Description:

from machine import Pin, PWM


class L298(object):

    def __init__(self, en, in1, in2, freq=1000):
        self.freq = freq
        self.speed = 0
        self.p_en = PWM(Pin(en, Pin.OUT), freq=self.freq, duty=self.speed)
        self.p_in1 = Pin(in1, Pin.OUT)
        self.p_in2 = Pin(in2, Pin.OUT)
        self.p_in1(0)
        self.p_in2(0)

    def stop(self):
        self.p_en.duty(0)
        self.p_in1(0)
        self.p_in2(0)

    def forward(self):
        self.p_in2(0)
        self.p_en.duty(self.speed)
        self.p_in1(1)

    def reverse(self):
        self.p_in1(0)
        self.p_en.duty(self.speed)
        self.p_in2(1)

    def speed(self, speed=None):
        if speed is None:
            return self.speed
        else:
            self.speed = min(1023, max(0, speed))
