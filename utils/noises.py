import cv2
import numpy as np


def add_no_noise(image, **kwargs):
    return image  # No noise added by default


def add_salt_pepper_noise(image: np.ndarray, *, 
                          prob: float = 0.1,
                          seed = None,
                          **kwargs) -> np.ndarray:
    assert 0 <= prob and prob <= 1, 'Probability must be between 0 and 1'
    rng = np.random.RandomState(seed)
    noise = rng.random(image.shape)
    output = np.copy(image)
    output[noise < prob] = 0  # Add salt
    output[noise > 1 - prob] = 1  # Add pepper
    return output


def add_gaussian_noise(image: np.ndarray, *, scale = 25, seed = None,
                       **kwargs) -> np.ndarray:
    rng = np.random.RandomState(seed)
    noise = rng.normal(loc=0, scale=scale, size=image.shape[:2])
    noise = np.array([noise] * 3).transpose((1, 2, 0))
    noise = np.astype(noise, np.int16)
    output = np.astype(image, np.int16)
    output += noise
    output = np.clip(output, 0, 255)
    output = np.astype(output, np.uint8)
    return output


_NOISES = {
    '(No noise)': add_no_noise,
    'Salt & pepper noise': add_salt_pepper_noise,
    'Gaussian noise': add_gaussian_noise,
}


def get_noise_names():
    return list(_NOISES.keys())


def get_noise_adder(noise_name: str):
    return _NOISES.get(noise_name, None)

