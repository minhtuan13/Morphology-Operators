import cv2
import numpy as np
from skimage.morphology import reconstruction, dilation, square
def grayscale_morphology(image, structuring_element, typeofOperator = "Dilation"):
    result = np.zeros_like(image)
    if (typeofOperator == "Dilation"):
        return cv2.dilate(image, structuring_element)
    elif (typeofOperator == "Erosion"): 
        return cv2.erode(image, structuring_element)
    elif (typeofOperator == "Opening"):
        return cv2.morphologyEx(image, cv2.MORPH_OPEN, structuring_element)
    elif (typeofOperator == "Closing"):
        return cv2.morphologyEx(image, cv2.MORPH_CLOSE, structuring_element)
    elif (typeofOperator == "Smoothing"):
        opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, structuring_element)
        return cv2.morphologyEx(opened, cv2.MORPH_CLOSE, structuring_element)
    elif (typeofOperator == "Gradient"): 
        return cv2.morphologyEx(image, cv2.MORPH_GRADIENT, structuring_element)
    elif (typeofOperator == "Top Hat"): 
        return cv2.morphologyEx(image, cv2.MORPH_TOPHAT, structuring_element)
    elif (typeofOperator ==  "Textual segmentation"): 
        closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, structuring_element)
        return cv2.morphologyEx(closed, cv2.MORPH_OPEN, structuring_element)
    elif (typeofOperator == "Granulometry"): 
        closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, structuring_element)
        opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, structuring_element)
        return closed - opened
    elif (typeofOperator == "Reconstruction"): 
        seed = np.copy(image)
        seed[1:-1, 1:-1] = image.min()
        # dilated = dilation(seed, square(3))
        reconstructed = reconstruction(seed, image, method='dilation')
        return reconstructed 
    return result
