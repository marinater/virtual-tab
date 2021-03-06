from threading import Thread
from .process import round_tuple, tracking_loop
import numpy as np
import cv2
import pyautogui

# pyautogui introduces a failsafe whereby moving your mouse
# to any corner for more than 1ms causes the program to abort
# to maximise fps, we remove this wait. Fear not, though, because
# cv2.waitKey(1) does this for us already
pyautogui.PAUSE = 0

# window dimensions. In the future, we should get these dynamically
# from the system
w_max = 1920
h_max = 1080

# a function to santize cv2 friendly points and use them with pyautogui
def cvPointToScreenPoint(cv_point):
    row, col = map(lambda x: int(max(0, round(x))), cv_point)
    return min(w_max - 1, col), min(h_max - 1, row)

# class that stores mouse and tablet positions as well as moves the mouse
# when tracking is on
class Tracking:
    # initialize everything to defaults
    def __init__(self):
        self.position = (0, 0)
        self._cornersRaw = []
        self.corners = None
        self.tabletPoly = None
        self.transform = None

    # reset tablet tracking
    def clearCorners(self):
        self._cornersRaw = None
        self.corners = None
        self.tabletPoly = None
        self.transform = None

    # add one corner to the array of points representing a tablet
    def setCorner(self):
        self._cornersRaw.append(self.position)
        if len(self._cornersRaw) == 4:
            self.corners = np.array(self._cornersRaw, dtype=np.float32)
            self._cornersRaw.append(self._cornersRaw[0])
            self.tabletPoly = [
                np.array(self._cornersRaw, dtype=np.int32).reshape((-1, 1, 2))
            ]
            self._cornersRaw = []
            self.setTransform()

    # once the tablet region is defined, precompute the perspective transform
    # needed to map a point into screen coordinates
    def setTransform(self):
        if self.corners is None:
            return

        src = self.corners
        dst = np.array(
            [
                [0, 0],
                [h_max - 1, 0],
                [h_max - 1, w_max - 1],
                [0, w_max - 1],
            ],
            dtype=np.float32,
        )

        self.transform = cv2.getPerspectiveTransform(src, dst)
        pyautogui.sleep(0.5)

    # update the mouse position
    def setPosition(self, position):
        self.position = position
        if self.transform is None:
            return

        src = np.array([[position]], dtype=np.float32)
        cvPoint = cv2.perspectiveTransform(src, self.transform)[0][0]
        screenPoint = cvPointToScreenPoint(cvPoint)
        print(screenPoint)
        pyautogui.moveTo(*screenPoint)

    # start tracking the mouse
    # in the future, this can be made threaded if we move away from cv2.imshow
    # for displaying images. We are currently unable to thread since cv2.imshow
    # must be called on the main thread
    def start(self):
        # trackingThread = Thread(target=tracking_loop, args= (self,))
        # trackingThread.start()
        tracking_loop(self)
