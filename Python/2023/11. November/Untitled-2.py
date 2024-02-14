import turtle
import math

def pen_pos(x, y):

    t.penup()
    t.goto(x, y)
    t.pendown()


def rect(rect_size):
    t.fillcolor("dark green")
    t.begin_fill()
    for i in range(2):
        t.forward(rect_size / 0.6)
        t.right(90)
        t.forward(rect_size)
        t.right(90)
    t.end_fill()


def draw_circle(turtle, size, steps):
    t.fillcolor("red")
    t.begin_fill()
    formula = 2 * math.pi * size  # 2 pi r
    step_length = formula / steps
    step_angle = 360 / steps
    for i in range(steps):
        turtle.forward(step_length)
        turtle.left(step_angle)
    t.end_fill()


t = turtle.Turtle()
t.color('dark green')
t.pensize(10)
t.shape("classic")

pen_pos(-125, 121)
rect(150)

pen_pos(0, -10)
draw_circle(t, 60, 100)

turtle.done()
