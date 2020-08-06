class Pokemon:
    # Initialise with core variables
    name = "Unknown"
    type = "Unknown"
    level = 1
    exp = 0
    level_exp = 20
    health = 0
    max_health = 0
    is_knocked_out = False
    speed = 0

    # Method to print summary of Pokemon's stats
    def summary(self):
        summary = "Name: {}\nType: {}\nLevel: {}\nExp: {}/{}\nHP: {}/{}\nSpeed: {}\n".format(
            self.name, self.type, self.level, self.exp, self.level_exp, self.health, self.max_health, self.speed)
        print(summary)

    # Constructor which prints summary after creation of new Pokemon
    def __init__(self, name, type, level=1):
        self.name = str.title(name)
        if self.max_health == 0:
            self.max_health = 25 + (level - 1) * 10
        self.health = self.max_health
        self.type = str.title(type)
        self.level = level
        self.level_exp = self.level * 20
        print(self.name + " was created!")
        self.summary()

    # Method to lose health
    def lose_health(self, damage):
        self.health -= damage
        # Check if health reduced to 0, then set is_knocked_out to True
        if self.health <= 0:
            self.health = 0
            self.is_knocked_out = True
        # Base string for reporting health loss
        report = "{} took {} damage and now has {}/{} hp!".format(
            self.name, damage, self.health, self.max_health)
        # Concatenate if knocked out
        if self.is_knocked_out:
            report += " {} is knocked out!".format(self.name)
        print(report)

    # Method to gain health
    def gain_health(self, heal):
        health_missing = self.max_health - self.health
        # Check if heal would overheal
        if health_missing < heal:
            heal = health_missing
        self.health += heal
        print("{} was healed for {} and now has {}/{} hp.".format(
            self.name, heal, self.health, self.max_health))

    # Method to gain exp
    def gain_exp(self, exp_gain):
        # Remaining exp until level up
        required_to_level = self.level_exp - self.exp
        # Initial report of actual exp gain
        print("{} gained {} exp.".format(self.name, exp_gain))
        # While loop which will systematically apply and use up the gained exp
        while exp_gain > 0:
            # If gained exp is enough to increase level, use that much gained exp, level up, set self.exp to 0, scale new level up requirement, scale new max health, heal to full and print report
            if exp_gain >= required_to_level:
                required_to_level = self.level_exp - self.exp
                exp_gain -= required_to_level
                self.level += 1
                self.exp = 0
                self.level_exp = self.level * 20
                self.max_health = int(self.max_health * 1.2)
                self.health = self.max_health
                print("{} grew to level {}!!".format(self.name, self.level))
            # Otherwise, remaining gained exp can simply be added to Pokemon's exp
            else:
                self.exp += exp_gain
                exp_gain = 0

    # Method to revive Pokemon
    def revive(self):
        if (self.is_knocked_out):
            self.is_knocked_out = False
            self.health = int(self.max_health * 0.2)
            print(self.name + " was revived with {} health".format(self.health))
        else:
            print(self.name + " is already conscious.")

    # Default attack
    def attack(self, enemy, damage=15, spell="Tackle"):
        self.attack_method(enemy, damage, spell)

    # Internal method to execute attack
    def attack_method(self, enemy, damage, spell):
        # Boolean variable if self.type has an advantage over enemy.type
        advantage = (self.type == "Grass" and enemy.type == "Water") or (
            self.type == "Water" and enemy.type == "Fire") or (self.type == "Fire" and enemy.type == "Grass") or (self.type == "Electric" and enemy.type == "Water")
        disadvantage = (self.type == "Grass" and enemy.type == "Fire") or (
            self.type == "Water" and enemy.type == "Grass") or (self.type == "Fire" and enemy.type == "Water")
        # Advantage deals double damage
        if advantage:
            print("{} used {} on {} for *{}* damage. It's super effective!".format(
                self.name, spell, enemy.name, damage*2))
            enemy.lose_health(damage*2)
        # Disadvantage deals half damage
        elif disadvantage:
            print("{} used {} on {} for ~{}~ damage. It's not very effective...".format(
                self.name, spell, enemy.name, int(damage/2)))
            enemy.lose_health(int(damage/2))
        # Otherwise deal full damage
        else:
            print("{} used {} on {} for {} damage.".format(
                self.name, spell, enemy.name, damage))
            enemy.lose_health(damage)

        # If knockout blow, gain exp
        if enemy.is_knocked_out:
            self.gain_exp(int(enemy.level_exp))
