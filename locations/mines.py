# mines.py
import random as r
import time as t

def mines(player, inventory):
    print("\n// Mines\nThe air is thick with dust. Pickaxes echo in the tunnels.")
    t.sleep(1)

    def mine():
        roll = r.random()

        if roll <= 0.001:
            coins_found = 100000
            print("JACKPOT")
            print("You strike a massive vein of treasure!")
        else:
            coins_found = r.randint(1, 100)
            print(f"You mine the rock and find {coins_found} coins.")

        inventory["coin"]["quantity"] += coins_found
        print(f"Total coins: {inventory['coin']['quantity']}")

    while True:
        choice = input("\n--- Mines ---\n1. Mine for coins\n2. Leave\n>>>")

        if choice == "1":
            mine()
        elif choice == "2":
            print("You leave the mines.")
            break
        else:
            print("Invalid option.")

    return player, inventory
