import numpy as np
def erosion(image, structuring_element):
    # Get dimensions of the image and the structuring element
    image_height, image_width = image.shape
    struct_height, struct_width = structuring_element.shape
    # Pad the image to handle border pixels
    padded_image = np.pad(image, ((struct_height//2, struct_height//2), (struct_width//2, struct_width//2)), mode='constant')
    
    # Create an empty array to store the result
    eroded_image = np.zeros_like(image)

    for i in range(image_height):
        for j in range(image_width):
            # Apply the structuring element to the neighborhood of the current pixel
            neighborhood = padded_image[i:i+struct_height, j:j+struct_width]
            erosion_result = np.logical_and(neighborhood, structuring_element)
            # Set the corresponding pixel in the eroded image to 1 if all elements in the result are True
            eroded_image[i, j] = np.all(erosion_result)
    
    return eroded_image