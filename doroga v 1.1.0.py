import random

print("По какой дороге поехать? ")
print("1-убитым быть")
print("2-женатым быть")
print("3-богатым быть")
user = int(input("Введите номер дороги" ))

if user == 1:
    print("Я встретил разбойников")
    print("1-отдать коня")
    print("2-драться")
    print("3-сыграть в кости")
    user = int(input("Что ты выберешь?" ))
    if user == 1:
        print("Я решил отдать своего коня")
        print("но разбойники поступили как крысы и убили меня")
        print("Вы вышли на плохую концовку,вашего коня забрали и убили вас")
    if user == 2:
        print("я долго дрался,но смог отбиться,и забрал коня!")
        print("Поздравляю! Вы вышли на хорошую концовку! Вы перебили всех разбойников,и забрали коня!")
    if user == 3:
        print("разбойники предложили сыграть в игру")
        print("я согласился на игру")  
        илья = random.randint(1, 6)        
        разбойник = random.randint(1, 6)
        print("илья кинул", илья)
        print("разбойник кинул", разбойник)
        if илья > разбойник:
            print("илья победил!")
        elif разбойник > илья:
            print("разбойник победил!")
        else:
            print("ничья!")

elif user == 2:
    print("я приехал к богатому золотому дому")
    print("но я увидел странное свечение в лесу")
    print("может поехать?")
    print("или нет...")
    print("1-не ехать")
    print("2-поехать")
    user = int(input("Что ты выберешь?" ))
    if user == 1:    
        print("я решил не ехать в лес,вдруг там опасно!")
        print("и поэтому я вошёл в дом")
        print("меня встретили и провели в комнату")
        print("мне сказали,что я могу отдохнуть")
        print("Меня позвали на улицу,и я поженился с девушкой-красавицей")
        print("Вы вышли на хорошую концовку,поздравляем!")
    if user == 2:
        print("я все таки поехал")
        print("я приехал в лес")
        print("и увидел белую дыру")
        print("я зашёл в неё")
        print("я шёл и шёл...")
        print("у меня резко потемнело в глазах, и я умер в этой белой дыре...")
        print("Вы вышли на плохую концовку...")
elif user == 3:
    print("я приехал в лес и нашел залежи золота")
    print("Я нагрузил коня и уехал обратно в богатый дом к своей жене")
    print("я приехал и выгрузил золото,и дальше мы жили долго и счастливо")
    print("Поздравляем,вы прошли игру на хорошую концовку")
else:
    print("Где ты такую дорогу увидел,мой дорогой (:")

print("Конец,Спасибо за игру!")


    



