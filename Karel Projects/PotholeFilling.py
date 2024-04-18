"""
File: PotholeFilling.py
Name: KeDuan
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    for i in range(3):
        into()
        put_123_beepers()
        leave()


def turn_right():
    for i in range(3):
        turn_left()


def into():
    """
    pre-condition:Karel is at the upper left of the pothole,facing East
    post-condition:Karel is in the pothole,facing South
    """
    move()
    turn_right()
    move()


def leave():
    """
    pre-condition:Karel is in the pothole,facing South
    post-condition:Karel is at the upper left of the pothole,facing East
    """
    for i in range(2):
        turn_left()
    move()
    turn_right()
    move()


def put_123_beepers():
    for i in range(123):
        put_beeper()


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
