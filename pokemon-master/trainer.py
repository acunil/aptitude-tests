class Trainer:
    name = "Unknown"
    pokemon_roster = []
    active_pokemon = 0
    potions = 3

    # Method to print summary of trainer
    def summary(self):
        pokemon_names = []
        for p in self.pokemon_roster:
            pokemon_names.append(p.name)
        print("Name: {}\nPokemon: {}\nNum. Potions: {}\n".format(
            self.name, ", ".join(pokemon_names) or "None", self.potions))

    # Constructor function
    def __init__(self, name, pokemon_roster=[], potions=3):
        self.name = name
        self.pokemon_roster = pokemon_roster
        self.potions = potions
        print("New trainer created!")
        self.summary()

    # Method to print summary of trainer's Pokemon roster
    def pokemon_summary(self):
        print(self.name + "'s roster: ---------")
        for poke in self.pokemon_roster:
            poke.summary()
        print("-------------------------------")

    # Method to add Pokemon to roster
    def add_pokemon(self, pokemon):
        if len(self.pokemon_roster) < 6:
            self.pokemon_roster.append(pokemon)
            print("{} was added to {}'s roster.".format(
                pokemon.name, self.name))
            self.pokemon_summary()
        else:
            print("Your roster is full.")

    # Method to heal a Pokemon
    def heal(self, pokemon, potion_strength=20):
        if pokemon not in self.pokemon_roster:
            print("{} does not own a {}.".format(self.name, pokemon))
        elif self.potions > 0:
            print("{} used a potion (+{}) on {}.".format(
                self.name, potion_strength, pokemon.name))
            pokemon.gain_health(potion_strength)
            self.potions -= 1
            print("{} has {} potions left.".format(self.name, self.potions))
        else:
            print(self.name + " is out of potions.")

    # Method to set active Pokemon
    def set_active(self, pokemon):
        index = None
        for poke in self.pokemon_roster:
            if poke.name == pokemon.name:
                index = self.pokemon_roster.index(poke)
        target = self.pokemon_roster[index]
        # Check if conscious and set as active
        if target.is_knocked_out:
            print(target.name + " is knocked out and can't be made active.")
        else:
            self.active_pokemon = index
            print(self.pokemon_roster[index].name + " is now active.")

    # Method to attack another trainer
    def attack(self, enemy):
        self.pokemon_roster[self.active_pokemon].attack(
            enemy.pokemon_roster[enemy.active_pokemon])
