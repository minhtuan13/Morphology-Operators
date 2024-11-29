import cv2.ximgproc
import cv2, numpy as np
from ..non_lib import region_filling
from skimage.morphology import skeletonize, reconstruction, thin
from skimage.filters import threshold_otsu
from skimage import measure
def binary_morphology(image, structuring_element, typeofOperator = "Dilation"):
    result = np.zeros_like(image)
    kernel = np.matrix(structuring_element, np.uint8) 
    if (typeofOperator == "Dilation"):
        return cv2.dilate(image, kernel, iterations = 1)
    elif (typeofOperator == "Erosion"): 
        return cv2.erode(image, structuring_element, iterations = 1)
    elif (typeofOperator == "Opening"):
        return cv2.morphologyEx(image, cv2.MORPH_OPEN, structuring_element)
    elif (typeofOperator == "Closing"):
        return cv2.morphologyEx(image, cv2.MORPH_CLOSE, structuring_element)
    elif (typeofOperator == "Hit or Miss"): 
        return cv2.morphologyEx(image, cv2.MORPH_HITMISS, structuring_element)
    elif (typeofOperator == "Boundary Extraction"):
        erode = cv2.erode(image, structuring_element, iterations = 1)  #co đối tượng lại
        return image - erode   #áp dụng công thức
    elif (typeofOperator == "Region Filling"): 
        # Make a copy of the input image to avoid modifying the original image
        image_copy = image.copy().astype(np.uint8)
        
        # Define the mask, with a 1-pixel border around the original image
        h, w = image_copy.shape
        mask = np.zeros((h+2, w+2), np.uint8)
        seedPoint = region_filling.find_seed_bounding_box_center(image)
        # Use floodFill to fill the region
        cv2.floodFill(image_copy, mask, seedPoint, newVal=255)
        # Invert floodfilled image
        im_floodfill_inv = cv2.bitwise_not(image_copy)
        
        # Combine the two images to get the foreground.
        im_out = image | im_floodfill_inv
        return im_out
    elif (typeofOperator == "Extraction of Connected Components"): 
        threshold_value = threshold_otsu(image)

        # Convert the image to binary using the threshold
        binary_image = image > threshold_value

        num_labels, labels = cv2.connectedComponents(image)

        # Create an output image where each component has a different color
        output_image = np.zeros((binary_image.shape[0], binary_image.shape[1], 3), dtype=np.uint8)

        # Map component labels to colors
        for label in range(1, num_labels):
            mask = labels == label
            output_image[mask] = np.random.randint(0, 255, size=3)
        return output_image
    
    elif (typeofOperator == "Convex Hull"):
        blur = cv2.blur(image, (3, 3)) #blur the image

        _, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY) #apply binary thresholding for blur

        # tìm contour trong ảnh threshhold
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        # Tìm Convex Hull của các contour
        hull = []
        for i in range(len(contours)):
            hull.append(cv2.convexHull(contours[i], False))
        
        # Vẽ Convex Hull lên hình ảnh gốc
        # create an empty black image
        drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
        
        # draw contours and hull points
        for i in range(len(contours)):
            color_contours = (0, 255, 0) # green - color for contours
            color = (255, 0, 0) # blue - color for convex hull
            # draw ith contour
            cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
            # draw ith convex hull object
            cv2.drawContours(drawing, hull, i, color, 1, 8)
        return drawing
    elif (typeofOperator == "Thinning"): 
        thinning_image= thin(image)
        result = np.zeros_like(thinning_image, dtype=np.uint8)
        result[thinning_image] = 255
        return result
        
    elif (typeofOperator == "Thickening"): 
        return result
    elif (typeofOperator == "Skeleton"): 
        skeleted =  skeletonize(image)
        result = np.zeros_like(skeleted, dtype=np.uint8)
        result[skeleted] = 255
        return result
    elif (typeofOperator == "Reconstruction"): 
        threshold_value = threshold_otsu(image)

        # Convert the image to binary using the threshold
        binary_image = image > threshold_value
        mask = np.resize(structuring_element, binary_image.shape)
        seed = np.zeros_like(binary_image)
        seed[mask > 0] = binary_image[mask > 0]

        return reconstruction(seed, binary_image,method='dilation')*255
    elif (typeofOperator == "Pruning"): 
        return result
    
    return result