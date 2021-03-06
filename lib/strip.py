# coding: utf-8

import time
import board
import neopixel

class Strip(object):
    def __init__(self, size = 50, pin = board.D18):
        self.size = size
        self.strip = neopixel.NeoPixel(pin, size)

    def reset_lights(self):
        self.strip.fill((0, 0, 0))

    def monochrome(self, color=(255, 0, 0), delay=0.05, reset_before=True):
        if reset_before:
            reset_lights()

        if delay == 0:
            self.strip.fill(color)
        else:
            for i in range(self.size):
                self.strip[i] = color
                time.sleep(delay)


    def right_left_right(self, color1=(255, 0, 0), color2=(0,0,255), delay=0.05):
        self.reset_lights()
        for i in range(self.size):
            self.strip[i] = color1
            time.sleep(delay)
        for i in reversed(range(self.size)):
            self.strip[i] = color2
            time.sleep(delay)


    def move_with_tail(self, delay=0.1, lenght=5, reverse=False):
        if not reverse:
            for i in range(self.size):
                if i - lenght >= 0:
                    self.strip[i-lenght] = (0, 0, 0)
                self.strip[i] = (255, 0, 0)
                time.sleep(delay)
        else:
            for i in reversed(range(self.size)):
                if i + lenght < self.size:
                    self.strip[i+lenght] = (0, 0, 0)
                self.strip[i] = (255, 0, 0)
                time.sleep(delay)


    def go_and_back(self, delay=0.05, lenght=5, times=10):
        self.reset_lights()
        for _ in range(times):
            self.move_with_tail(delay, lenght)
            self.move_with_tail(delay, lenght, True)
              
