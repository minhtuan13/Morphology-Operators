import numpy as np

from scipy.ndimage import label, find_objects, binary_dilation

def find_seed_bounding_box_center(image):
    """
    Find the seed point as the center of the bounding box of the foreground region.
    
    Parameters:
    image: np.ndarray
        The binary input image.
        
    Returns:
    seed_point: tuple
        The (row, column) coordinates of the seed point.
    """
    labeled_image, num_features = label(image)
    slices = find_objects(labeled_image)
    
    # Assuming the first labeled object is the target region
    if slices:
        bbox = slices[0]
        bbox_center = ((bbox[0].start + bbox[0].stop) // 2, (bbox[1].start + bbox[1].stop) // 2)
        return bbox_center
    else:
        raise ValueError("No foreground region found in the image.")

def region_fill(image):
    """
    Perform region filling on the binary image using the given structuring element.
    
    Parameters:
    image: np.ndarray
        The binary input image.
    structuring_element: np.ndarray
        The structuring element used for dilation.
        
    Returns:
    np.ndarray
        The filled binary image.
    """
    structuring_element = np.array([[0, 1, 0],
                                    [1, 1, 1],
                                    [0, 1, 0]], dtype=int)
    seed_point = find_seed_bounding_box_center(image)
    print("Seed point:", seed_point)
    
    # Create a marker image with the seed point
    marker = np.zeros_like(image)
    marker[seed_point] = 1
    
    # Iteratively dilate the marker image and intersect with the original image complement
    prev_marker = np.zeros_like(marker)
    while not np.array_equal(marker, prev_marker):
        prev_marker = marker.copy()
        marker = binary_dilation(marker, structure=structuring_element)
        marker = marker & ~image
    
    # Combine the marker with the original image to get the filled region
    filled_image = marker | image
    
    return filled_image
        