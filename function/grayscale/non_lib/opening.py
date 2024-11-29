from . import dilation
from . import erosion

def opening (image, structuring_element):
    opend_image = erosion.erosion(image, structuring_element)
    opend_image = dilation.dilation(opend_image, structuring_element)
    return opend_image