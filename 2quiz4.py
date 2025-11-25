class GameCharacter:
    def attack(self):
        print(" ")

    def move(self):
        print(" ")

    def show_info(self):
        print(" ")


class Player(GameCharacter):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"{self.name} ba shamshir hamle mikonad! ghodrate zarbe: {self.power}")

    def move(self):
        print(f"{self.name} sari' harekat mikonad...")

    def show_info(self):
        print(f"Player -> nam: {self.name} | ghodrat: {self.power}")


class Enemy(GameCharacter):
    def __init__(self, name, power, attack_type):
        self.name = name
        self.power = power
        self.attack_type = attack_type

    def attack(self):
        print(f"{self.name} ba {self.attack_type} hamle mikonad! ghodrate zarbe: {self.power}")

    def move(self):
        print(f"{self.name} be arami va makhfi harekat mikonad...")

    def show_info(self):
        print(f"Enemy -> nam: {self.name} | ghodrat: {self.power} | noe hamle: {self.attack_type}")


p1 = Player("Arash", 50)
p2 = Player("Luna", 70)

e1 = Enemy("Goblin", 40, "dandan")
e2 = Enemy("Orc", 90, "tabar")

p1.show_info()
p1.move()
p1.attack()

print("-" * 40)

e1.show_info()
e1.move()
e1.attack()
