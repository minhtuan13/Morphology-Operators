from . import erosion
def boundary_extraction (image, structuring_element):
    erode = erosion.erosion(image, structuring_element)  #co đối tượng lại
    return image/255 - erode