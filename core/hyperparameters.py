import json
import cv2

class Hyperparameters:
    def __init__(self):
        self.importParameters()

    def importParameters(self):
        with open('./settings/hyperparameters.json', 'r') as f:
            params = json.load(f)

        self.thresh_pen_min = tuple(params['thresh_pen_min'])
        self.thresh_pen_max = tuple(params['thresh_pen_max'])

    def exportParameters(self, value):
        with open('./settings/hyperparameters2.json', 'w') as f:
            exported_params = {
                'thresh_pen_min': self.thresh_pen_min,
                'thresh_pen_max': self.thresh_pen_max
            }
            json.dump(exported_params, f, indent=4)

    def updatePenThresholdsCallback(self, updateMax, index):
        def updatePenThresholds(value):
            if updateMax:
                newMax = list(self.thresh_pen_max)
                newMax[index] = value
                self.thresh_pen_max = tuple(newMax)
            else:
                newMin = list(self.thresh_pen_min)
                newMin[index] = value
                self.thresh_pen_min = tuple(newMin)
        return updatePenThresholds

title_window = 'output'
cv2.namedWindow(title_window)

params = Hyperparameters()


cv2.createTrackbar(
    'Max - H', title_window,
    params.thresh_pen_max[0], 180,
    params.updatePenThresholdsCallback(True, 0)
)

cv2.createTrackbar(
    'Max - S', title_window,
    params.thresh_pen_max[1], 255,
    params.updatePenThresholdsCallback(True, 1)
)

cv2.createTrackbar(
    'Max - V', title_window,
    params.thresh_pen_max[2], 255,
    params.updatePenThresholdsCallback(True, 2)
)

cv2.createTrackbar(
    'Min - H', title_window,
    params.thresh_pen_min[0], 180,
    params.updatePenThresholdsCallback(False, 0)
)

cv2.createTrackbar(
    'Min - S', title_window,
    params.thresh_pen_min[1], 180,
    params.updatePenThresholdsCallback(False, 1)
)

cv2.createTrackbar(
    'Min - V', title_window,
    params.thresh_pen_min[2], 255,
    params.updatePenThresholdsCallback(False, 2)
)

cv2.createTrackbar(
    'Save', title_window,
    0, 1,
    params.exportParameters
)