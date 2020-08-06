import pokemon
import trainer
import types
Trainer = trainer.Trainer
Pokemon = pokemon.Pokemon


squirtle = types.Water("Squirtle")
bulbasaur = types.Grass("Bulbasaur")
charmander = types.Fire("Charmander", 2)
pikachu = types.Electric("Pikachu", 3)
ash = Trainer("Ash Ketchum", [bulbasaur, pikachu])
gary = Trainer("Gary Oak", [charmander])

###########

ash.pokemon_summary()
gary.pokemon_summary()
ash.attack(gary)
gary.attack(ash)
ash.add_pokemon(squirtle)
ash.set_active(squirtle)
ash.attack(gary)
bulbasaur.revive()
ash.heal(bulbasaur)
ash.pokemon_summary()
