import cv2
import numpy as np
from PIL import ImageGrab
import pythoncom
import pywintypes
import win32gui
from pynput import keyboard
import os

process_list = []
toplist = []

# Game Process Name
process_name = 'Studio Code'


# Keys used in game
keys = {
    'w': 0,
    'a': 0,
    's': 0,
    'd': 0
}

# Make Dirs
for key in keys:
    try:
        data_path = 'data/' + key
        os.makedirs(data_path)
    except:
        pass


def enum_win(hwnd, result):  # All Process
    win_text = win32gui.GetWindowText(hwnd)
    process_list.append((hwnd, win_text))


win32gui.EnumWindows(enum_win, toplist)  # Find Game Process From All Process
game_hwnd = 0
for (hwnd, win_text) in process_list:
    if process_name in win_text:
        game_hwnd = hwnd


def save_screen(key, num):  # Take And Save ScreenShot
    # Position of Our Game Window
    position = win32gui.GetWindowRect(game_hwnd)
    # Take Screenshot
    screenshot = ImageGrab.grab(position)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    # Image Name
    img_dir = 'data/' + key + '/'+key + str(num) + '.jpg'
    # Save Screen Shot
    cv2.imwrite(img_dir, screenshot)


def on_press(key):  # Save One Key Press
    try:
        global keys
        keys[key.char] += 1
        save_screen(key.char, keys[key.char])

    except AttributeError:
        if (key == keyboard.Key.esc):
            for k in keys:
                print(k, ' : ', keys[k])
            return False


if __name__ == "__main__":
    # monitor keypress
    with keyboard.Listener(on_press) as listener:
        listener.join()
