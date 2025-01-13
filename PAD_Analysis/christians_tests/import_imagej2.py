from imagej import ImageJ
import numpy as np

# Initialize ImageJ
ij = ImageJ("Z:\Software\Fiji.app\ImageJ-win64.exe")

# Open an image
image_plus = ij.io().open(r"C:\Users\cterjesen\Documents\set-cornell_testing_day3\run-10img_100-200_1pulseCap1_pinhole\frames\10img_100-200_1pulseCap1_pinhole_00000001.raw")

# Convert the ImagePlus object to a numpy array
image_array = np.array(image_plus)

# Define the coordinates of the ROI
x = 50
y = 50
width = 100
height = 100

# Create the ROI
roi = image_array[y:y+height, x:x+width]

# Calculate the mean of the ROI
mean = np.mean(roi)

# Print the results
print("Mean of the ROI:", mean)