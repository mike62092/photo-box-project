import tkinter as tk
from tkinter import PhotoImage
import time
import datetime as dt
from picamzero import Camera

def capture_photo():
    i = dt.datetime.now()
    now = i.strftime("%Y%m%d-%H%M%S")
    filepath = "name_of_local_directory" + now + ".jpg"
    cam = Camera()
    cam.start_preview()
    cam.take_photo(filepath)
    cam.stop_preview()

# Create the root window
root = tk.Tk()

# Set the resolution for a 5-inch touchscreen (typically 800x480)
screen_width = 800
screen_height = 480
root.geometry(f"{screen_width}x{screen_height}")

# Create a canvas to hold the background image
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack(fill="both", expand=True)

# Load the background image
background_image = PhotoImage(file="Untitled_Artwork 2.png")

# Get the image width and height
image_width = background_image.width()
image_height = background_image.height()

# Calculate the center of the screen
x_center = screen_width // 2
y_center = screen_height // 2

# Place the background image at the center of the canvas
canvas.create_image(x_center, y_center, image=background_image, anchor="center")

# Load image for the button
round_button_image = PhotoImage(file="nellie.png")  # Create a round button image with transparent background

# Create the button
photo_button = tk.Button(root, image=round_button_image, command=capture_photo, bg="white", borderwidth=0)  # borderwidth=0 removes the frame
canvas.create_window(screen_width - 100, screen_height - 50, anchor="center", window=photo_button)

# Add a label for the blue text over the button (placing it on top of the image)
button_text = tk.Label(root, text="TAKE PICTURE", font=("Futura", 14, "bold"), fg="blue", bg="white")
canvas.create_window(screen_width - 100, screen_height - 50, anchor="center", window=button_text)

root.mainloop()
