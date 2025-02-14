import os
import pydicom
import numpy as np
from PIL import Image
import cv2
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to load DICOM images from a folder and convert them to PNG
def convert_dcm_folder_to_png():
    # Ask for the input folder containing DICOM files
    src_folder = filedialog.askdirectory(title="Select Folder with DICOM Files")
    
    if src_folder:
        # Ask for the output folder to save PNG files
        dst_folder = filedialog.askdirectory(title="Select Folder to Save PNG Files")
        
        if dst_folder:
            try:
                # Loop through each DICOM file in the source folder
                for filename in os.listdir(src_folder):
                    if filename.endswith(".dcm"):
                        dicom_path = os.path.join(src_folder, filename)
                        
                        # Read the DICOM file
                        dicom_data = pydicom.dcmread(dicom_path)
                        img = dicom_data.pixel_array 

                        # Normalize image to 8-bit (if needed)
                        if img.dtype != np.uint8:
                            img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
                            img = np.uint8(img)
                        
                        # Convert the numpy array to a PIL image
                        img_pil = Image.fromarray(img)

                        # Construct the output PNG file path
                        output_file = os.path.join(dst_folder, f"{os.path.splitext(filename)[0]}.png")
                        
                        # Save the image as PNG
                        img_pil.save(output_file)
                        print(f"Converted {filename} to PNG and saved to {output_file}")
                
                messagebox.showinfo("Success", "All DICOM files converted to PNG successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("No Folder", "No output folder selected.")
    else:
        messagebox.showwarning("No Folder", "No input folder selected.")

# Create the main window
root = tk.Tk()
root.title("DICOM to PNG Converter")

# Add a button to trigger the DICOM folder to PNG conversion
btn_convert = tk.Button(root, text="Convert DICOM Folder to PNG", command=convert_dcm_folder_to_png)
btn_convert.pack(pady=20)

# Run the application
root.mainloop()
