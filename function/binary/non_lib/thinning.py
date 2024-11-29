import numpy as np
"""
Zhang-Suen thinning algorithm
"""
def neighbours(x, y, image):
    """Return 8-neighbours of image point P1(x,y), in a clockwise order"""
    img = image
    return [img[x-1, y], img[x-1, y+1], img[x, y+1], img[x+1, y+1], img[x+1, y], 
            img[x+1, y-1], img[x, y-1], img[x-1, y-1]]


def transitions(neighbours):
    """No. of 0,1 patterns (transitions from 0 to 1) in the ordered sequence of neighbours"""
    n = neighbours + neighbours[0:1]  # to create a cyclic sequence
    return sum((n1, n2) == (0, 1) for n1, n2 in zip(n, n[1:]))


def thinning_iteration(image, iter):
    marker = np.zeros(image.shape, dtype=np.uint8)
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            P2, P3, P4, P5, P6, P7, P8, P9 = neighbours(i, j, image)
            C = image[i, j]
            if (C == 1 and 
                2 <= sum(neighbours(i, j, image)) <= 6 and 
                transitions(neighbours(i, j, image)) == 1 and 
                (P2 * P4 * P6 == 0 if iter == 0 else P2 * P4 * P8 == 0) and 
                (P4 * P6 * P8 == 0 if iter == 0 else P2 * P6 * P8 == 0)):
                marker[i, j] = 1
    image[marker == 1] = 0


def thinning(image):
    prev_image = np.zeros(image.shape, np.uint8)
    while not np.array_equal(image, prev_image):
        prev_image = image.copy()
        thinning_iteration(image, 0)
        thinning_iteration(image, 1)
    return image