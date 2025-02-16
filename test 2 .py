#q= int(input())


import turtle


i=0
i2=0

screen = turtle.Screen()
screen.setup(width=2000, height=2000,startx=990,starty=0)
t = turtle.Turtle()
#angle = 65
#angle2=100
lenstep = 10
#screen.speed(0)
t.pensize(5)
t.shape("turtle")

t.lt(90)
t.fd(300)

gs=[]
p=[]
r=t.heading()
p.append(t.xcor())
p.append(t.ycor())

t.lt(45)
t.fd(100)
t.lt(-21)
t.fd(100)
t.lt(-21)
t.fd(100)



print (r)
t.up()

t.seth(r)
t.goto(p)
t.down()

t.rt(45)
t.fd(100)
t.rt(-21)
t.fd(100)
t.rt(-21)
t.fd(100)

gs.append(p)

canvas = screen.getcanvas()
screen.exitonclick()
