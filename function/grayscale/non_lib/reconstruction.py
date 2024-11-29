
import numpy as np 
# Define dilation function
def dilation(image, structuring_element):
    pad_width = structuring_element.shape[0] // 2
    padded_image = np.pad(image, pad_width, mode='edge')
    dilated_image = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_image[i:i + structuring_element.shape[0], j:j + structuring_element.shape[1]]
            dilated_image[i, j] = np.max(region * structuring_element)

    return dilated_image

# Define reconstruction by dilation function
def reconstruction_dilation(marker, mask, structuring_element):
    current_image = marker.copy()
    prev_image = np.zeros_like(marker)

    while not np.array_equal(current_image, prev_image):
        prev_image = current_image.copy()
        dilated_image = dilation(current_image, structuring_element)
        current_image = np.minimum(dilated_image, mask)

    return current_image