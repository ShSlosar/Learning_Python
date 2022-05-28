from dojo_pets_package.ninja_file import Ninja
from dojo_pets_package.pets_file import Pet

class Dog(Pet):
    def __init__(self, name, typ, breed, tricks):
        super().__init__(name, typ, tricks)
        self.breed = breed

    def whats_my_dogs_breed(self):
        print(f"{self.name}'s breed is: {self.breed}!")
        self.noise()

class Cat(Pet):
    def __init__(self, name, typ, breed, tricks= "Meow?"):
        super().__init__(name, typ, tricks)
        self.breed = breed
        
    def noise(self):
        print("MEEEOOOOOWWW!!")
    
    def play(self):
        print("PLAY TIME!")
        print(f"Purr Purr Meow!")
        self.health += 5
        print(f"{self.name}'s health has increased to : {self.health}!")
        return self
        #pass
    def eat(self):
        print("Nibble.. Nibble.. Crunch")
        self.energy_lvl += 5
        self.health += 10
        print(f"{self.name}'s energy lvl is now: {self.energy_lvl} and their health is now: {self.health}!")
        return self
        #pass
    
doge = Dog("Doge", "Dog", "Shiba-Inu", "Rolls Over")
han = Ninja("Han", "Solo", "Beggin Strips", "Kibble", doge)
mrTibbs = Cat("Mr.Tibbs", "Cat", "Tabby")
john = Ninja("John", "Solo", "Cat-Nip", "Tuna", mrTibbs)
print(john.pet.name)
mrTibbs.eat().play()
print(han.pet.name)
han.pet.whats_my_dogs_breed()
han.walk().feed().bathe()
doge.sleep()
