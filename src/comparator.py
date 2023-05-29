import cv2
import numpy as np
import sys
import os

# For pyinstaller to include fish image when building
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        return os.path.join(os.path.abspath("."), relative_path)

fish_caught_path = resource_path('FishingImages/fish_caught.png')
fish_caught_image = cv2.imread(fish_caught_path, cv2.IMREAD_GRAYSCALE)

def check_fish_caught(fish_e_position):
    fish_caught_match = cv2.matchTemplate(fish_e_position, fish_caught_image, cv2.TM_CCOEFF_NORMED)

    if np.max(fish_caught_match) > 0.95:
        return True
    
    return False