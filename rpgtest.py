# Video at tutorial at: https://youtu.be/hg2NkuLLqcw
#This is the completed file

#This is used for teaching A-level Computer science. There's a few concepts that aren't very pythonistic. 

import random
import time

class Character: #Class
    def __init__(self):
        self.name = ""
        self.attack = 0
        self.defence = 0
        self.health = 0 #Demo private attribute
        self.experience = 0

    def print_basics(self): 
        print("\nName:       ",self.name)
        print("attack:     ",self.attack)
        print("defence     ",self.defence)
        print("health:     ",self.health)
        print("experience: ",self.experience)
    

    def setter(self,name):#setter
        self.name = name
        self.attack = random.randint(0,50)
        self.defence = random.randint(0,50)
        self.health = random.randint(30,50)

    def health_getter(self): # Not really needed for Python
        return self.health

    def print_me(self):
        self.print_basics()


class wizard(Character):
    def __init__(self):
        Character.__init__(self) #need to add in parent classes
        self.magic = 30

    def print_me(self):
        self.print_basics()
        print("magic       ",self.magic) #polymorphism



class knight(Character):
    def __init__(self):
        Character.__init__(self) #need to add in parent classes
        self.armour = 30

    def print_me(self):
        self.print_basics()
        print("armour      ",self.armour) #polymorphism

caste = input("\nWould you like to be a Wizard or Knight? W or K")
char_name = input("And what is your name?")

if caste.upper() == "K":
    print("A great knight is created!")
    you = knight()
elif caste.upper() == "W":
    print("A great wizards shimmers into existance")
    you = wizard()
else:
    print("\nTyping W or K too much for you! \nClearly you plan to die...\nBasic peasant for you!")
    you = Character()

you.setter(char_name)
you.print_me()
goblin1 = Character() 
goblin1.setter("goblin1")
goblin1.print_basics()
print("You encounter a goblin!\n")
while goblin1.health >0:
    time.sleep(0.3)
    attack = input("Which attack would you like to use: Fireball or Melee\n")
    if attack.upper() =="FIREBALL":
        dmgdealt = (you.magic/2)*round(random.uniform(0,2),1)
        goblin1.health = goblin1.health - dmgdealt
        time.sleep(0.3)
        print(f"You did {dmgdealt} damage with your mighty fireball!")
        time.sleep(0.3)
        print("Goblin HP is now:",round(goblin1.health_getter(),2))
    if attack.upper() =="MELEE":
        dmgdealt = (you.attack/2)*round(random.uniform(0,2),1)
        goblin1.health = goblin1.health - dmgdealt
        time.sleep(0.3)
        print(f"You did {dmgdealt} damage with your weighty slash!")
        time.sleep(0.3)
        print("Goblin HP is now:",round(goblin1.health_getter(),2))
    elif attack.upper() != "MELEE" and attack.upper() != "FIREBALL" :
        print("You fool, you failed to attack successfully and the goblin has now healed!")
        goblin1.health += random.randint(1,10)
        time.sleep(0.3)
        print("Goblin HP is now:",round(goblin1.health_getter(),2))
print("Congratulations! You are triumphant, for now...")
