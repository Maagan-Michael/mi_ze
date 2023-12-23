import cv2
import numpy as np


def format_yolov5(image_path):
    image = cv2.imread(image_path)
    row, col, _ = image.shape
    _max = max(col, row)
    result = np.zeros((_max, _max, 3), np.uint8)
    result[0:row, 0:col] = image
    return result