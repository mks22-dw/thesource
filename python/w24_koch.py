import turtle
window = turtle.Screen()
window.setup(600, 600)

def draw_square_spiral(t, length):
    if (length > 0):
        t.fd(length)
        t.rt(90)
        draw_square_spiral(t, length-5)

# - At depth 2, the curve is:
#   - A straight line,
#   - followed by a rotation of 60 degrees to the left,
#   - followed by another straight line (aka koch curve)
#   - followed by a rotation of 120 degrees to the right
#   - followed by another straight line (aka koch curve)
#   - followed by a rotation of 60 degrees to the left
#   - followed by one more straight line. (aka koch curve)
def koch_curve(t, length, depth):
    if (depth == 1):
        t.fd(length)
    else:
        koch_curve(t, length, depth-1)
        t.lt(60)
        koch_curve(t, length, depth-1)
        t.rt(120)
        koch_curve(t, length, depth-1)
        t.lt(60)
        koch_curve(t, length, depth-1)

raphael = turtle.Turtle()
raphael.pu()
raphael.goto(-250, 0)
raphael.pd()


koch_curve(raphael, 50, 3)

window.exitonclick()
