from .fps import FPS
from .image_io import ImageIO
import cv2

def run():
    io = ImageIO()

    while True:
        image = io.get_frame()
        if io.show_frame('input', image, wait=True):
            break
