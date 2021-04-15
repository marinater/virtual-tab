from .image_io import ImageIO
import numpy as np
import cv2

io = ImageIO()

def process_frame(image):
    return cv2.rotate(image, cv2.ROTATE_180)

def run():
    while True:
        image_in = io.get_frame()
        io.show_frame('input', image_in)

        image_out = process_frame(image_in)
        if io.show_frame('output', image_out, wait=True):
            break
