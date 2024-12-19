import turtle

lenstep = 20
storoni = 60
offset = 0

def m(len, storon):
    n=0
    t.begin_fill()
    t.fillcolor(0,0,255)
    while n<storon :
        t.forward(len)
        t.left(360/storon)
        n = n + 1
        print(n,":",storon)
    t.end_fill()



screen = turtle.Screen()
screen.setup(width=2000, height=2000, startx=offset, starty=offset)
t = turtle.Turtle()
screen.colormode(255)
t.pencolor(0,0,225)

for i in range (storoni):
    m(lenstep,i)

#canvas = screen.getcanvas()
screen.exitonclick() 