import turtle as t
import random

t.speed(0)




t.colormode(255)

while True:
    x = random.randint(-300, 300)
    y = random.randint(-100, 100)
    sides = random.randint(3, 10)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    t.penup()
    t.goto(x, y)

    t.fillcolor(red, green, blue)
    t.pendown()
    t.begin_fill()
    for i in range(sides):
        t.fd(360 / sides * 2)
        t.left(360 / sides)
    t.end_fill()



t.done()