from pokemon import Pokemon


# Grass child class of Pokemon
class Grass(Pokemon):
    max_health = 40
    speed = -1

    def __init__(self, name, level=1):
        self.max_health = 40 + (level - 1) * 15
        self.health = self.max_health
        super().__init__(name, "Grass", level)

    def attack(self, enemy):
        damage = 5 + int(self.level * 10)
        self.attack_method(enemy, damage, "Drain Life")
        self.gain_health(int(damage / 2))


# Fire child class of Pokemon
class Fire(Pokemon):
    speed = 1

    def __init__(self, name, level=1):
        super().__init__(name, "Fire", level)

    def attack(self, enemy):
        damage = int(5 + self.level * 15)
        self.attack_method(enemy, damage, "Fire Blast")


# Water child class of Pokemon
class Water(Pokemon):

    def __init__(self, name, level=1):
        self.max_health = 30 + (level - 1) * 12
        self.health = self.max_health
        super().__init__(name, "Water", level)

    def attack(self, enemy):
        damage = int(15 + self.level * 5)
        self.attack_method(enemy, damage, "Bubble Gun")
        enemy.speed -= 1


# Electric child class of Pokemon
class Electric(Pokemon):
    speed = 3

    def __init__(self, name, level=1):
        super().__init__(name, "Electric", level)

    def attack(self, enemy):
        damage = int(10 + self.level * 10)
        self.attack_method(enemy, damage, "Shock")
        self.speed += 2
