import cv2
import numpy as np 
from matplotlib import pyplot as plt


def hex_to_rgb(v):
        v = v.lstrip('#')
        lv = len(v)
        return list(int(v[i:i+lv//3], 16) for i in range(0, lv, lv//3))
        

def count_pixels(img, value):
    np_img = np.fromstring(img, np.uint8)
    jpg = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    try:
        hc = hex_to_rgb(value)
    except Exception as e:
        return 0

    c_white_pix = np.sum(jpg == 255)
    c_black_pix = np.sum(jpg == 0)    
    c_pix = np.sum(jpg == hc)

    return [c_white_pix, c_black_pix, c_pix]