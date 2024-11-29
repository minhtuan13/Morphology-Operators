from . import dilation
from . import erosion

def gradient (image, structuring_element):
    dialated_img = dilation.dilation(image, structuring_element)
    eroded_img = erosion.erosion(image, structuring_element)
    return dialated_img - eroded_img
