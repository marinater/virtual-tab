import cv2

class Hyperparameters:
    pen_thresholding_max = (0, 0, 0)
    pen_thresholding_min = (180, 255, 255)

    def updatePenThresholdsCallback(updateMax, index):
        def updatePenThresholds(value):
            if updateMax:
                newMax = list(Hyperparameters.pen_thresholding_max)
                newMax[index] = value
                Hyperparameters.pen_thresholding_max = tuple(newMax)
            else:
                newMin = list(Hyperparameters.pen_thresholding_min)
                newMin[index] = value
                Hyperparameters.pen_thresholding_min = tuple(newMin)

        return updatePenThresholds

title_window = 'Filtering Settings'
cv2.createTrackbar(
    'H - Max', title_window,
    0, 180,
    Hyperparameters.updatePenThresholdingMaxCallback(0)
)

cv2.createTrackbar(
    'H - Min', title_window,
    0, 180,
    Hyperparameters.updatePenThresholdingMaxCallback(0)
)

cv2.createTrackbar(
    'S - Max', title_window,
    0, 180,
    Hyperparameters.updatePenThresholdingMaxCallback(0)
)

cv2.createTrackbar(
    'S - Min', title_window,
    0, 180,
    Hyperparameters.updatePenThresholdingMaxCallback(0)
)

cv2.createTrackbar(
    'V - Max', title_window,
    0, 180,
    Hyperparameters.updatePenThresholdingMaxCallback(0)
)

cv2.createTrackbar(
    'V - Min', title_window,
    0, 180,
    Hyperparameters.updatePenThresholdingMaxCallback(0)
)
