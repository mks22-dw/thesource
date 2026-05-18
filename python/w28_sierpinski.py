import turtle

window = turtle.Screen()
window.setup(800, 800)

def triangle(t, size):
    t.pd()
    t.lt(60)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(180)

def sierpinski(t, depth, length):
    if depth == 1:
        triangle(t, length)
    else:
        sierpinski(t, depth-1, length/2)
        t.fd(length/2)    
        sierpinski(t, depth-1, length/2)
        t.bk(length/2)
        t.lt(60)
        t.fd(length/2)
        t.rt(60)
        sierpinski(t, depth-1, length/2)
        t.lt(60)
        t.bk(length/2)
        t.rt(60)
        


michaelangelo = turtle.Turtle() # make a new turlte
michaelangelo.pu()
michaelangelo.setpos(-390, -380)
michaelangelo.pd()
sierpinski(michaelangelo, 4, 750)
