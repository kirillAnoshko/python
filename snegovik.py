import turtle as t


start_radius = 50
for i in range(3):
    t.circle(start_radius)
    t.penup()

    start_radius = start_radius / 2
    if start_radius < 5:
        break

    input("+++++++++++++")

t.done()