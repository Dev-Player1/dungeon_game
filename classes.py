from time import sleep
import random
import json

class Character:
    def __init__(self, name, hp, money, weapon, armor):
        self.name = name
        self.hp = hp
        self.money = money
        self.weapon = weapon
        self.armor = armor

    def is_dead(self):
        if self.hp <= 0:
            answer = True
            print(f"{self.name} мертв")
            return answer
        else:
            answer = False
            print(f"{self.name} жив")
            return answer
        
    def deal_damage(self, enemy):       
        dmg = self.weapon.damage - enemy.armor.defense
        if dmg <= 0:
            print("Урон не нанесется.")
        else:
            enemy.hp = enemy.hp - dmg
            print(f"{self.name} нанес {dmg} урона по {enemy.name}. Теперь у него осталось {enemy.hp} здоровья.")
            print()   
        
class Enemy(Character):
    def __init__(self, name, hp, money, weapon, armor, loyalty, cruelty):
        super().__init__(name, hp, money, weapon, armor)
        self.loyalty = loyalty
        self.cruelty = cruelty

class Hero(Character):
    def __init__(self, name, hp, money, weapon, armor):
        super().__init__(name, hp, money, weapon, armor)
        self.inventory = []

    def inventory_manager(self):
        print("Вы зашли в инвентарь")
        self.show_inventory()
        while True:
            answer = input("Какое действие вы выберете? \n1. Использовать предметы. \n2. Выйти из инвентаря. \n3. Экипировка.")
            print()
            if answer == "1":
                self.use_item()
            
            elif answer == "2":
                break
            
            elif answer == "3":
               self.show_equipment() 
            
            else:
                print("Что ты вводишь? Нет такой команды")
                

    def show_equipment(self):
        print(f"У вас оружие {self.weapon.name}")
        print(f" У вас броня {self.armor.name}")
        print(f"У вас {self.money} денег")
        print(f"У вас {self.hp} жизней")

    def use_item(self):
        self.show_inventory()
        answer = int(input("Какой предмет вы хотите использовать? "))
        print()
        if self.inventory == []:
            print("Инвентарь пустой")
            return
        elif answer > len(self.inventory):
            print("Такого элемента нет в инвентаре")
            return
        else:
            answer = answer - 1
            item = (self.inventory.pop(answer))
            if isinstance(item, Weapon):
                self.inventory.append(self.weapon) 
                self.weapon = item
                print(f"Экипирован {self.weapon.name}")
            elif isinstance(item, Armor):
                self.inventory.append(self.armor)
                self.armor = item
                print(f"Экипирован {self.armor.name}")
            elif isinstance(item , Healing):
                if item.name == "Heal_Box":
                    item.heal(self)
                elif item.name == "Pennyroyal_tea":
                    item.pen_tea(self)
            
              

    def show_inventory(self):
        counter = 1
        for i in self.inventory:
            print(f"{counter}. {i}")
            counter = counter + 1


class Weapon:
    def __init__(self, name, damage, price):
        self.name = name
        self.damage = damage
        self.price = price

    def __str__(self):
        return f"name: {self.name}, damage: {self.damage}, price: {self.price}"
    

class Armor:
    def __init__(self, name, defense, price):
        self.name = name
        self.defense = defense
        self.price = price

    def __str__(self):
        return f"name: {self.name}, defense: {self.defense}, price: {self.price}"
    
class Healing:
    def __init__(self, name, healing, price):
        self.name = name
        self.healing = healing
        self.price = price

    def __str__(self):
        return f"name: {self.name}, defense: {self.healing}, price: {self.price}"
   
    def heal(self, hero):       
        if hero.hp >= 100:
            choice = random.randint(1,3)
            if choice == 1:
                print("HEY!")
            elif choice == 2:
                print("WAIT!")
            elif choice == 3:
                print("I GOT A NEW COMPLAINT!")
        
        else:
            hero.hp = hero.hp + self.healing
            print(f"Использован {self.healing.name}")
            print(f"Ваше здоровье увеличилось на {self.healing} единиц")
    
    def pen_tea(self, hero):
        hero.hp = hero.hp + self.healing
        print(f"Использован {self.name}")
        print(f"Ваше здоровье увеличилось на {self.healing} единиц")
        text = random.randint(1,3)
        if text == 1:
            print("I'm on warm milk and laxitives. Cherry flavoured antacids")
        elif text == 2:
            print("Distill the life that inside of me")
        elif text == 3:
            print("I'm anemic royalty")
      

class Room:
    def __init__(self, name, enemies):
        self.name = name
        self.enemies = enemies

    def enter_room(self, hero):
        print(f"Ты зашел в комнату которая называется {self.name}")
        for enemy in self.enemies:
            self.start_fight(hero, enemy)
    
    def start_fight(self, hero, enemy):
        print(f"Ты начал бой с {enemy.name}")
        while not hero.is_dead() and not enemy.is_dead(): 
            hero.deal_damage(enemy)
            sleep(2)
            enemy.deal_damage(hero)
            sleep(2)
        if hero.is_dead() == False:
            self.get_loot(hero, enemy)
    
    def get_loot(self, hero, enemy):
        choice = random.randint(1, 3)
        if choice == 1:
            hero.money = hero.money + 5
            print(f"У вас теперь {hero.money} денег")

        elif choice == 2:
            hero.inventory.append(enemy.weapon)
            print(f"В ваш инвентарь добавилось {enemy.weapon}")

        elif choice == 3:
            hero.inventory.append(enemy.armor)
            print(f"В ваш инвентарь добавилось {enemy.armor}")        
        

class Dungeon:
    def __init__(self, name, rooms, hero, trader):
        self.name = name
        self.rooms = rooms
        self.counter = 0
        self.hero = hero
        self.trader = trader
        self.is_dungeon_finished = False


    def next_room(self):
        self.rooms[self.counter].enter_room(self.hero)
        self.counter = self.counter + 1
        len(self.rooms)
        if self.counter == len(self.rooms):
            self.is_dungeon_finished = True


    def dungeon_manager(self):
        while True:
            if self.is_dungeon_finished == True:
                print("Спасибо,что прошли игру!")
                break
            if self.hero.is_dead():
                print("Вы умерли. Как жаль")
                break
            
            answer = input("Какое действие ты выберешь? \n1. Зайти в следующую комнату \n2. Зайти к торговцу \n3. Открыть инвентарь \n4. Выйти из подземелья \n5. Сохранить игрока \n6. Загрузить игрока ")
            print()
            if answer == "1":
                self.next_room()
            
            if answer == "2":
                self.trader.trader_manager(self.hero)               

            if answer == "3":
                self.hero.inventory_manager()

            if answer == "4":
                print("Ты серьезно? Игра же только началась")
                if self.is_dungeon_finished == True:
                    print("Поздравляю! Вы прошли игру!")
            
            if answer == "5":
                self.save_player()

            if answer == "6":
                self.load_player()

    def save_player(self):
        player = {
            "name" : self.hero.name,
            "hp" : self.hero.hp,
            "money" : self.hero.money,
            "weapon" : {
                "name" : self.hero.weapon.name,
                "damage" : self.hero.weapon.damage,
                "price" : self.hero.weapon.price
            },
            "armor" : {
                "name" : self.hero.armor.name,
                "defense" : self.hero.armor.defense,
                "price" : self.hero.armor.price
            }
        }
        with open("save.json", "w", encoding="utf-8") as file:
            json.dump(player, file, ensure_ascii=False, indent=4)
    
    def load_player(self):
        with open("save.json", "r", encoding="utf-8") as file:
            player = json.load(file)
            name = player["name"]
            hp = player["hp"]
            money = player["money"]
            weapon = Weapon(player["weapon"]["name"], player["weapon"]["damage"], player["weapon"]["price"])
            armor = Armor(player["armor"]["name"], player["armor"]["defense"], player["armor"]["price"])
            self.hero = Hero(name, hp, money, weapon, armor)
class Trader:
    def __init__(self, name, goods, money):
        self.name = name
        self.goods = goods
        self.money = money

    def trader_manager(self, hero):
        print(f"Приветствую тебя у {self.name} торговца")
        while True:
            answer = input("Какое действие ты выберешь? \n1. Посмотреть товары и купить товары \n2. Продать вещи \n3. Выйти из магазина ")
            print()
            if answer == "1":
                self.buy_item(hero)

            if answer == "2":
                self.sell_item(hero)

            if answer == "3":
                break

    def buy_item(self, hero: Hero):
        self.show_trader_goods()
        try:
            answer = int(input("Какой товар ты хочешь купить, путник? Или нажми на 0 если не хочешь ничего покупать!"))
            print()
        except:
            print("Отвечай цифрами!!")   
            return
        
        if answer == 0:
            return
    
        if answer == "любой":
            print("Какой конкретно?")
            return
        
        if answer == "какой-то":
            print("Какой конкретно?")
            return
        
        if answer == "какой-нибудь":
            print("Какой конкретно?")
            return
        
        if answer > len(self.goods):
            print("Такого товара нет")
            return
    
        answer = answer - 1
        if hero.money > self.goods[answer].price:
            self.money = self.money + self.goods[answer].price
            hero.money = hero.money - self.goods[answer].price
            item = self.goods.pop(answer)
            hero.inventory.append(item)           
            print("I just want you to know that I dont hate you anymore!")
            print(f"Вы купили {item.name}")
            print(f"У вас сейчас {hero.money} денег")
            print(f"У {self.name} теперь {self.money} денег")
        else:
            choice = random.randint(1,2)
            if choice == 1:
                print(f"У тебя {hero.money} денег. Убирайся отсюда халявщик!")
            if choice == 2:
                print("Let's talk about someone else")

    def sell_item(self, hero: Hero):
        hero.show_inventory()
        try:
            answer = int(input("Какой товар ты хочешь продать, путник? Или нажми на 0 если не хочешь продавать!"))        
            print()
        except:
            print("Отвечай цифрами!!")
            return
        
        if answer == 0:
            return
        
        if len(hero.inventory) == 0:
            print("У тебя нет вещей! Что ты собираешься мне продать?")
            return
        
        if answer > len(hero.inventory):
            print("У тебя нет такого товара!")
            return
        answer = answer - 1
        if self.money > self.goods[answer].price:
            self.money = self.money - hero.inventory[answer].price
            hero.money = hero.money + self.goods[answer].price
            item = hero.inventory.pop(answer)
            self.goods.append(item)
            print(f"Вы продали {item.name}")
            print(f"У вас сейчас {hero.money} денег")
            print(f"У {self.name} теперь {self.money} денег")
        else:
            print(f"У меня мало денег. Я не смогу у тебя что либо купить")
    
    def show_trader_goods(self):
        counter = 1
        for i in self.goods:
            print(f"{counter}. {i}")
            counter = counter + 1





            
            



