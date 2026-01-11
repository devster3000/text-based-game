# witch_hut.py
import time as t
from game.entities import entities

def witch_hut(player, inventory, combat_func):
    print("\n// Witch Hut\nA crooked hut stands deep in the woods. Something watches you.")
    t.sleep(1)

    all_entities = entities()
    witch = all_entities["Witch"]

    while True:
        choice = input("\n--- Witch Hut ---\n1. Look around\n2. Enter the hurt\n3. Leave\n>>>")

        if choice == "1":
            print("Bones hang from the roof. The air smells of rot and herbs.")

        elif choice == "2":
            if not witch["alive"]:
                print("The hut is silent. The witch has already been defeated.")
                continue

            print("\nThe witch screeches and attacks!")
            t.sleep(1)
            combat_func(player, witch)

            if not witch["alive"]:
                print("\nThe witch collapses into dust.\nYou feel like this will have consequences…")

        elif choice == "3":
            print("You back away from the hut.")
            break

        else:
            print("Invalid option.")

    return player, inventory
