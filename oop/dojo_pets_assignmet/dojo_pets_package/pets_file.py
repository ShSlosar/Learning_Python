class Pet:
    def __init__(self, name, typ, tricks):
        self.name = name
        self.type = typ
        self.tricks = tricks
        self.energy_lvl = 50
        self.health = 100
        
    def sleep(self):
        self.energy_lvl += 25
        print(f"{self.name} is lying down for a nice nap..")
        print("ZZzzzzzZZzzz...")
        print(f"{self.name}'s energy level is now: {self.energy_lvl}!")
        return self
        #pass
    
    def eat(self):
        print(f"Crunch! Crunch! Nom! Nom! Buuurp!")
        self.energy_lvl += 5
        self.health += 10
        print(f"{self.name}'s energy lvl is now: {self.energy_lvl} and their health is now: {self.health}!")
        return self
        #pass
    
    def play(self):
        print("PLAY TIME!")
        print(f"Woof! Woof! Borf! Borf!")
        self.health += 5
        print(f"{self.name}'s health has increased to : {self.health}!")
        return self
        #pass
    
    def noise(self):
        print("Borf! Borf! Arwooo!")
        #pass
    
print(f"{__name__} Imported")