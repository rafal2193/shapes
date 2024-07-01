#Rafal Krauze
#June 8,2024
#CMP 131
#Lab 3 consits of creating simple illustratiomns using Python Turtle Graphics. I will be creating the following shapes: circle, square, trianglem and rectangle. Each sahpe will not overlap, s input dialog box will be created to allow you to choose the shapes colors and the radius of the circle. 
#I hereby attest that this code is original and written by me alone. I understand that I risk a penalty for violating the Academic Integrity policy at CCM

#Opening python and activating turtle mode. 
import turtle
turtle.showturtle()
#Changing the sahpe of the arrow to a turtle
turtle.shape("turtle")
#Lifting pen up
turtle.penup
turtle.penup()
#Turtle moved to starting position
turtle.goto(10,200)
#Entering my name
#Moved my name a little to the left, due to the reason of the letter count to make it more centered
turtle.write("Rafal Krauze")


#Code to create a color input dialong
def get_color(shape_name):
    return turtle.textinput(f"{shape_name} Color", f"Enter the color for the {shape_name}:")

#Creating a circle
#Equation for create input dialong for the radius circle
radius = turtle.numinput("Circle Radius", "Enter the radius of the circle:")
#Equation to choose color for circle
circle_color = get_color("Circle")

#Penup to move to the starting position
turtle.penup()
#Staring position
turtle.goto(-200, -200)
#Pendown to start drawing
turtle.pendown()
#Choose color of the cirlce 
turtle.fillcolor(circle_color)
#Begin filling the circle
turtle.begin_fill()
# Draw a circle
turtle.circle(radius)
# End filling
turtle.end_fill()
# Penup to end drawing
turtle.penup()

#Creating a square
#Equation to choose color of square
square_color = get_color("Square")
#Move to starting position
turtle.goto(200,200)
#Pendown to start drawing
turtle.pendown()
#Fill sqaure with color
turtle.fillcolor(square_color)
#Begin coloring square
turtle.begin_fill()
#Move turtle forward
turtle.forward(50)
#Move turtle right
turtle.right(90)
#Move turtle forward
turtle.forward(50)
#Move turtle right
turtle.right(90)
#Move turtle forward
turtle.forward(50)
#Move turtle right
turtle.right(90)
#move turtle forward
turtle.forward(50)
#End filling
#Sqaure is created 
turtle.end_fill()

#Creating a rectangle
#Equation to choose color of rectangle 
rectangle_color = get_color("Rectangle")
#Penup
turtle.penup()
#Move to starting position
turtle.goto (200,-200)
#Pendown to start drawing
turtle.pendown()
#Choose color of rectangle
turtle.fillcolor(rectangle_color)
#Begin coloring rectangle
turtle.begin_fill()
#Move turtle forward
turtle.forward(100)
#Move turtle right
turtle.right(90)
#Move turtle forward
turtle.forward(50)
#Move turtle right
turtle.right(90)
#Move turtle forward
turtle.forward(100)
#Move turtle right
turtle.right(90)
#Move turtle forward
turtle.forward(50)
#End filling
#Rectangle is created
turtle.end_fill()

#Creating a triangle
#Equationto choose color of triangle
triangle_color = get_color("Triangle")
#Penup
turtle.penup()
#Move to starting position
turtle.goto(-200,200)
#Pendown to start drawing
turtle.pendown()
#Choose color of triangle
turtle.fillcolor(triangle_color)
#Begin coloring triangle
turtle.begin_fill()
#Move turtle forward
turtle.forward(66)
#Move turtle left
turtle.left(110)
#Move turtle forward
turtle.forward(75)
#Move turtle left
turtle.left(130)
#Move forward
turtle.forward(82)
#End filling
#Triangle is created
turtle.end_fill()
#Penup
turtle.penup()
#Move turtle to end position  
turtle.goto(0,0)
#Return turtle to orginal color
turtle.fillcolor("black")
