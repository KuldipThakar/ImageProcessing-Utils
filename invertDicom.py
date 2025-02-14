#Author kuldip thakar 
#date 18-12-2024 3



import os
import argparse
import pydicom
import numpy as np

def invert_and_normalize_pixel_array(pixel_array):
    """Invert the pixel array and normalize the values."""
    inverted_pixel_array = np.max(pixel_array) - pixel_array
    return inverted_pixel_array

def invert_dicom_images(src_folder, dst_folder):
    try:
        print(f"Source Folder: {src_folder}")
        print(f"Destination Folder: {dst_folder}")

        # Ensure destination directory exists
        os.makedirs(dst_folder, exist_ok=True)

        # Get all DICOM files in the source folder
        dicom_files = [f for f in os.listdir(src_folder) if f.lower().endswith(".dcm")]

        if not dicom_files:
            print("No DICOM files found in the source folder.")
            return

        print(f"Found {len(dicom_files)} DICOM files to process.")

        for dicom_file in dicom_files:
            src_path = os.path.join(src_folder, dicom_file)
            dst_path = os.path.join(dst_folder, dicom_file)

            try:
                # Read the DICOM file
                dicom = pydicom.dcmread(src_path)

                # Check for Pixel Data
                if 'PixelData' not in dicom:
                    print(f"Skipping file (no Pixel Data): {src_path}")
                    continue

                # Get the pixel array
                pixel_array = dicom.pixel_array

                # Invert and normalize the pixel array
                inverted_pixel_array = invert_and_normalize_pixel_array(pixel_array)

                # Replace the PixelData with the inverted array
                dicom.PixelData = inverted_pixel_array.tobytes()

                # Update metadata if necessary
                if hasattr(dicom, "WindowCenter") and hasattr(dicom, "WindowWidth"):
                    dicom.WindowCenter = [np.mean(inverted_pixel_array)]
                    dicom.WindowWidth = [np.max(inverted_pixel_array) - np.min(inverted_pixel_array)]

                # Save the inverted DICOM file
                dicom.save_as(dst_path)
                print(f"Inverted DICOM saved: {dst_path}")

            except Exception as e:
                print(f"Error processing file {src_path}: {e}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Invert multiple DICOM images in a folder.")
    parser.add_argument("--src", required=True, help=" Enter the Source folder containing DICOM files")
    parser.add_argument("--dst", required=True, help=" Enter Destination folder for inverted DICOM files")
    args = parser.parse_args()

    invert_dicom_images(args.src, args.dst)
