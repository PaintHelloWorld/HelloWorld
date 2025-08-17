import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

rainbow = turtle.Turtle()
rainbow.width(20)
rainbow.speed(11)
colors = ["red","orange","yellow","limegreen","dodgerblue","blue","purple"]

start_x=220
radius=250

for color in colors:
    rainbow.pencolor(color)
    rainbow.penup()
    rainbow.goto(start_x,-50)
    rainbow.pendown()
    rainbow.setheading(270)
    rainbow.right(180)
    rainbow.circle(radius, 180)
    start_x-=20
    radius-=20
    
rainbow.hideturtle()
screen.exitonclick()
