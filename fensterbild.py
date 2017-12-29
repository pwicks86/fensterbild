from screenapi import ScreenApi
import time
import math
import random
import argparse

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

pastel_red = (255, 200, 200)
pastel_yellow = (255, 255, 200)
pastel_green = (200, 255, 200)
pastel_blue = (200, 200, 255)
pastel_purple = (255, 200, 255)
pastels = [pastel_red, pastel_yellow, pastel_green,
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
            index = (math.floor((x + y) / 2) + frame) % len(pastels)
            screen[x][y] = pastels[index]
    return screen


def pastel_random():
    screen = whole_screen(black)
    for x in range(height):
        for y in range(width):
            screen[x][y] = pastels[random.randint(0, len(pastels) - 1)]
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

    parser = argparse.ArgumentParser(description='Control the pretty lights.')
    parser.add_argument('design', default='default', help='Options: confetti')

    args = parser.parse_args()

    design = []
    if args.design == 'confetti':
        design = confetti()
    elif args.design == default:
        design = default(white)
    else:
        design = default(white)

    api = ScreenApi(mock=True)

    while True:
        for i in design:
            api.draw(i)
            time.sleep(0.1)
