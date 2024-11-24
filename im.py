import turtle
from PIL import Image

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("white")

# Load the photo
photo = Image.open("thakur.jpg")

# Get the width and height of the photo
width, height = photo.size

# Create a new turtle to draw the sketch
sketch = turtle.Turtle()
sketch.speed(1)
sketch.pencolor("black")

# Convert the photo to grayscale
photo = photo.convert("L")

# Iterate over each pixel in the photo
for x in range(width):
    for y in range(height):
        # Get the pixel value
        value = photo.getpixel((x, y))

        # Move the turtle to the pixel's location
        sketch.penup()
        sketch.goto(x - width // 2, height // 2 - y)
        sketch.pendown()

        # Draw a dot with size proportional to the pixel value
        sketch.dot(value / 255 * 10)

# Keep the window open until it is closed by the user
turtle.done()
