class videocard:

    def __init__(self, name="RTX 4090", memory=24, pin=16, heat=40):
        self.name = name
        self.memory = memory
        self.pin = pin
        self.heat = heat

    def image(self):
        print("Какое-то изображение")

    def heat(self):
        self.heat += 100
        print()        



        