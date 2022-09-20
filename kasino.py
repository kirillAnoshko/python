import random

user_money = 2
casino_money = 2


while user_money and casino_money:
    print("У игрока", user_money, "монет")
    print("У казино", casino_money, "монет")

    input("нажмите Enter чтобы сделать ход")

    user_turn = random.randint(1, 6)
    casino_turn = random.randint(1, 6)
    print("игрок выбросил", user_turn)
    print("казино выбросило", casino_turn)
    if user_turn > casino_turn:
        print("игрок победил")
        user_money += 1
        casino_money -= 1
    elif casino_turn > user_turn:
        print("казино победило")
        casino_money += 1
        user_money -= 1
    else:
        print("ничья")

if user_money:
    print("Игрок забрал все деньги")
else:
    print("Казино забрало все деньги")  
# TODO ставки до броска кубика
# ставки > 0
# ставка <= деньгам