import turtle as t

t.speed(0)
t.colormode(255)

side = 2

while True:
    t.fd(side)
    t.left(90)
    side = side ** 2

t.done