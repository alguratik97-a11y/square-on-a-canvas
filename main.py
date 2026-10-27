# Program to draw a square on a turtle canvas

import turtle

# Set up the screen/canvas
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Draw a Square")

# Create a turtle pen object
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("blue")
pen.pensize(3)
pen.speed(2)

# Loop to draw the 4 sides of the square
for i in range(4):
    pen.forward(100)  # Move forward by 100 pixels
    pen.right(90)     # Turn right by 90 degrees

# Keep the window open until clicked
turtle.done()
