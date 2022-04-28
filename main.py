import pyvjoy
import pyautogui
import time
import pygame

# 1 : A
# 2 : B
# 3 : UP
# 4 : LEFT
# 5 : DOWN
# 6 : RIGHT
# 7 : L
# 8 : R
# 9 : START
# 10 : SELECT
j = pyvjoy.VJoyDevice(1)
frame = 1 / 30


def a():
    time.sleep(frame)
    j.set_button(1, 1)
    time.sleep(frame)
    j.set_button(1, 0)


def b():
    time.sleep(frame)
    j.set_button(2, 1)
    time.sleep(frame)
    j.set_button(2, 0)


def up():
    time.sleep(frame)
    j.set_button(3, 1)
    time.sleep(frame)
    j.set_button(3, 0)


def left():
    time.sleep(frame)
    j.set_button(4, 1)
    time.sleep(frame)
    j.set_button(4, 0)


def down():
    time.sleep(frame)
    j.set_button(5, 1)
    time.sleep(frame)
    j.set_button(5, 0)


def right():
    time.sleep(frame)
    j.set_button(6, 1)
    time.sleep(frame)
    j.set_button(6, 0)


# left shoulder
def ls():
    time.sleep(frame)
    j.set_button(7, 1)
    time.sleep(frame)
    j.set_button(7, 0)


# right shoulder
def rs():
    time.sleep(frame)
    j.set_button(8, 1)
    time.sleep(frame)
    j.set_button(8, 0)


def start():
    time.sleep(frame)
    j.set_button(9, 1)
    time.sleep(frame)
    j.set_button(9, 0)


def select():
    time.sleep(frame)
    j.set_button(10, 1)
    time.sleep(frame)
    j.set_button(10, 0)


def soft_reset():
    j.reset_buttons()
    time.sleep(frame)
    j.set_button(1, 1)
    j.set_button(2, 1)
    j.set_button(9, 1)
    j.set_button(10, 1)
    time.sleep(frame)
    j.reset_buttons()


def open_app():
    # Open Epilogue Operator.
    pyautogui.click(854, 1421)
    # Launch game.
    time.sleep(4)
    pyautogui.click(1112, 766)
    time.sleep(2)


def mash_a(n):
    i = 0
    while i < n:
        a()
        i += 1


def restart_game():
    mash_a(40)
    time.sleep(1)
    down()
    mash_a(280)


def name_player():
    time.sleep(0.8)
    right()
    right()
    right()
    right()
    a()
    left()
    left()
    left()
    left()
    down()
    down()
    a()
    right()
    right()
    right()
    right()
    up()
    up()
    a()
    down()
    down()
    right()
    a()
    right()
    right()
    right()
    right()
    up()
    up()
    a()
    down()
    left()
    left()
    left()
    left()
    a()
    left()
    left()
    up()
    a()
    start()
    mash_a(160)
    time.sleep(9)


if __name__ == '__main__':
    j.reset_buttons()
    open_app()
    restart_game()
    name_player()

