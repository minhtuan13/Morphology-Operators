import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

from binary.lib import header_lib as binary_lib
from grayscale.lib import header_lib as gray_lib

from binary.non_lib import header_non_lib as binary_non_lib
from grayscale.non_lib import header_non_lib as gray_non_lib
import os

def grayscale_to_binary(image_path, threshold):
    # Open the grayscale image
    grayscale_img = Image.open(image_path).convert('L')


    # Apply thresholding
    binary_img = grayscale_img.point(lambda pixel: 255 if pixel > threshold else 0)

    return binary_img

class ImageProcessorApp:
    def __init__(self, master):
        
        self.master = master
        self.master.title("Image Processor")

        self.source_image_label = tk.Label(master, text="Source Image:")
        self.source_image_label.grid(row=0, column=0, padx=5, pady=5)

        self.processed_image_label = tk.Label(master, text="Processed Image:")
        self.processed_image_label.grid(row=0, column=1, padx=5, pady=5)

        self.original_image = None
        self.original_image_label = tk.Label(master)
        self.original_image_label.grid(row=1, column=0, padx=5, pady=5)

        self.processed_image = None
        self.processed_image_label = tk.Label(master)
        self.processed_image_label.grid(row=1, column=1, padx=5, pady=5)

        self.import_type_var = tk.StringVar(master, "Grayscale")
        self.import_type_label = tk.Label(master, text="Import Type:")
        self.import_type_label.grid(row=2, column=0, padx=5, pady=5)
        self.import_type_menu = tk.OptionMenu(master, self.import_type_var, "Grayscale", "Binary")
        self.import_type_menu.grid(row=2, column=1, padx=5, pady=5)
        
        self.import_type_var.trace_add('write', self.update_process_options)  # Thiết lập phương thức theo dõi

        self.select_button = tk.Button(master, text="Select Image", command=self.open_image)
        self.select_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.use_library_var = tk.BooleanVar()
        self.use_library_var.set(True)
        self.use_library_checkbutton = tk.Checkbutton(master, text="Use Library Function", variable=self.use_library_var)
        self.use_library_checkbutton.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.structuring_element_var = tk.StringVar(master, value="1\n1\n1")
        self.struct_entry_label = tk.Label(master, text="Enter Structuring Element (0s and 1s, separated by newline):")
        self.struct_entry_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        self.struct_entry = tk.Text(master, height=3, width=10)
        self.struct_entry.insert(tk.END, "1\n1\n1")
        self.struct_entry.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.process_options = ["Dilation", "Erosion", "Opening", "Closing", "Reconstruction"]  
     
        self.process_option_var = tk.StringVar(master)
        self.process_option_var.set(self.process_options[0])  # Default operation
        self.operation_label = tk.Label(master, text="Select Operation:")
        self.operation_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
        self.process_option_menu = tk.OptionMenu(master, self.process_option_var, *self.process_options)
        self.process_option_menu.grid(row=8, column=0, columnspan=2, padx=5, pady=5)  
        default_value = self.import_type_var.get()
        if default_value:
            self.update_process_options()
        self.process_button = tk.Button(master, text="Process Image", command=self.process_image)
        self.process_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

        self.save_button = tk.Button(master, text="Save Processed Image", command=self.save_image)
        self.save_button.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            if self.import_type_var.get() == "Grayscale":
                self.image = Image.open(file_path).convert('L')
            else:
                self.image = grayscale_to_binary(file_path, 127)
            self.display_original_image()
    def update_process_options(self, *args):
        if self.import_type_var.get() == "Grayscale":
            if "Top Hat" not in self.process_options:
                self.process_options.append("Top Hat")
            if "Smoothing" not in self.process_options: 
                self.process_options.append("Smoothing")
            if "Gradient" not in self.process_options: 
                self.process_options.append("Gradient")
            if "Textual segmentation" not in self.process_options: 
                self.process_options.append("Textual segmentation")
            if "Granulometry" not in self.process_options: 
                self.process_options.append("Granulometry")
            

            if "Hit or Miss" in self.process_options:
                self.process_options.remove("Hit or Miss")
            if "Boundary Extraction" in self.process_options: 
                self.process_options.remove("Boundary Extraction")
            if "Region Filling" in self.process_options: 
                self.process_options.remove("Region Filling")
            if "Extraction of Connected Components" in self.process_options: 
                self.process_options.remove("Extraction of Connected Components")
            if "Convex Hull" in self.process_options: 
                self.process_options.remove("Convex Hull")
            if "Thinning" in self.process_options: 
                self.process_options.remove("Thinning")
            if "Thickening" in self.process_options: 
                self.process_options.remove("Thickening")
            if "Skeleton" in self.process_options: 
                self.process_options.remove("Skeleton")  
            if "Pruning" in self.process_options: 
                self.process_options.remove("Pruning")    
        else:
            if "Top Hat" in self.process_options:
                self.process_options.remove("Top Hat")
            if "Smoothing" in self.process_options: 
                self.process_options.remove("Smoothing")
            if "Gradient" in self.process_options: 
                self.process_options.remove("Gradient")
            if "Textual segmentation" in self.process_options: 
                self.process_options.remove("Textual segmentation")
            if "Granulometry" in self.process_options: 
                self.process_options.remove("Granulometry")
           

            if "Hit or Miss" not in self.process_options:
                self.process_options.append("Hit or Miss")
            if "Boundary Extraction" not in self.process_options: 
                self.process_options.append("Boundary Extraction")
            if "Region Filling" not in self.process_options: 
                self.process_options.append("Region Filling")
            if "Extraction of Connected Components" not in self.process_options: 
                self.process_options.append("Extraction of Connected Components")
            if "Convex Hull" not in self.process_options: 
                self.process_options.append("Convex Hull")
            if "Thinning" not in self.process_options: 
                self.process_options.append("Thinning")
            if "Thickening" not in self.process_options: 
                self.process_options.append("Thickening")
            if "Skeleton" not in self.process_options: 
                self.process_options.append("Skeleton")  
            if "Pruning" not in self.process_options: 
                self.process_options.append("Pruning")    
        # Update the process option menu
        self.process_option_menu.destroy()  # Hủy bỏ menu cũ
        self.process_option_menu = tk.OptionMenu(self.master, self.process_option_var, *self.process_options)  # Tạo menu mới với các tùy chọn đã cập nhật
        self.process_option_menu.grid(row=8, column=0, columnspan=2, padx=5, pady=5)  # Sử dụng .grid() để đặt menu trong lưới
    def display_original_image(self):
        if self.image:
            self.image.thumbnail((300, 300))  # Resize the image to fit the window
            img = ImageTk.PhotoImage(self.image)
            self.original_image_label.config(image=img)
            self.original_image_label.image = img

    def display_processed_image(self):

        if self.processed_image is not None and self.processed_image.size[0] > 0:  # Check if processed_image is not None and has at least one element
            self.processed_image.thumbnail((300, 300))  # Resize the image to fit the window
            img = ImageTk.PhotoImage(self.processed_image)
            self.processed_image_label.config(image=img)
            self.processed_image_label.image = img

    def process_image(self):
        if self.image:
            struct_str = self.struct_entry.get("1.0", tk.END)
            struct_array = np.array([[int(val) for val in line.split()] for line in struct_str.splitlines() if line.strip()])
            if struct_array.size == 0:
                messagebox.showerror("Error", "Please enter a valid structuring element.")
                return
            if not np.all(np.logical_or(struct_array == 0, struct_array == 1)):
                messagebox.showerror("Error", "Structuring element should contain only 0s and 1s.")
                return
        src_image = np.array(self.image)
        if self.import_type_var.get() == "Binary": 
            if not self.use_library_var.get():
                # print ("tu viet")
                self.processed_image = binary_non_lib.binary_morphology(src_image, struct_array, self.process_option_var.get())
                print(self.processed_image)
                self.processed_image = Image.fromarray(self.processed_image.astype(np.uint8)* 255)
                
            else: 
                
                self.processed_image = binary_lib.binary_morphology(src_image, struct_array, self.process_option_var.get())
                print(self.processed_image)
            # Convert the processed NumPy array to a PIL Image object
                self.processed_image = Image.fromarray(self.processed_image.astype(np.uint8))
            self.display_processed_image()
        else:
            if not self.use_library_var.get():

                
                self.processed_image = gray_non_lib.grayscale_morphology(src_image, struct_array, self.process_option_var.get())

            else:
                self.processed_image = gray_lib.grayscale_morphology(src_image, struct_array, self.process_option_var.get())
            self.processed_image = Image.fromarray(self.processed_image.astype(np.uint8))
            self.display_processed_image()

    def save_image(self):
        if self.processed_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                self.processed_image.save(file_path)
                messagebox.showinfo("Save", "Image saved successfully!")
            else:
                messagebox.showerror("Error", "Please provide a valid file path.")

def main():
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()