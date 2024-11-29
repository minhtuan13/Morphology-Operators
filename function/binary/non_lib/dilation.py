import numpy as np
def dilation(image, structuring_element):
     # Get dimensions of the image and the structuring element
    image_height, image_width = image.shape
    struct_height, struct_width = structuring_element.shape
    
    # Pad the image to handle border pixels
    padded_image = np.pad(image, ((struct_height//2, struct_height//2), (struct_width//2, struct_width//2)), mode='constant')
    
    # Initialize an empty array to store the dilated image
    dilated_image = np.zeros_like(image)
    
    # Loop through each pixel in the image
    for i in range(image_height):
        for j in range(image_width):
            # Apply the structuring element to the neighborhood of the current pixel
            neighborhood = padded_image[i:i+struct_height, j:j+struct_width]
            dilation_result = np.logical_and(neighborhood, structuring_element)
            # Set the corresponding pixel in the dilated image to 1 if any element in the result is True
            dilated_image[i, j] = np.any(dilation_result)
    
    return dilated_image