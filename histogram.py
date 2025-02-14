import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to display histogram
def display_histogram(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Error: Unable to read the image.")
        return
    
    # Calculate the histogram
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Plot the histogram
    plt.figure(figsize=(10, 6))
    plt.plot(histogram, color='black')
    plt.title('Grayscale Histogram')
    plt.xlabel('Pixel Intensity Value')
    plt.ylabel('Frequency')
    plt.xlim([0, 255])  # Ensure the x-axis covers all bins
    plt.grid(alpha=0.5)
    plt.show()

# Input: Provide the path to the image file
image_path = input("Enter the path to the image file: ").strip()
display_histogram(image_path)
