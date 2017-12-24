from screenapi import ScreenApi
import time
import math
import random

width = 13
height = 12

black = (0, 0, 0)
white = (255, 255, 255)

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
rainbow = [red, orange, yellow, green, blue, purple]

pastel_red = (255, 150, 150)
pastel_orange = (255, 165, 150)
pastel_yellow = (255, 255, 150)
pastel_green = (150, 255, 150)
pastel_blue = (150, 150, 255)
pastel_purple = (255, 150, 255)
pastels = [pastel_red, pastel_orange, pastel_yellow, pastel_green,
           pastel_blue, pastel_purple]


def default(color):
    animation = []
    for r in range(12):
        for c in range(13):
            screen = [[black for x in range(width)] for y in range(height)]
            screen[r][c] = color
            animation.append(screen)
    return animation


def whole_screen(color):
    screen = [[color for x in range(width)] for y in range(height)]
    return screen


def pastel_gradient(frame):
    screen = whole_screen(black)
    for x in range(height):
        for y in range(width):
            index = (math.floor((x + y) / 2) + frame) % 6
            if index == 0:
                screen[x][y] = pastel_red
            elif index == 1:
                screen[x][y] = pastel_orange
            elif index == 2:
                screen[x][y] = pastel_yellow
            elif index == 3:
                screen[x][y] = pastel_green
            elif index == 4:
                screen[x][y] = pastel_blue
            elif index == 5:
                screen[x][y] = pastel_purple
    return screen


def pastel_random():
    screen = whole_screen(black)
    for x in range(height):
        for y in range(width):
            screen[x][y] = pastels[random.randint(0, 5)]
    return screen


def staggered_odd(color, background):
    screen = background
    for x in range(height):
        for y in range(width):
            if (x + y) % 2 == 0:
                screen[x][y] = color
    return screen


def staggered_even(color, background):
    screen = background
    for x in range(height):
        for y in range(width):
            if (x + y) % 2 == 1:
                screen[x][y] = color
    return screen


def confetti():
    animation = []

    for x in range(6):
        screen = staggered_even(white, pastel_random())
        animation.append(screen)
        screen = staggered_odd(white, pastel_random())
        animation.append(screen)

    return animation


if __name__ == '__main__':

    api = ScreenApi(mock=True)

    while True:
        for i in confetti():
            api.draw(i)
            time.sleep(0.1)
