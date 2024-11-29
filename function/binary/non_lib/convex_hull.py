import numpy as np 
import cv2
from PIL import Image, ImageDraw
def complete_convex_hull(image):
    # Lấy tọa độ của các điểm trên đường biên của hình ảnh
    y, x = np.where(image > 0)
    points = np.column_stack((x, y))
    
    # Tính Convex Hull của các điểm
    hull = []
    #duyệt qua các điểm trên đường biên của hình ảnh
    for i in range(len(points)):
        #kiểm tra các điểm trên Convex Hull hiện tại
        while len(hull) >= 2 and np.cross(hull[-1] - hull[-2], points[i] - hull[-2]) <= 0:
            hull.pop()  #xóa điểm cuối cùng của Convex Hull nếu điểm này không nằm trên đường convex
        hull.append(points[i])
        
    #chọn vì điểm cuối cùng đã được thêm vào Convex Hull ở vòng lặp trước
    for i in range(len(points)-2, -1, -1):
        while len(hull) >= 2 and np.cross(hull[-1] - hull[-2], points[i] - hull[-2]) <= 0:
            hull.pop()
        hull.append(points[i])
        
    return np.array(hull)
def convex_hull(image):
    
    ## vẽ các hull lên ảnh gốc
    hulls = complete_convex_hull(image)
    # Nếu image là một numpy array, chuyển nó thành đối tượng PIL Image
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)

    # # Chuyển đổi ảnh sang chế độ grayscale
    # image = image.convert('L')
    # image_np = np.array(image)

    if len(hulls) == 0:
        print("No hull found.")
        return
    image_rgb = image.convert('RGB')
    draw = ImageDraw.Draw(image_rgb)
    # Draw the convex hull on the image
    hull_points = [(int(point[0]), int(point[1])) for point in hulls]
    draw.polygon(hull_points, outline='red')
    # Convert the image back to numpy array
    result_image_np = np.array(image_rgb)

    return result_image_np*255