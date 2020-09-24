import cv2
import numpy as np
from PIL import ImageGrab
import pythoncom
import pywintypes
import win32gui
from pynput import keyboard
import os

windows_list = []
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
    windows_list.append((hwnd, win_text))


win32gui.EnumWindows(enum_win, toplist)  # Find Game Process From All Process
game_hwnd = 0
for (hwnd, win_text) in windows_list:
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
        # if (key.char == 'w'):
        #     global num
        #     keys[key.char] += 1
        #     save_screen('w', keys[key.char])

        # if (key.char == 'a'):
        #     global a_num
        #     a_num += 1
        #     save_screen('a', w_num)

        # if (key.char == 's'):
        #     global s_num
        #     s_num += 1
        #     save_screen('s', w_num)

        # if (key.char == 'd'):
        #     global d_num
        #     d_num += 1
        #     save_screen('d', w_num)

    except AttributeError:
        if (key == keyboard.Key.esc):
            print('w = ', w_num)
            print('a = ', a_num)
            print('s = ', s_num)
            print('d = ', d_num)
            return False


if __name__ == "__main__":
    # monitor keypress
    with keyboard.Listener(on_press) as listener:
        listener.join()
