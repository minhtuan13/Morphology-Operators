from . import dilation
from . import erosion

def closing (image, structuring_element):
    closed_image = dilation.dilation(image, structuring_element)
    closed_image = erosion.erosion(closed_image, structuring_element)
    return closed_image