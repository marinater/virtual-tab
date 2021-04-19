from .image_io import ImageIO
from .hyperparameters import params
import numpy as np
import cv2

io = ImageIO()

def process_frame(image_in):
    image_hsv = cv2.cvtColor(image_in, cv2.COLOR_BGR2HSV)
    image_thresh = cv2.inRange(image_hsv, params.thresh_pen_min, params.thresh_pen_max)
    image_thresh = cv2.morphologyEx(image_thresh, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))

    image_thresh_overlayed = image_in.copy()
    image_thresh_overlayed[image_thresh == 255, :] = (0, 0, 255)
    # io.show_frame('thresholded', image_thresh_overlayed)

    count, labeled, stats, centroids = cv2.connectedComponentsWithStats(image_thresh, 4, cv2.CV_32S)
    if count > 1:
        largest_label = np.argmax(stats[1:, cv2.CC_STAT_AREA]) + 1
        print(largest_label, stats[largest_label, cv2.CC_STAT_AREA])

    # if contours:
    #     largest_contour_idx, largest_contour_area = max([
    #         (i, cv2.contourArea(contour))
    #         for i, contour
    #         in enumerate(contours)
    #     ], key= lambda x: x[1])

    #     cv2.drawContours(image_thresh_overlayed, contours, largest_contour_idx, (0, 255, 0), -1)

    return image_thresh_overlayed

def run():
    while True:
        image_in = io.get_frame()
        # io.show_frame('input', image_in)

        image_out = process_frame(image_in)
        if io.show_frame('output', image_out, wait=True):
            break
