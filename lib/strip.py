# coding: utf-8

import time
import board
import neopixel

class Strip():
    PIXELS_ORDER = neopixel.RGB
    def __init__(self, size=50, pin=board.D18):
        self.size = size
        self.pin = pin
        self.pixels = neopixel.NeoPixel(pin=pin, n=size, pixel_order=self.PIXELS_ORDER)

    def __setitem__(self, index, val):
        self.pixels[index] = val

    def __getitem__(self, index):
        return self.pixels[index]

    def reset_lights(self):
        self.pixels.fill((0, 0, 0))

    def monochrome(self, color=(255, 0, 0), delay=0.05, reset_before=True):
        if reset_before:
            self.reset_lights()

        if delay == 0:
            self.pixels.fill(color)
        else:
            for i in range(self.size):
                self.pixels[i] = color
                time.sleep(delay)

    def right_left_right(self, color1=(255, 0, 0), color2=(0, 0, 255), delay=0.05):
        self.reset_lights()
        for i in range(self.size):
            self.pixels[i] = color1
            time.sleep(delay)
        for i in reversed(range(self.size)):
            self.pixels[i] = color2
            time.sleep(delay)

    def draw_fadeout_line(self, center, length, central_color=(255, 255, 255)):
        strip = neopixel.NeoPixel(self.pin, self.size, pixel_order=self.PIXELS_ORDER, auto_write=False)

        radio = int(length/2) + 1
        color_step = [x/radio for x in central_color]

        strip[center] = central_color
        for offset in range(1, 1 + radio):
            color = []
            for i, j in zip(central_color, color_step):
                color.append(i - (offset * j))
            pos = center - offset
            if pos >= 0:
                strip[pos] = color

            pos = center + offset
            if pos < self.size:
                strip[pos] = color
        strip.show()

    def move_with_tail(self, delay=0.1, length=5, color=(255, 255, 255), reverse=False):
        iterator = reversed(range(self.size)) if reverse else range(self.size)
        for i in iterator:
            self.draw_fadeout_line(i, length, color)
            time.sleep(delay)

    def go_and_back(self, delay=0.05, length=5, color=(255, 255, 255), times=10):
        self.reset_lights()
        for _ in range(times):
            self.move_with_tail(delay, length, color)
            self.move_with_tail(delay, length, color, True)
