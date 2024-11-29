from . import opening
from . import closing

def granulometry (image, structuring_element):
    closed = closing.closing(image, structuring_element)
    opened = opening.opening(image, structuring_element)
    return closed - opened