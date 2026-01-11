import random as r
import time as t
import sys

from netaddr import mac_pgsql

from game.inventory import *
def house(player):

    inventory = items()

    print(f"\nWelcome home, {player['name']}!")
    t.sleep(1)
    print("You look around your house. There's a bed, a chest, and a window.\n")

    def bed():
        print("You rest on your bed. Feeling refreshed!\n")
        t.sleep(1)
        return bed()

    def chest():
        print("You open the chest...\n")
        t.sleep(1)

        #  Coins
        chest_coins = r.randint(1, 5)
        choice = input(f"You found {chest_coins} coins. Take them? (Y/n) ").lower()
        if choice == "y":
            inventory["coin"]["quantity"] += chest_coins
            print(f"+{chest_coins} coins added! You now have {inventory['coin']['quantity']} coins.\n")
        else:
            print("You leave the coins behind.\n")

        #  Weapon
        weapons_list = ["sword", "mace"]
        weapon_found = r.choice(weapons_list + [None])
        if weapon_found:
            choice = input(f"You found a {inventory[weapon_found]['name']}. Take it? (Y/n) ").lower()
            if choice == "y":
                inventory[weapon_found]["quantity"] += 1
                print(f"{inventory[weapon_found]['name']} added to your inventory! Quantity: {inventory[weapon_found]['quantity']}\n")
            else:
                print(f"You leave the {inventory[weapon_found]['name']} behind.\n")
        else:
            print("No weapon found in the chest.\n")

        # Consumables
        consumables_list = ["strawberry", "apple", "bread"]
        chest_food = r.choice(consumables_list)
        quantity = r.randint(1, 4)
        inventory[chest_food]["quantity"] += quantity
        print(f"You found {quantity} {inventory[chest_food]['name']}(s) in the chest! Total: {inventory[chest_food]['quantity']}\n")

        return chest()

    def window():
        choice = input("There is a window in the room. Open it? (Y/n) ").lower()
        if choice == "y":
            print("You open the window.\nUh-oh… bad choice! Game over.")
            t.sleep(2)
            sys.exit()
        else:
            print("You wisely avoid the window.\n")

        return window()

    while True:
        action = input("Where do you want to go?\n1. Bed\n2. Chest\n3. Window\n4. Leave the house\n>>>")

        match action:
            case "1":
                bed()
                break
            case "2":
                chest()
            case "3":
                window()
            case "4":
                print("You leave the house.")
                break

    return inventory 
