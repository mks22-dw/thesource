import turtle
window = turtle.Screen()
window.setup(600, 600)

def triangle(t, size):
    t.lt(60)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(180)

def draw_sierpinski(t, depth, length):
    if (depth == 1):
        triangle(t, length)
    else:
        draw_sierpinski(t, depth-1, length/2)
        t.fd(length/2)
        draw_sierpinski(t, depth-1, length/2)
        t.bk(length/2)
        t.lt(60)
        t.fd(length/2)
        t.rt(60)
        draw_sierpinski(t, depth-1, length/2)
        t.lt(60)
        t.bk(length/2)
        t.rt(60)

raphael = turtle.Turtle()
raphael.pu()
raphael.ht()
raphael.speed(0)
raphael.goto(-250, -250)
raphael.pd()

draw_sierpinski(raphael, 8, 500)

window.exitonclick()
