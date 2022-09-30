import os

name = input("как зовут персонажа? ")
if name == "": name = "илья муромец"

way_1 = True
way_2 = True
way_3 = True
game = True
key = ""

while game:


    if (way_1 or way_2 or way_3) and key == "":
        key = ""
        os.system("cls")
        print(f"Подъезжает {name} к трем дорожкам, на перекрестке камень лежит, а на том камне написано: «Кто вправо поедет - тому убитым быть, кто влево поедет - тому богатым быть, а кто прямо поедет - тому женатым быть».Куда поехать?")
        if way_1:
            print("убитым быть")
        if way_2:
            print("богатым быть")
        if way_3:
            print("женатым быть")
        user_choice = input("какой вариант? Выбирай,1 дорога,2 дорога или 3 дорога")
        
        if user_choice == "1" and way_1:
            key += user_choice
        if user_choice == "2" and way_2:
            key += user_choice
        if user_choice == "3" and way_3:
            key += user_choice

        
    # РАЗБОЙНИКИ
    if key == "1" and way_1:
        os.system("cls")
        print("я могу поехать к разбойникам,но может в лесу что-то интересное?")
        print("ехать к разбойникам")
        print("поехать в другую сторону")
        user_choice = input("какой вариант?Выбирай,1 дорога или 2 дорога ")
        if user_choice == "1" or user_choice == "2":
            key += user_choice
        
    # РАЗБОЙНИКИ - ХОРОШИЙ ВАРИАНТ
    if key == "11" and way_1:
        os.system("cls")
        print("Поеду-ка я по той дорожке, где убитому быть. Умру в чистом поле, как славный богатырь!")
        print("И поехал он по дороге, где убитому быть.")
        print("Только он отъехал три версты, напали на него сорок разбойников.")
        print("Ну и я начал драться против разбойников и всех победил!")
        print("хорошая концовка")
        way_1 = False
        key = ""
        input("ENTER - дальше")

    # РАЗБОЙНИКИ - ПЛОХОЙ ВАРИАНТ
    if key == "12" and way_1:
        os.system("cls")
        print("Я решил поехать в другую сторону,а именно в лес,но я не увидел обрыв и упал")
        print("вы вышли на плохую концовку ):")
        game = False
        
    
    if key == "2" and way_2:
        os.system("cls")
        print("я приехал к груде золота,которая лежала рядом со мной,но я могу поехать в загадочный тоннель")
        print("собрать золото")
        print("поехать в тоннель")
        user_choice = input("какой вариант?Выбирай,1 дорога или 2 дорога")
        if user_choice == "1" or user_choice == "2":
            key += user_choice


    if key == "21" and way_2:
        os.system("cls")
        print("Я нагрузил коня и уехал обратно к себе домой")
        print("Вы вышли на хоршую концовку (:")
        way_2 = False
        key = ""
        input("ENTER - дальше")

    if key == "22":      
        os.system("cls")
        print("я зашел в тоннель,и увидел белую дыру,я дошёл туда,мне резко стало плохо,и я умер")
        print("Вы вышли на плохую концовку ):")
        game = False
        key = ""        

    if key == "3" and way_3:
        os.system("cls")     
        print("дорога 3")
        print("вариант 1")
        print("вариант 2")
        user_choice = input("какой вариант?Выбирай,1 дорога или 2 дорога")
        if user_choice == "1" or user_choice == "2":
            key += user_choice

    if key == "31" and way_3:
        os.system("cls")
        print("1 вариант хороший выбор")
        way_3 = False
        key = ""
        input("ENTER - дальше")    
    if key == "32":
        os.system("cls")
        print("2 вариант-плохой выбор")
        game = False




print("game end")         
          





