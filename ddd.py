import turtle as t
import math

t.shape("turtle")
t.color("blue")

walls_width = 200
walls_high = 100
door_width = 30
door_height = 30
roof_height = 0
roof_side = math.sqrt(roof_height ** 2 + (walls_width / 2) ** 2)
roof_angle = math.degrees(math.atan(roof_height / (walls_width / 2)))
print(roof_angle)


# стены дома
for i in range(2):
    t.forward(walls_width)
    t.left(90)
    t.fd(walls_high)
    t.left(90)


# дверь
t.fd(walls_width / 2 - door_width / 2)
for i in range(2):
    t.fd(door_width)
    t.left(90)
    t.fd(door_height)
    t.left(90)

t.left(180)
t.fd(walls_width / 2 - door_width / 2)
t.right(90)
t.fd(walls_high)
t.right(90)
t.left(roof_angle)
t.fd(roof_side)
t.right(roof_angle * 2)
t.fd(roof_side)


t.done()

