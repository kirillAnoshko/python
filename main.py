class Hero:
    def __init__(self, name, hp, money, attack, lvl, xp, inventory):
        self.name = name
        self.hp = hp
        self.money = money
        self.attack = attack
        self.lvl = lvl
        self.xp = xp
        self.inventory = []

    def attacking(self):
        self.hp -= self.attack
        print("Персонаж нанес урон другому персонажу!")    

class Sword:
    def __init__(self, damage, Strength):        