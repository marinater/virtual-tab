import cv2

class ImageIO:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)

    # retrieve a single frame from the
    # webcam to process
    def get_frame(self):
        ret, frame = self.cam.read()
        return frame

    # queues the image to be displayed by
    # the GUI. Does not actually dispaly
    # until the function is called with
    # wait=True. When wait=True, the
    # function will wait 1ms an listen to
    # check if the window recieved a kill
    # signal and return True if so.
    def show_frame(self, title, frame, wait=False):
        cv2.imshow(title, frame)

        if wait and cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            return True

        return False
