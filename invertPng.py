import cv2
import numpy as np
import argparse

# Function to invert the grayscale image
def invert_image(input_path, output_path):
    # Read the image in grayscale
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Could not load image: {input_path}")
        return
    
    # Invert the grayscale image
    inverted_image = cv2.bitwise_not(image)
    
    # Save the inverted image
    cv2.imwrite(output_path, inverted_image)
    print(f"Inverted image saved at {output_path}")

# Main function to parse arguments and call the invert function
def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description="Invert a grayscale PNG image.")
    parser.add_argument("input", help="Path to the input grayscale PNG image")
    parser.add_argument("output", help="Path to save the inverted grayscale PNG image")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call the function to invert the image
    invert_image(args.input, args.output)

# Run the main function
if __name__ == "__main__":
    main()
