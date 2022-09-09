user_money = float(input())  # пользователь вводит сумму в рублях
dinar = 196.80  # сохранить в памяти курсы трех валют
rial = 0.0014  # сохранить в памяти курсы трех валют
belrub = 24.02  # сохранить в памяти курсы трех валют4

print(round(user_money / dinar, 2), "кувейтских динаров")
print(round(user_money / rial, 2), "иранских риалов")
print(round(user_money / belrub, 2), "белорусских рублей")