import numpy as np
from PIL import Image
import cv2
import time
import pyautogui

# Game Process Name
process_name = 'Studio Code'


def enum_win(hwnd, result):  # All Process
    win_text = win32gui.GetWindowText(hwnd)
    process_list.append((hwnd, win_text))


win32gui.EnumWindows(enum_win, toplist)  # Find Game Process From All Process
game_hwnd = 0
for (hwnd, win_text) in process_list:
    if process_name in win_text:
        game_hwnd = hwnd


def grab_screen():
    # Position of Our Game Window
    position = win32gui.GetWindowRect(game_hwnd)
    # Take Screenshot
    screenshot = ImageGrab.grab(position)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    return screenshot

# Moving Functions


def forward():
    pyautogui.keyDown('w')
    pyautogui.keyUp('w')


def left():
    pyautogui.keyDown('a')
    pyautogui.keyDown('w')
    pyautogui.keyUp('a')
    pyautogui.keyUp('w')


def right():
    pyautogui.keyDown('d')
    pyautogui.keyDown('w')
    pyautogui.keyUp('d')
    pyautogui.keyUp('w')


def back():
    pyautogui.keyDown('s')
    pyautogui.keyUp('s')


# load Model

# LOOP
    # load image
    # preProcess image
    # pred
    # call appropriate motion function
