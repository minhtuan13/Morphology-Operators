import numpy as np
def is_endpoint(image, x, y):
    # Get 3x3 neighborhood
    neighborhood = image[x-1:x+2, y-1:y+2]
    return np.sum(neighborhood) == 255 * 2  # Center pixel + one neighbor

def prune(binary_image, iterations=1):
    pruned_image = (binary_image.copy()) /255
    for _ in range(iterations):
        endpoints = []
        
        # Find all endpoints
        for i in range(1, pruned_image.shape[0] - 1):
            for j in range(1, pruned_image.shape[1] - 1):
                if pruned_image[i, j] == 255 and is_endpoint(pruned_image, i, j):
                    endpoints.append((i, j))
        
        # Remove all endpoints
        for i, j in endpoints:
            pruned_image[i, j] = 0
    
    return pruned_image