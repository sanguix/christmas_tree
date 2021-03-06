# coding: utf-8

import board
import neopixel
import time

SIZE = 50
pixels = neopixel.NeoPixel(board.D18, SIZE)


def reset_lights():
    for i in range(SIZE):
        pixels[i] = (0, 0, 0)


def ligth_monocrome(color=(255, 0, 0), delay=0.05, reset_lights=True):
    if reset_lights:
        reset_lights()
    for i in range(SIZE):
        pixels[i] = color
        time.sleep(delay)


def right_left_right(color1=(255, 0, 0), color2=(0,0,255), delay=0.05):
    reset_lights()
    for i in range(SIZE):
        pixels[i] = color1
        time.sleep(delay)
    for i in reversed(range(SIZE)):
        pixels[i] = color2
        time.sleep(delay)


def move_with_tail(delay=0.1, lenght=5, reverse=False):
     if not reverse:
         for i in range(SIZE):
             if i - lenght >= 0:
                 pixels[i-lenght] = (0, 0, 0)
             pixels[i] = (255, 0, 0)
             time.sleep(delay)
     else:
         for i in reversed(range(SIZE)):
             if i + lenght < SIZE:
                  pixels[i+lenght] = (0, 0, 0)
             pixels[i] = (255, 0, 0)
             time.sleep(delay)


def go_and_back(delay=0.05, lenght=5, times=10):
    reset_lights()
    for _ in range(times):
        move_with_tail(delay, lenght)
        move_with_tail(delay, lenght, True)
              
