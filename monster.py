import os
class Monster:
    def __init__(self,id,Name,Origin,Description,Attack,Magical_Force,Magical_Defence,Defence, Intelligence,Health):
        self.id = id
        self.Name = Name
        self.Origin = Origin
        self.Description = Description
        self.Attack = Attack
        self.Magical_Force = Magical_Force
        self.Magical_Defence = Magical_Defence
        self.Defence = Defence
        self.Intelligence = Intelligence
        self.Health = Health
    def __repr__(self):
        return self.Name
    def printme(self):
        print("ID:",self.id)
        print("Name",self.Name)
        print("Origin:",self.Origin)
        print("Description:",self.Description)
        print("Attack:",self.Attack)
        print("Magical Force:",self.Magical_Force)
        print("Magical Defence:",self.Magical_Defence)
        print("Defence:",self.Defence)
        print("Intelligence:",self.Intelligence)
        print("Health:",self.Health)
        print("\n")

monster_collection = []
def read_monsters():
        try:
            with open('Monsters.txt') as f:
                for line in f:
                    parts = line.split(",")
                    monster_collection.append(Monster(*parts[0:10]))
        except OSError:
            print("Sorry, could not find the file. Make sure it is in the correct directory. The current directory is",os.getcwd())
read_monsters()
for i in range(30):
    monster_collection[i].printme()
