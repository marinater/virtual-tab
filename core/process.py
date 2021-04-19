from .image_io import ImageIO
from .hyperparameters import params
import numpy as np
import cv2

io = ImageIO()

def process_frame(image_in):
    image_hsv = cv2.cvtColor(image_in, cv2.COLOR_BGR2HSV)
    image_thresh = cv2.inRange(image_hsv, params.thresh_pen_min, params.thresh_pen_max)
    image_thresh = cv2.morphologyEx(image_thresh, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))

    # image_thresh_overlayed = image_in.copy()
    # image_thresh_overlayed[image_thresh == 255, :] = (0, 0, 255)
    # io.show_frame('thresholded', image_thresh_overlayed)

    contours, hierarchy = cv2.findContours(image_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest_contour = max([(cv2.contourArea(contour), contour) for contour in contours], key= lambda x: x[0])
        print(largest_contour[0])

    return image_thresh

def run():
    while True:
        image_in = io.get_frame()
        # io.show_frame('input', image_in)

        image_out = process_frame(image_in)
        if io.show_frame('output', image_out, wait=True):
            break
