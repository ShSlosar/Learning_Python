class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
        
    def walk(self):
        print(f"{self.pet.name}, lets go for a walk!")
        self.pet.play()
        print(f"Woah! that was a great walk {self.pet.name}")
        return self
        #pass
    
    def feed(self):
        print(f"time to eat {self.pet.name}!")
        print(f"{self.pet.name} nibbles the {self.pet_food}")
        self.pet.eat()
        print(f"you really seem to like your {self.pet_food}!")
        return self
        #pass
    
    def bathe(self):
        print(f"time for your bath {self.pet.name}!")
        self.pet.noise()
        print("Scrub, Scrub....")
        print(f"Wow {self.pet.name}! So clean and sparkly!")
        self.pet.noise()
        #pass


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
        print(f"Woof! Woof! Borf! Borf!")
        self.health += 5
        print(f"{self.name}'s health has increased to : {self.health}!")
        return self
        #pass
    
    def noise(self):
        print("Borf! Borf! Arwooo!")
        #pass
    
doge = Pet("Doge", "shiba-inu", "rolls over")
han = Ninja("Han", "Solo", "Beggin Strips", "Kibble", doge)
#print(han.pet.name)
han.walk().feed().bathe()
doge.sleep()
