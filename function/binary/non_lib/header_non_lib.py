from . import dilation
from . import erosion
from . import opening
from . import closing
from . import hit_or_miss
from . import boundary_extraction
from . import region_filling
from . import connect_components
from . import convex_hull
from . import thinning
from . import thickening
from . import skeletons
from . import pruning
from . import reconstruction
import numpy as np
import cv2
def gray2binary(gray):
    return (127 < gray) & (gray <= 255)
def binary_morphology(image, structuring_element, typeofOperator = "Dilation"):
    result = np.zeros_like(image)
    if (typeofOperator == "Dilation"):
        return dilation.dilation(image, structuring_element = structuring_element)
    elif (typeofOperator == "Erosion"): 
        return erosion.erosion(image, structuring_element= structuring_element)
    elif (typeofOperator == "Opening"):
        return opening.opening(image, structuring_element = structuring_element)
    elif (typeofOperator == "Closing"):
        return closing.closing(image, structuring_element = structuring_element)
    elif (typeofOperator == "Hit or Miss"): 
        return hit_or_miss.hit_or_miss(image, structuring_element)
    elif (typeofOperator == "Boundary Extraction"):
        return boundary_extraction.boundary_extraction(image, structuring_element)
        
    elif (typeofOperator == "Region Filling"): 
        # Invert floodfilled image
        floodfilled_image = region_filling.region_fill(gray2binary(image))
        image_copy = floodfilled_image.astype(np.uint8)
        
        im_floodfill_inv = cv2.bitwise_not(image_copy)
        print (im_floodfill_inv)
        # Combine the two images to get the foreground.
        im_out = gray2binary(image) | (im_floodfill_inv -254)
        return  im_out

    elif (typeofOperator == "Extraction of Connected Components"): 

        # Convert the image to binary using the threshold
        binary_image = gray2binary(image)

        num_labels, labels = connect_components.connect_components(image)

        # Create an output image where each component has a different color
        output_image = np.zeros((binary_image.shape[0], binary_image.shape[1], 3), dtype=np.uint8)

        # Map component labels to colors
        for label in range(1, num_labels):
            mask = labels == label
            output_image[mask] = np.random.randint(0, 255, size=3)
        return output_image

    elif (typeofOperator == "Convex Hull"):
        return convex_hull.convex_hull(image)
    elif (typeofOperator == "Thinning"): 

        return thinning.thinning(gray2binary(image))
    elif (typeofOperator == "Thickening"): 
        return thickening.thickening(image)
    elif (typeofOperator == "Skeletons"): 
        return skeletons.skeletons(image,structuring_element)
    elif (typeofOperator == "Reconstruction"): 
        return reconstruction.reconstruction(image, structuring_element)
    elif (typeofOperator == "Pruning"): 
        return pruning.prune(image)
    
    return result