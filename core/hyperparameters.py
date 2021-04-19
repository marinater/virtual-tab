import json
import cv2

class Hyperparameters:
    def __init__(self):
        self.importHyperparameters()

    def importHyperparameters(self):
        with open('./settings/hyperparameters.json') as f:
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

            print(self.thresh_pen_min, self.thresh_pen_max)
        return updatePenThresholds

title_window = 'output'
cv2.namedWindow(title_window)

params = Hyperparameters()

cv2.createTrackbar(
    'H - Min', title_window,
    0, 180,
    params.updatePenThresholdsCallback(False, 0)
)

cv2.createTrackbar(
    'H - Max', title_window,
    180, 180,
    params.updatePenThresholdsCallback(True, 0)
)

cv2.createTrackbar(
    'S - Min', title_window,
    0, 180,
    params.updatePenThresholdsCallback(False, 1)
)

cv2.createTrackbar(
    'S - Max', title_window,
    255, 255,
    params.updatePenThresholdsCallback(True, 1)
)

cv2.createTrackbar(
    'V - Min', title_window,
    0, 255,
    params.updatePenThresholdsCallback(False, 2)
)

cv2.createTrackbar(
    'V - Max', title_window,
    255, 255,
    params.updatePenThresholdsCallback(True, 2)
)
