from pymagej.roi import ROIEncoder, ROIRect
import os
import imagej
import numpy as np 

# Start ImageJ
imagej_executable = r"Z:\Software\Fiji.app\ImageJ-win64.exe"
ij = imagej.init(imagej_executable)

# Open an image
image_path = r"C:\Users\cterjesen\Documents\set-cornell_testing_day3\run-10img_100-200_1pulseCap1_pinhole\frames\10img_100-200_1pulseCap1_pinhole_00000001.raw"
image = ij.io().open(image_path)

# Define the base file name
base_filename = "roi_test"

# Define the ROI File Number to be saved
roi_filenumber = 1

# Define fixed ROI dimensions in pixels (width and height)
width = 100
height = 100

# Define ROI coordinates (top, left, bottom, right)
top = 10
left = 10
bottom = 110
right = 110

# Make ROIRect object with the new coordinates
roi_obj = ROIRect(top, left, bottom + width, right + height)
roi_filename = f"{base_filename}_{roi_filenumber}.roi"
roi_directory = 'christians_tests'

# Create the full path to the ROI file
roi_path = os.path.join(roi_directory, roi_filename)

# Save the ROI in the specified directory
with ROIEncoder(roi_path, roi_obj) as roi:
    roi.write()

# Print the file name
print(roi_filename + " saved")