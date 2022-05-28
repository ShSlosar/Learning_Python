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
print(f"{__name__} Imported")