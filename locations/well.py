# well.py
import time as t
import sys

def well(player, inventory):
    print("\n// Well\nAn old stone well sits in the center of the village.")
    t.sleep(1)

    while True:
        choice = input("\n--- Well ---\n1. Look into the well\n2. Jump into the well\n3. Leave\n>>>")

        if choice == "1":
            print("You peer down. It’s very deep. You hear water far below.")
        elif choice == "2":
            confirm = input("This seems like a terrible idea. Jump anyway? (y/n): ").lower()
            if confirm == "y":
                inventory["coin"]["quantity"] += 1_000_000
                print("\nYou fall…")
                t.sleep(1)
                print("You land in water.")
                t.sleep(1)
                print("At the bottom, you find an impossible amount of treasure.\nBut the walls are smooth. There is no way out.\nYou gained 1,000,000 coins.\nYou died.")
                sys.exit()
        elif choice == "3":
            print("You step away from the well.")
            break
        else:
            print("Invalid option.")

    return player, inventory
