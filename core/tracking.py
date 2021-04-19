class Tracking:
    def __init__(self):
        self.position = None
        self._cornersRaw = []
        self.corners = None

    def clearCorners(self):
        self._cornersRaw = None
        self.corners = None

    def setCorner(self, corner):
        self._cornersRaw.append(corner)
        if len(self._cornersRaw) == 4:
            self.corners = self._cornersRaw
            self._cornersRaw = []
