class Person:

    moods = ("happy", "tired", "lazy")

    def __init__(self, name, money, mood="happy", healthRate=100):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def buy(self, items):
        if items <= 0:   
            print("Invalid number of items")
            return

        total_cost = items * 10

        if self.money >= total_cost:
            self.money -= total_cost
            print(f"{items} items purchased")
        else:
            print("Not enough money!")
 