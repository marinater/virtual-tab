from .image_io import ImageIO
from .hyperparameters import Hyperparameters
import numpy as np
import cv2

io = ImageIO()

# H (0, 180)
# S (0, 255)
# V (0, 255)

def process_frame(image_in):
    image_hsv = cv2.cvtColor(image_in, cv2.COLOR_BGR2HSV)
    image_thresh = cv2.inRange(image_hsv, Hyperparameters.thresh_pen_min, Hyperparameters.thresh_pen_min)
    # io.show_frame('thresholded', image_thresh)
    # image_overlay = np.zeros_like(image_in)
    # image_overlay[:,:,2] = image_thresh
    # image_out = cv2.addWeighted(image_in, 0.8, image_overlay, 0.2, 0)
    print(Hyperparameters.thresh_pen_min, Hyperparameters.thresh_pen_max)
    return image_thresh

def run():
    while True:
        image_in = io.get_frame()
        # io.show_frame('input', image_in)

        image_out = process_frame(image_in)
        if io.show_frame('output', image_out, wait=True):
            break
