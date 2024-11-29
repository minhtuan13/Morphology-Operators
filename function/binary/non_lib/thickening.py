import numpy as np
import cv2
def thickening(binary_image, iterations=1):
    # Ensure the binary image is in the correct format
    binary_image = binary_image.astype(np.uint8) * 255  # Convert to 0-255 range for OpenCV
    
    # Define a cross-shaped structuring element
    struct_elem = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    
    thickened_image = binary_image.copy()
    for _ in range(iterations):
        dilated = cv2.dilate(thickened_image, struct_elem)
        thickened_image = cv2.bitwise_or(thickened_image, dilated)
    
    return thickened_image