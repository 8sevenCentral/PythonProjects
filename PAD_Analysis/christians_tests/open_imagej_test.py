import subprocess
import tkinter as tk
from tkinter import filedialog
import psutil
import imagej
import numpy as np

imagej_executable = r"Z:\Software\Fiji.app\ImageJ-win64.exe"    # image executable for ImageJ on Zdrive

imagej_running = False  # Check if ImageJ is open
for process in psutil.process_iter(attrs=['pid', 'name']):
    if "ImageJ-win64.exe" in process.info['name']:
        imagej_running = True
        break

if not imagej_running:  # If ImageJ is not open, open it
    try:
        subprocess.Popen([imagej_executable])
        print("ImageJ opened successfully.")    # print that ImageJ opened or not
    except FileNotFoundError:
        print("ImageJ executable not found. Please specify the correct path.")
    except Exception as e:
        print(f"An error occurred: {e}")

root = tk.Tk()   # Create a window to select an image to analyze 
root.withdraw()  # Hide the main window

# Prompt the user to select an image file
image_path = filedialog.askopenfilename(title="Select image")

# Check if an image file was selected
if image_path:
    print(f"Selected image: {image_path}")
else:
    print("No image selected.")

# Start an instance of ImageJ
ij = imagej.init('net.imagej:imagej')

# Create a blank 100x100 pixel ROI
width = 100
height = 100
roi_image = np.zeros((height, width), dtype=np.uint8)

# Convert the numpy array to an ImageJ dataset
roi_dataset = ij.py.to_dataset(roi_image)

# Show the ROI
ij.ui().show(roi_dataset)

# Optionally save the ROI as an ImageJ dataset
# ij.io().save(roi_dataset, 'path_to_save/roi_image.tif')

# Stop the ImageJ instance
ij.context().dispose()