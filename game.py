import random

player = random.randint(1, 6)
cpu = random.randint(1, 6)

print("игрок кинул", player)
print("комп кинул", cpu)

if player > cpu:
	print("игрок победил!")
elif cpu > player:
	print("комп победил!")
else:
	print("ничья!")