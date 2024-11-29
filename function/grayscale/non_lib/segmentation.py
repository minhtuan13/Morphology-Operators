from . import closing
from . import opening
def texture_segmentation(image, structuring_element):
    closed_img = closing.closing(image, structuring_element)
    return opening.opening(closed_img, structuring_element)