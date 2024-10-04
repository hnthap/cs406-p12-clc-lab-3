import cv2
import numpy as np


def sharpen_image(image: np.ndarray):
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    output = cv2.filter2D(image, -1, kernel)
    return output
