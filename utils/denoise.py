import cv2
import numpy as np


def mean_denoise(image: np.ndarray, kernel_size: int) -> np.ndarray:
    mean_kernel = np.ones((kernel_size, kernel_size))
    mean_kernel /= kernel_size * kernel_size
    output = cv2.filter2D(src=image, ddepth=-1, kernel=mean_kernel)
    return output


def median_denoise(image: np.ndarray, kernel_size: int) -> np.ndarray:
    output = cv2.medianBlur(src=image, ksize=kernel_size)
    return output


_DENOISER = {
    'Denoise (mean)': mean_denoise,
    'Denoise (median)': median_denoise,
}


def get_denoiser_names():
    return list(_DENOISER.keys())


def get_denoiser(denoiser_name: str):
    return _DENOISER.get(denoiser_name, None)
