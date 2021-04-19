from .image_io import ImageIO
from .hyperparameters import Hyperparameters
import numpy as np
import cv2

io = ImageIO()

# H (0, 180)
# S (0, 255)
# V (0, 255)

def process_frame(image_in):
    image_hsv = cv2.cvtColor(image_in, cv2.COLOR_RGB2HSV)
    image_thresh = cv2.inRange(image_hsv, Hyperparameters.thresh_pen_min, Hyperparameters.thresh_pen_max)
    # io.show_frame('thresholded', image_thresh)
    image_out = image_in.copy()
    image_out[image_thresh == 255, 2] = 255
    return image_out

def run():
    while True:
        image_in = io.get_frame()
        # io.show_frame('input', image_in)

        image_out = process_frame(image_in)
        if io.show_frame('output', image_out, wait=True):
            break
