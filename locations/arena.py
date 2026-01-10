from game.entities import *
from game.mechanics.combat import *

def arena_scene(player):
    print("\nWelcome to the Arena! Guards are here to fight you!\n")

    all_entities = entities()  # get all enemy templates

    # Spawn a guard
    enemy_to_fight = {
        "name": all_entities["Guards"]["name"],
        "health": all_entities["Guards"]["health"],
        "damage": all_entities["Guards"]["damage"]
    }

    # Start combat
    combat(player, enemy_to_fight)

    print("You survived the arena!\n")
