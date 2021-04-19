import cv2

class Hyperparameters:
    thresh_pen_min = (0, 0, 0)
    thresh_pen_max = (180, 255, 255)

    def updatePenThresholdsCallback(updateMax, index):
        def updatePenThresholds(value):
            if updateMax:
                newMax = list(Hyperparameters.thresh_pen_max)
                newMax[index] = value
                Hyperparameters.thresh_pen_max = tuple(newMax)
            else:
                newMin = list(Hyperparameters.thresh_pen_min)
                newMin[index] = value
                Hyperparameters.thresh_pen_min = tuple(newMin)
        return updatePenThresholds

title_window = 'Filtering Settings'
cv2.namedWindow(title_window)
cv2.createTrackbar(
    'H - Min', title_window,
    0, 180,
    Hyperparameters.updatePenThresholdsCallback(False, 0)
)

cv2.createTrackbar(
    'H - Max', title_window,
    180, 180,
    Hyperparameters.updatePenThresholdsCallback(True, 0)
)

cv2.createTrackbar(
    'S - Min', title_window,
    0, 180,
    Hyperparameters.updatePenThresholdsCallback(False, 1)
)

cv2.createTrackbar(
    'S - Max', title_window,
    255, 255,
    Hyperparameters.updatePenThresholdsCallback(True, 1)
)

cv2.createTrackbar(
    'V - Min', title_window,
    0, 255,
    Hyperparameters.updatePenThresholdsCallback(False, 2)
)

cv2.createTrackbar(
    'V - Max', title_window,
    255, 255,
    Hyperparameters.updatePenThresholdsCallback(True, 2)
)
