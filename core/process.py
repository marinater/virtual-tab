from .image_io import ImageIO
from .hyperparameters import params
import numpy as np
import cv2

io = ImageIO()

def round_tuple(x):
    return int(round(x[0])), int(round(x[1]))

def process_frame(tracker):
    image_in = io.get_frame()

    image_hsv = cv2.cvtColor(image_in, cv2.COLOR_BGR2HSV)
    image_thresh = cv2.inRange(image_hsv, params.thresh_pen_min, params.thresh_pen_max)
    image_thresh = cv2.morphologyEx(image_thresh, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))

    image_thresh_overlayed = image_in.copy()
    image_thresh_overlayed[image_thresh == 255, :] = (0, 0, 255)
    # io.show_frame('thresholded', image_thresh_overlayed)

    count, labeled, stats, centroids = cv2.connectedComponentsWithStats(image_thresh, 4, cv2.CV_32S)
    if count > 1:
        largest_label = np.argmax(stats[1:, cv2.CC_STAT_AREA]) + 1
        pen_center = centroids[largest_label]

        image_thresh_overlayed[labeled == largest_label, :] = (255, 100, 0)
        cv2.drawMarker(image_thresh_overlayed, round_tuple(pen_center), (100, 255, 0), cv2.MARKER_CROSS, 10, 2)
        tracker.setPosition(pen_center)

    if not tracker.tabletPoly is None:
        cv2.polylines(image_thresh_overlayed, tracker.tabletPoly, True, (255, 255, 255), 2)

    return io.show_frame('output', image_thresh_overlayed, wait=True, tracker=tracker)

def tracking_loop(tracker):
    while process_frame(tracker):
        pass
