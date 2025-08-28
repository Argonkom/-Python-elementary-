import random
import time

class Unit:

    def __init__(self, classes, HP, Mana):
        self.classes = classes
        self.HP = HP
        self.Mana = Mana 

    def info(self):
        return (f"{self.classes}. HP: {self.HP}, Mana: {self.Mana} ")


class Enemy:
    def __init__(self, classes, HP, Resist):
        self.classes = classes
        self.HP = HP
        self.Resist = Resist
    


Bigfoot = Enemy("Bigfoot", 250, "Ice")
spider = Enemy("Flamed spiders", 200,"Fire")
robot = Enemy("Rebellious mechanism", 350, "Arcane")
Enemies = [Bigfoot, spider, robot]
current_enemy = random.choice(Enemies)


class Spells():
    def Fire(self):
        if self.Mana <= 0:
            print("You are out of mana. Run!!!")
        self.Mana -= 50 
        if current_enemy == spider:
            current_enemy.HP -= 30
        else:
            current_enemy.HP -= 100
        print("Fireball!")


    def Ice(self):
        if self.Mana <= 0:
            print("You are out of mana. Run!!!")
        self.Mana -= 30
        if current_enemy == Bigfoot:
            current_enemy.HP -= 40
        else:
            current_enemy.HP -= 80
        print("Freeze!")
        


    def Arcane(self):
        if self.Mana <= 0:
            print("You are out of mana. Run!!!")
        self.Mana -= 200
        if current_enemy == robot:
            current_enemy.HP -= 80
        else:
            current_enemy.HP -= 200
        print("Come to the void!")


class Warrior(Unit, Spells):
    def __init__(self, classes, HP, Mana):
        super().__init__(classes, HP, Mana)

    def hammer(self):
        if self.Mana <= 0:
            print("You are out of mana. Run!!!")
        current_enemy.HP -= 50
        print("Smash!\n")


class Archer(Unit, Spells):
    def __init__(self, classes, HP, Mana):
        super().__init__(classes, HP, Mana)

    def arrow(self):
        if self.Mana <= 0:
            print("You are out of mana. Run!!!")
        current_enemy.HP -= 60
        print("Hit!")


class Mage(Unit, Spells):
    def __init__(self, classes, HP, Mana):
        super().__init__(classes, HP, Mana)


warrior = Warrior("Warrior", 350, 100)
archer = Archer("Archer", 250, 150)
mage = Mage("Mage", 200, 300)


#main
print("\nWelcome Stranger!\nChoose your class wisely:\n")
print("1.", warrior.classes)
print("2.",archer.classes)
print("3.",mage.classes)
option = int(input("\nChoose your class:\n"))
if option == 1:
    print("Here is your first enemy.He is enormous and horrifying.")
    while current_enemy.HP > 0:
        print("##########################")
        print(current_enemy.classes, "HP: ", current_enemy.HP, "\n")
        time.sleep(1.2)       
        print(warrior.info())
        print("1. ", warrior.hammer.__name__)
        print("2. ", warrior.Fire.__name__)
        action = int(input("\nTake your action:\n"))  
        if action == 1:
            warrior.hammer()
            if warrior.Mana <= 0:
                print("Not enough mana. You have to run!")
                break
        if action == 2: 
            warrior.Fire()
            if warrior.Mana <= 0:
                print("Not enough mana. You have to run!")
                break
        if current_enemy.HP <= 0:
            print("Congratulations! You won! Want to rest or continue your journey?")
            break
        print("The enemy hits you.")
        warrior.HP -= 75
        print(warrior.info())
        time.sleep(3)


if option == 2:
    print("Here is your first enemy.He is enormous and horrifying.")
    while current_enemy.HP > 0:

        print("##########################")
        print(current_enemy.classes, "HP: ", current_enemy.HP, "\n")
        time.sleep(1.2)
        print(archer.info())
        print("1. ", archer.arrow.__name__)
        print("2. ", archer.Ice.__name__)
        action = int(input("\nTake your action:\n"))
        if archer.Mana <= 0:
            print("Not enough mana")  
        if action == 1:
            archer.arrow()
            if archer.Mana <= 0:
                print("Not enough mana. You have to run!")
                break
        if action == 2: 
            archer.Ice()
            if archer.Mana <= 0:
                print("Not enough mana. You have to run!")
                break    
        if current_enemy.HP <= 0:
            print("Congratulations! You won! Want to rest or continue your journey?")
            break
        print("The enemy hits you.")
        archer.HP -= 75
        print(archer.info())
        time.sleep(3)
            


if option == 3:
    print("Here is your first enemy.He is enormous and horrifying.")
    while current_enemy.HP > 0:
        print("##########################")
        print(current_enemy.classes, "HP: ", current_enemy.HP, "\n")
        time.sleep(1.2)
        print(mage.info())
        print("1. ", mage.Fire.__name__)
        print("2. ", mage.Ice.__name__)
        print("3. ", mage.Arcane.__name__)
        action = int(input("\nTake your action:\n"))
        if action == 1:
            mage.Fire()
            if mage.Mana <= 0:
                print("Not enough mana. You have to run!")
                break
        if action == 2: 
            mage.Ice()
            if mage.Mana <= 0:
                print("Not enough mana. You have to run!")
        if action == 3: 
            mage.Arcane()
            if mage.Mana <= 0:
                print("Not enough mana. You have to run!")
        if current_enemy.HP <= 0:
            print("Congratulations! You won! Want to rest or continue your journey?")
            break
        print("The enemy hits you.")
        mage.HP -= 75
        print(archer.info())
        time.sleep(3)
