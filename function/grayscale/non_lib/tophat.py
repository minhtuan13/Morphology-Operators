from . import opening
def tophat(image, structuring_element):
    opened_img = opening.opening(image, structuring_element)
    return image - opened_img