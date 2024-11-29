import numpy as np
def dilation (image, structuring_element): 
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
            # Initialize an empty array to store the values of the structuring element applied to the neighborhood
            neighborhood_values = []
            # Loop through each pixel in the structuring element
            for m in range(struct_height):
                for n in range(struct_width):
                    # Calculate the coordinates in the padded image
                    padded_i = i - struct_height // 2 + m
                    padded_j = j - struct_width // 2 + n
                    # Apply the structuring element to the neighborhood of the current pixel
                    if (0 <= padded_i < padded_image.shape[0]) and (0 <= padded_j < padded_image.shape[1]):
                        neighborhood_values.append(padded_image[padded_i, padded_j] + structuring_element[m, n])
            # Set the corresponding pixel in the dilated image to the maximum value in the neighborhood
            dilated_image[i, j] = max(neighborhood_values)
    return dilated_image