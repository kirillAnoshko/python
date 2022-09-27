import os

name = input("как зовут персонажа? ")
if name == "": name = "илья муромец"

way_1 = True
way_2 = True
way_3 = True
game = True
key = ""

while game:


    if way_1 or way_2 or way_3:
        key = ""
        os.system("cls")
        print(f"{name} у камня")
        if way_1:
            print("1 вариант")
        if way_2:
            print("2 вариант")
        if way_3:
            print("3 вариант")

        user_choice = input("какой вариант")
        key += user_choice

    if key == "1" and way_1:
        os.system("cls")
        print("дорога 1")
        print("1 вариант")
        print("2 вариант")
        user_choice = input("какой вариант? ")
        key += user_choice

        if key == "11":
            os.system("cls")
            print("дорога 1-хороший выбор")
            way_1 = False
        if key == "12":
            os.system("cls")
            print("дорога 1-плохой выбор")
            game = False



print("game end")