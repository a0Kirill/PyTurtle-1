import turtle

screen = turtle.Screen()
screen.setup(width=600, height=400)
t = turtle.Turtle()
angle = 65
step = 10

t.forward(step)
t.left(angle)
t.forward(step)
t.right(angle)
t.right(angle)
t.forward(step)
t.left(angle)
t.forward(step)

canvas = screen.getcanvas()
screen.exitonclick()