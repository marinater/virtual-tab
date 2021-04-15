import cv2
from .fps import FPS

class ImageIO:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.fps = FPS()
        self.prev_rate = 0

    # retrieve a single frame from the
    # webcam to process
    def get_frame(self):
        self.fps.start_frame()
        _, frame = self.cam.read()
        return frame

    # queues the image to be displayed by
    # the GUI. Does not actually dispaly
    # until the function is called with
    # wait=True. When wait=True, the
    # function will wait 1ms an listen to
    # check if the window recieved a kill
    # signal and return True if so.
    def show_frame(self, title, frame, wait=False):
        if wait:
            frame_copy = frame.copy()
            cv2.putText(frame_copy, f'{self.prev_rate:.0f} fps', (30, 30), cv2.FONT_HERSHEY_PLAIN, 1, 255)
            cv2.imshow(title, frame_copy)
        else:
            cv2.imshow(title, frame)

        if wait and cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            return True

        self.prev_rate = self.fps.stop_frame()
        return False
