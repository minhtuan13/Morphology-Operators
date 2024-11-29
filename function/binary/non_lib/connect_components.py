import numpy as np
from scipy.ndimage import find_objects
from scipy.ndimage import label, binary_dilation


def connect_components(binary_image):
    struct_elem = np.array([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]], dtype=int)

    label = 1
    labels = np.zeros_like(binary_image)
    
    # Copy the binary image
    working_image = binary_image.copy()
    
    while np.any(working_image):
        # Find a seed pixel
        seed = np.zeros_like(working_image)
        seed[np.unravel_index(np.argmax(working_image), working_image.shape)] = 1
        
        component = seed
        while True:
            new_component = binary_dilation(component, struct_elem)
            new_component = new_component & binary_image
            if np.array_equal(new_component, component):
                break
            component = new_component
        
        # Label the component
        labels[component == 1] = label
        working_image[component == 1] = 0
        label += 1
    
    return label - 1, labels
