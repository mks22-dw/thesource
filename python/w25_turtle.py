import turtle

window = turtle.Screen()
window.setup(500, 500) #set window size to 500x500 pixels
window.colormode(255)

def draw_square(t, size):
    t.pd()
    i = 0
    while i < 4:
        t.fd(size)
        t.rt(90)
        i+= 1

def draw_spiral0(t, size):
    t.pd()
    while size >= 0:
        t.fd(size)
        t.rt(90)
        size-= 5

def draw_spiral1(t, size, angle):
    t.pd()
    while size >= 0:
        t.fd(size)
        t.rt(angle)
        size-= 5



raphael = turtle.Turtle() # make a new turlte
raphael.speed(1)
raphael.pu()
raphael.setpos(-245, 245)
draw_square(raphael, 200)


raphael.pu()
raphael.setpos(5, 245)
draw_spiral0(raphael, 200)

raphael.pu()
raphael.setpos(-245, 5)
raphael.setheading(0)
draw_spiral1(raphael, 200, 45)