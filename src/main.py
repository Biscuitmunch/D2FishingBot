from time import sleep
import cv2
import pyautogui
import numpy as np
import mss
import comparator
import areas

sct = mss.mss()

def obtain_fish_input():
    print('caught!')
    pyautogui.keyDown('e')
    sleep(3)
    pyautogui.keyUp('e')

def restart_fishing_input():
    pyautogui.keyDown('e')
    sleep(1.5)
    pyautogui.keyUp('e')

def restart_fishing_check(): 
    pass

while(True):
    print('fishing...')
    fish_e_position = areas.fish_e_position.copy()

    fish_e_check = np.array(sct.grab(fish_e_position))
    fish_e_check = cv2.cvtColor(fish_e_check, cv2.COLOR_BGRA2GRAY)
    fish_caught = comparator.check_fish_caught(fish_e_check)

    if (fish_caught == True):
        obtain_fish_input()
        restart_fishing_input()