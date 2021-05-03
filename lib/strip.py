# coding: utf-8

import time
import threading

import board
import neopixel


class Strip():
    PIXELS_ORDER = neopixel.RGB
    MAX_BRIGHTNESS = 0.5

    def __init__(self, size=50, pin=board.D18):
        self.size = size
        self.pin = pin
        self.pixels = neopixel.NeoPixel(pin=pin, n=size, pixel_order=self.PIXELS_ORDER, brightness=self.MAX_BRIGHTNESS)
        self.thread = None
        self.stop_sequence = False

    def __setitem__(self, index, val):
        self.stop_any_sequence()
        self.pixels[index] = val

    def __getitem__(self, index):
        self.stop_any_sequence()
        return self.pixels[index]

    def fill(self, color):
        self.stop_any_sequence()
        self.pixels.fill(color)

    def turn_off(self):
        self.stop_any_sequence()
        self.fill((0, 0, 0))

    def stop_any_sequence(self):
        if self.thread is not None:
            self.stop_sequence = True
            self.thread.join()

    def start_sequence(self, generator):
        self.stop_any_sequence()
        self.stop_sequence = False
        self.thread = threading.Thread(target=self._sequencer, args=(generator,))
        self.thread.start()

    def _sequencer(self, generator):
        strip = neopixel.NeoPixel(self.pin, self.size, pixel_order=self.PIXELS_ORDER, auto_write=False)
        for item in generator:
            if self.stop_sequence:
                return
            for pos, color in enumerate(item):
                if color is None:
                    continue
                strip[pos] = color
            strip.show()

    def progressive_fill(self, color=(255, 255, 255), delay=0.05, reset_before=False):
        def generator(color, delay, reset_before=False):
            if reset_before:
                yield [(0, 0, 0)] * self.size

            if delay == 0:
                yield [color] * self.size
            else:
                new_map = [None] * self.size
                for i in range(self.size):
                    time.sleep(delay)
                    new_map[i] = color
                    yield new_map
        self.start_sequence(generator(color, delay, reset_before))

    def right_left_right(self, color1=(255, 0, 0), color2=(0, 0, 255), delay=0.05):
        self.stop_any_sequence()
        self.turn_off()
        for i in range(self.size):
            self.pixels[i] = color1
            time.sleep(delay)
        for i in reversed(range(self.size)):
            self.pixels[i] = color2
            time.sleep(delay)

    def get_fadeout_lights(self, center, length, central_color=(255, 255, 255)):
        lights = [(0, 0, 0)] * self.size

        radio = int(length/2) + 1
        color_step = [x/radio for x in central_color]

        lights[center] = central_color
        for offset in range(1, 1 + radio):
            color = []
            for i, j in zip(central_color, color_step):
                color.append(i - (offset * j))

            pos = center - offset
            if pos >= 0:
                lights[pos] = color

            pos = center + offset
            if pos < self.size:
                lights[pos] = color

        return lights

    def scanner_effect_generator(self, delay=0.1, length=5, color=(255, 255, 255), reverse=False):
        iterator = reversed(range(self.size)) if reverse else range(self.size)
        for i in iterator:
            time.sleep(delay)
            yield self.get_fadeout_lights(i, length, color)

    def scanner_effect(self, delay=0.05, length=15, color=(255, 255, 255)):
        def generator(delay, length, color):
            reverse = False
            while True:
                for lights in self.scanner_effect_generator(delay, length, color, reverse):
                    yield lights
                reverse = not reverse
        self.start_sequence(generator(delay, length, color))
