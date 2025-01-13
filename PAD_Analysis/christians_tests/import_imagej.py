import imagej
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Initialize the ImageJ gateway
imagej_executable = "Z:\Software\Fiji.app\ImageJ-win64.exe"
ij = imagej.init(imagej_executable)


# Open a dialog to select an image file
root = tk.Tk()
root.withdraw()
image_path = filedialog.askopenfilename(title="Select an Image File")

# Check if the user canceled the file dialog
if not image_path:
    print("No image selected. Exiting.")
    exit()

# Read the image from the selected path
image = ij.io().open(image_path)

# Show the image in ImageJ
ij.ui().show("Selected Image", image)

# Create an ROI
roi_width = 100
roi_height = 100
roi_x = (image.getWidth() - roi_width) // 2  # Center the ROI horizontally
roi_y = (image.getHeight() - roi_height) // 2  # Center the ROI vertically
roi = ij.op().run("create.roi.rectangle", roi_x, roi_y, roi_width, roi_height)

# Add the ROI to the image
ij.rois().addRoi(roi)

# Make sure ImageJ is still running and does not exit immediately
ij.ui().show("ImageJ is running", image)

# You can use this line to pause execution until you close ImageJ
input("Press Enter to exit ImageJ...")

# Close ImageJ when done
ij.ui().quit()
