import turtle as t
import math

t.shape("turtle")
t.speed(12)

walls_width = int(input("ширина стен "))
walls_high = int(input("высота стен "))
walls_color = input("цвет стен (hex) ")
door_width = int(input("ширина двери "))
door_height = int(input("высота двери "))
door_color = input("цвет двери (hex) ")
roof_color = input("цвет крыши (hex) ")
roof_height = int(input("высота крыши" ))
roof_side = math.sqrt(roof_height ** 2 + (walls_width / 2) ** 2)
roof_angle = math.degrees(math.atan(roof_height / (walls_width / 2)))
print(roof_angle)

# отодвинуть черепаху

x = (walls_width / 2) * -1
y = (walls_high + roof_height) / 2 * -1
t.setpos(x, y)
# стены дома
t.fillcolor(walls_color)
t.begin_fill()
for i in range(2):
    t.forward(walls_width)
    t.left(90)
    t.fd(walls_high)
    t.left(90)
t.end_fill()


# дверь
t.fd(walls_width / 2 - door_width / 2)
t.fillcolor(door_color)
t.begin_fill()
for i in range(2):
    t.fd(door_width)
    t.left(90)
    t.fd(door_height)
    t.left(90)
t.end_fill()
# крыша
t.left(180)
t.fd(walls_width / 2 - door_width / 2)
t.right(90)
t.fd(walls_high)
t.fillcolor(roof_color)
t.begin_fill()
t.right(90)
t.left(roof_angle)
t.fd(roof_side)
t.right(roof_angle * 2)
t.fd(roof_side)
t.end_fill()


t.done()

