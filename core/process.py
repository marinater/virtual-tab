from .image_io import ImageIO
import cv2

io = ImageIO()

def run():
    while True:
        image = io.get_frame()
        if io.show_frame('input', image, wait=True):
            break
