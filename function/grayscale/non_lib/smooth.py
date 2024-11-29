from . import opening
from . import closing

def smoothing(image, structuring_element):
    result = opening.opening(image, structuring_element)
    result = closing.closing(result, structuring_element)
    return result