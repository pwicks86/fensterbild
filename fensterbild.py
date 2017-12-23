from screenapi import ScreenApi
import time


def default():
    animation = []
    for r in range(12):
        for c in range(13):
            screen = [[(0, 0, 0) for x in range(13)] for y in range(12)]
            screen[r][c] = (255, 255, 255)
            animation.append(screen)
    return animation


if __name__ == '__main__':

    api = ScreenApi(mock=True)

    while True:
        for i in default():
            api.draw(i)
            time.sleep(0.1)
