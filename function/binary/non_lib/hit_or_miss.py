from scipy.ndimage import binary_erosion
import numpy as np
def hit_or_miss (image, structuring_element):
    # Tạo các bản sao của kernel
    b1 = structuring_element.copy()
    

  # Make a copy of the kernel
    b2 = structuring_element.copy()

    # Swap 1s and 0s in the copy
    b2 = 1 - b2
    print (b2)

    # Thực hiện phép xói mòn với kernel b1, b2 trên ảnh đầu vào
    a =  binary_erosion(image,b1)
    b =  binary_erosion(~image, b2)
    
    # Lấy phép giao giữa 2 ảnh đã xói mòn
    hitmiss_img = a&b
    return hitmiss_img