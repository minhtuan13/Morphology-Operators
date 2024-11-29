import numpy as np
from . import erosion
def skeletons(image, structuring_element):
    skeleton = np.zeros(image.shape, dtype=bool)
    temp_image = image.copy()

    while True:
        eroded = erosion.erosion(temp_image, structuring_element)
        temp = np.logical_and(temp_image, np.logical_not(eroded))
        skeleton = np.logical_or(skeleton, temp)
        temp_image = eroded.copy()

        if np.sum(temp_image) == 0:
            break

    return skeleton *255