import turtle
window = turtle.Screen()
window.setup(600, 600)

def draw_square(t, length):
    i = 0
    while (i < 4):
        t.fd(length)
        t.rt(90)
        i+= 1

def draw_square_spiral(t, length):
    while (length > 0):
        t.fd(length)
        t.rt(90)
        length-= 5

def draw_spiral(t, length, angle):
    while (length > 0):
        t.fd(length)
        t.rt(angle)
        length-= 5


raphael = turtle.Turtle()
raphael.pu()
raphael.goto(-250, 250)
raphael.pd()

#draw_square(raphael, 200)
draw_square_spiral(raphael, 200)
#draw_spiral(raphael, 100, 30)

window.exitonclick()
