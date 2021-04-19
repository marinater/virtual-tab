from threading import Thread
from .process import tracking_loop
import numpy as np

class Tracking:
    def __init__(self):
        self.position = (0, 0)
        self._cornersRaw = []
        self.corners = None
        self.tabletPoly = None

    def clearCorners(self):
        self._cornersRaw = None
        self.corners = None
        self.tabletPoly = None

    def setCorner(self):
        self._cornersRaw.append(self.position)
        if len(self._cornersRaw) == 4:
            self.corners = self._cornersRaw
            self._cornersRaw = []

            tablet = self.corners[:]
            tablet.append(tablet[0])
            self.tabletPoly = [np.array(tablet, dtype=np.int32).reshape((-1,1,2))]


    def start(self):
        # trackingThread = Thread(target=tracking_loop, args= (self,))
        # trackingThread.start()
        tracking_loop(self)
