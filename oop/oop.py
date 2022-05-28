class Character:
    def __init__(self, name, belly_size, chewing_speed):
        self.name = name
        self.max_fullness = 100
        self.lvl = 1
        self.fullness = 0
        self.belly_size = belly_size
        self.expirence = 1
        self.chewing_speed = chewing_speed

    def eat(self, food):
        #increase fullness based on cal
        if self.belly_size <= 2:
            self.fullness += round(food.cal * 0.1)
            self.max_fullness -= round(food.cal * 0.1)
        print("Yummy Yum Yum Yum")
        print(self.fullness)
        print(self.max_fullness)
        if self.max_fullness > 50:
            print("I can Keep Going!")
        else:
            print("I'm close to exploding from all this food!!")
        return self


class Food:
    def __init__(self, name, tastiness, cal):
        self.name = name
        self.tastiness = tastiness
        self.cal = cal


mario = Character("Mario", 2, 9, )
# raiden = Character("Raiden")

spaghetti = Food("spaghetti", 8, 600)
hotdog = Food("hotdog", 7, 200)

print(mario.fullness)
mario.eat(hotdog).eat(spaghetti)

print(mario.fullness)
