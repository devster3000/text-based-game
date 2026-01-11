import time as t

# Function imports

from game.entities import *
from game.player import *
from game.locations import *
from game.inventory import *
from game.skills import *
from game.mechanics.combat import *
from game.map import *

# Location Imports
from locations.arena import *
from locations.house import *
from locations.blacksmith import *
from locations.tavern import *
from locations.field import *
from locations.castle import*
from locations.mines import *
from locations.market import *
from locations.well import *
from locations.fishing_pier import *
from locations.witch_hut import *


def main():
    skilldict = skills()
    inventorydict = items()

    print("Hello and also welcome to this game.\n")


    ### NAME GIVING ####

    name = input("What is your name? \n>>>")
    p = player(name)
    print("Hello,",p["name"])


    ### SKILL GIVING ###

    def skill_display():
        print("Your current skill levels are as follows: \n")

        for skill_key, skill_data in skilldict.items():
            print(skill_data["name"], "XP:", skill_data["xp"])

    def skill_picker():
        total_xp = 15
        while total_xp > 0:
            selection = input("Which skill do you want? \n- Press 's' for Strawberry Picking skill\n- Press 'sp' for Speed skill\n- Press 'd' for Drunk skill\n- Press 'c' for Combat skill.\n-- Press 'h' for current skill levels.\n>>>")

            match selection:
                case "s":
                    total_xp -= 1
                    skilldict["strawberry_picking"]["xp"] += 1
                    print("+1 XP to strawberry picking. There is ", skilldict["strawberry_picking"]["xp"]," strawberry picking XP in total.\n",total_xp,"XP Remaining")
                    skill_display()

                case "sp":
                    total_xp -= 1
                    skilldict["speed"]["xp"] += 1
                    print("+1 XP to speed. There is ", skilldict["speed"]["xp"],"speed XP in total.\n",total_xp,"XP Remaining")
                    skill_display()
                case "d":
                    total_xp -= 1
                    skilldict["drunk"]["xp"] += 1
                    print("+1 XP to drunk. There is ", skilldict["drunk"]["xp"],"drunk XP in total.\n",total_xp,"XP Remaining")
                    skill_display()

                case "c":
                    total_xp -= 1
                    skilldict["combat"]["xp"] += 1
                    print("+1XP to combat There is ", skilldict["combat"]["xp"],"combat XP in total.\n",total_xp,"XP Remaining")
                    skill_display()
                case "h":
                    print("### CURRENT XP LEVELS ###")
                    skill_display()
                case "skip":
                    total_xp = 0

    print("Loading...")
    t.sleep(2)
    print("Please select your skills.\n")
    t.sleep(1)
    skill_display()
    t.sleep(2)
    print("\n")
    skill_picker()


    ### === MAP SYSTEM ===

    inventory = items()
    entities_dict = entities()
    start_pos = [1, 4]

    while True:
        player_pos, location = map_system(start_pos)


        ## LOCATIONS
        if location == "house":
            inventory = house(p)


        elif location == "arena":
            print("You arrive at the arena. Combat goes here.")
            all_entities = entities()
            enemy_to_fight = {
                "name": all_entities["Guards"]["name"],
                "health": all_entities["Guards"]["health"],
                "damage": all_entities["Guards"]["damage"]
            }
            combat(p, enemy_to_fight)


        elif location == "blacksmith":
            inventory = blacksmith(inventory)


        elif location == "tavern":
            p, inventory = tavern(p, inventory, combat)


        elif location == "castle":
            p, inventory = castle(p, inventory, entities_dict, combat)


        elif location == "flower_field":
            p, inventory = flower_field(p, inventory)


        elif location == "strawberry_field":
            p, inventory = strawberry_field(p, inventory, skilldict)


        elif location == "mines":
            p, inventory = mines(player, inventory)


        elif location == "market":
            p, inventory = market(player, inventory)


        elif location == "witch_hut":
            p, inventory = witch_hut(player, inventory, combat)


        elif location == "well":
            p, inventory = well(player, inventory)


        elif location == "fishing_pier":
            p, inventory = fishing_pier(player, inventory)


        elif location is None:
            print("You quit the map.")
            break

        start_pos = player_pos


main()