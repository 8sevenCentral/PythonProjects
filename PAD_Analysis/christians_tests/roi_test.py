import roifile
import numpy as np
from pymagej.roi import ROIEncoder, ROIRect
import roi_obj


# Image path
image_path = r"C:\Users\cterjesen\Documents\set-cornell_testing_day3\run-10img_100-200_1pulseCap1_pinhole2\frames\10img_100-200_1pulseCap1_pinhole2_00000001.raw"

# Create a sample rectangular ROI
roi_obj = roifile.ImagejRoi.frompoints()
roi_obj = [
    (10, 10),  # Vertex 1
    (110, 10),  # Vertex 2
    (110, 110),  # Vertex 3
    (10, 110)  # Vertex 4
]

# Save the ROI to a file
roi_file_path = "sample_roi.roi"
roi_obj.save(roi_file_path)

print(f"ROI saved to {roi_file_path}")

# Read the ROI file and print the information
read_roi_obj = roifile.ImagejRoi(roi_file_path)
print(f"Type: {read_roi_obj['type']}")
print(f"Top: {read_roi_obj['top']}")
print(f"Left: {read_roi_obj['left']}")
print(f"Bottom: {read_roi_obj['bottom']}")
print(f"Right: {read_roi_obj['right']}")

# Optionally, you can load the image data (assuming it's a raw file)
with open(image_path, "rb") as image_file:
    image_data = image_file.read()
    # Process image_data as needed
