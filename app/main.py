#!/usr/bin/env python3
import random
import time

import pyautogui


def mouse_click(posx, posy, repeats, time_break, time_different):
    """Mouse clicks with random time delays.

    :param posx: x coordinate on screen
    :param posy: y coordinate on screen
    :param repeats: how many times function has to click
    :param time_break: average time of delay between clicks
    :param time_different: time deviation from the average
    """
    for _ in range(repeats):
        pyautogui.click(posx, posy)
        time.sleep(time_break + random.uniform(-time_different, time_different))
