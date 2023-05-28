from time import sleep
import cv2
import numpy as np

fish_caught = cv2.imread('FishingImages\\fish_caught.png')
fish_caught = cv2.cvtColor(fish_caught, cv2.COLOR_BGR2GRAY)

def check_fish_caught(fish_e_position):
    fish_caught_match = cv2.matchTemplate(fish_e_position, fish_caught, cv2.TM_CCOEFF_NORMED)

    if np.max(fish_caught_match) > 0.95:
        return True
    
    return False