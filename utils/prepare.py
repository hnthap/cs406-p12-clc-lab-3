from PIL import Image
import numpy as np


def prepare_image(image_file, new_height = 1024) -> np.ndarray:
    image = Image.open(image_file)
    assert isinstance(image, Image.Image), 'Image must exist'
    image = image.convert('RGB')
    if new_height is not None:
        width, height = image.size
        new_width = int(round(new_height * width / height))
        image = image.resize((new_width, new_height))
    return np.asarray(image)
