import numpy as np
from . import dilation
def reconstruction(image, structuring_element):

    mask = dilation.dilation(image, structuring_element)

    # Ensure the marker is less than or equal to the mask
    marker = np.minimum(image, mask)
    
    prev_marker = np.zeros_like(marker)
    while not np.array_equal(marker, prev_marker):
        prev_marker = marker
        marker = dilation.dilation(marker,  structuring_element)
        marker = np.minimum(marker, mask)
    
    return marker