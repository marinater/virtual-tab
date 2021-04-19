from threading import Thread
from .process import tracking_loop
import numpy as np
import cv2

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

        w = 1920
        h = 1080

        src = self.corners
        dst = np.array([
            [0, 0],
            [h - 1, 0],
            [h - 1, w - 1],
            [0, w - 1],
        ], dtype=np.float32)

        self.transform = cv2.getPerspectiveTransform(src, dst)

    def setPosition(self, position):
        self.position = position
        if self.transform is None:
            return

        src = np.array([[position]], dtype=np.float32)
        res = cv2.perspectiveTransform(src, self.transform)
        print(res[0])

    def start(self):
        # trackingThread = Thread(target=tracking_loop, args= (self,))
        # trackingThread.start()
        tracking_loop(self)
