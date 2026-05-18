import turtle

window = turtle.Screen()
window.setup(600, 300) #set window size to 600x600 pixels

def draw_koch(t, depth, length):
    if depth == 1:
        t.fd(length)
    else:
        draw_koch(t, depth-1, length)
        t.lt(60)
        draw_koch(t, depth-1, length)
        t.rt(120)
        draw_koch(t, depth-1, length)
        t.lt(60)
        draw_koch(t, depth-1, length)

raphael = turtle.Turtle() # make a new turlte
raphael.pu()
raphael.setpos(-295, -120)
raphael.pd()
draw_koch(raphael, 3, 50)