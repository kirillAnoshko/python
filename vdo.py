class player:

    def __init__(self, name="Безымянный"):
        self.name = name
        self.hp = 100

    def ride(self):
        print("ирвмчошсщшвмгпрывлочслдзщкшвщзашгсчлолщвзчдлмвлмлыдмлвыща")

    def heal(self):
        self.hp += 15
        print("Вылечил 15 жизней")        


p1 = player()
p2 = player("Ася")
p3 = player("Квася")

print(p1.name)
print(p2.name)
print(p3.name)

