from threading import Thread
from .process import round_tuple, tracking_loop
import numpy as np
import cv2
import pyautogui

w_max = 1920
h_max = 1080
def cvPointToScreenPoint(cv_point):
    row, col = map(lambda x: int(max(0, round(x))), cv_point)
    return min(w_max - 1, col), min(h_max - 1, row)

class Tracking:
    def __init__(self):
        self.position = (0, 0)
        self._cornersRaw = []
        self.corners = None
        self.tabletPoly = None
        self.transform = None

    def clearCorners(self):
        self._cornersRaw = None
        self.corners = None
        self.tabletPoly = None
        self.transform = None

    def setCorner(self):
        self._cornersRaw.append(self.position)
        if len(self._cornersRaw) == 4:
            self.corners = np.array(self._cornersRaw, dtype=np.float32)
            self._cornersRaw.append(self._cornersRaw[0])
            self.tabletPoly = [np.array(self._cornersRaw, dtype=np.int32).reshape((-1,1,2))]
            self._cornersRaw = []
            self.setTransform()

    def setTransform(self):
        if self.corners is None:
            return

        src = self.corners
        dst = np.array([
            [0, 0],
            [h_max - 1, 0],
            [h_max - 1, w_max - 1],
            [0, w_max - 1],
        ], dtype=np.float32)

        self.transform = cv2.getPerspectiveTransform(src, dst)

    def setPosition(self, position):
        self.position = position
        if self.transform is None:
            return

        src = np.array([[position]], dtype=np.float32)
        cvPoint = cv2.perspectiveTransform(src, self.transform)[0][0]
        screenPoint = cvPointToScreenPoint(cvPoint)
        pyautogui.moveTo(0, 0)

    def start(self):
        # trackingThread = Thread(target=tracking_loop, args= (self,))
        # trackingThread.start()
        tracking_loop(self)
