import os
import cv2
import argparse

def rename_images_in_folder(input_folder):
    # Ensure the folder exists
    if not os.path.isdir(input_folder):
        print(f"Error: The folder '{input_folder}' does not exist.")
        return

    # Get a list of all files in the folder
    files = os.listdir(input_folder)

    # Filter only valid image files using OpenCV
    image_files = []
    for file in files:
        file_path = os.path.join(input_folder, file)
        if os.path.isfile(file_path):
            # Attempt to read the file as an image
            image = cv2.imread(file_path)
            if image is not None:
                image_files.append(file)

    # Sort the files to maintain a consistent order
    image_files.sort()

    if not image_files:
        print(f"No valid image files found in the folder '{input_folder}'.")
        return

    # Rename files starting from 1
    for idx, file_name in enumerate(image_files, start=1):
        # Get the file extension
        file_extension = os.path.splitext(file_name)[1]

        # Construct the new file name
        new_name = f"{idx}{file_extension}"

        # Full paths for renaming
        old_path = os.path.join(input_folder, file_name)
        new_path = os.path.join(input_folder, new_name)

        # Check if the new file name already exists
        if os.path.exists(new_path):
            print(f"File {new_name} already exists, skipping renaming of {file_name}.")
            continue

        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: '{file_name}' -> '{new_name}'")

    print(f"Renamed {len(image_files)} files successfully.")

if __name__ == "__main__":
    # Use argparse to parse input folder
    parser = argparse.ArgumentParser(description="Rename image files in a folder sequentially.")
    parser.add_argument("input_folder", type=str, help="Path to the folder containing images")
    args = parser.parse_args()

    # Call the function with the input folder
    rename_images_in_folder(args.input_folder)
