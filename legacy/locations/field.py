import random as r

def strawberry_field(player, inventory, skills):
    print("\n// You arrive at the Strawberry Field.\nRows of ripe strawberries stretch out in front of you.\n")

    while True:
        choice = input("What do you want to do?\n1. Pick strawberries\n2. Leave field\n>>>")

        if choice == "1":
            base_amount = r.randint(1, 3)

            skill_bonus = skills["strawberry_picking"]["xp"]
            total = base_amount + skill_bonus

            inventory["strawberry"]["quantity"] += total

            print(f"You pick {total} strawberries.")
            print(f"Total strawberries: {inventory['strawberry']['quantity']}")

        elif choice == "2":
            print("You leave the strawberry field.")
            break

        else:
            print("Invalid choice.")

    return player, inventory

def flower_field(player, inventory):
    print("\n// You arrive at the Flower Field.\nBeautiful colorful flowers bloom all around you.\n")

    while True:
        choice = input("What do you want to do?\n1. Pick flowers\n2. Leave field\n>>>")

        if choice == "1":
            amount = r.randint(1, 4)
            inventory["flower"]["quantity"] += amount

            print(f"You pick {amount} flowers.")
            print(f"Total flowers in inventory: {inventory['flower']['quantity']}")

        elif choice == "2":
            print("You leave the Flower Field.")
            break

        else:
            print("Invalid choice. Pick 1 or 2.")

    return player, inventory
