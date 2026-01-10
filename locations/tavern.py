import time as t
from game.entities import entities

def tavern(player, inventory, combat_func):
    print("\n// Tavern")
    print("The tavern smells like beer and poor decisions.")
    t.sleep(1)

    all_entities = entities()
    drunk = all_entities["Drunk"]

    BEER_PRICE = 10
    ROB_AMOUNT = 5

    def buy_beer():
        if inventory["coin"]["quantity"] < BEER_PRICE:
            print("You don't have enough coins.")
            return

        inventory["coin"]["quantity"] -= BEER_PRICE
        inventory["beer"]["quantity"] += 1
        print("You buy a beer.")

    def drink_beer():
        if inventory["beer"]["quantity"] <= 0:
            print("You have no beer.")
            return

        inventory["beer"]["quantity"] -= 1
        player["health"] += 5
        print("You drink the beer. +5 health.")

    def fight_drunk():
        if not drunk["alive"]:
            print("The drunk man is already unconscious.")
            return

        print("\nThe drunk man picks a fight!")
        t.sleep(1)

        combat_func(player, drunk)

        if not drunk["alive"]:
            print("\nThe drunk man collapses on the floor.")

            choice = input("Rob him for coins? (y/n): ").lower()
            if choice == "y":
                stolen = min(ROB_AMOUNT, inventory["coin"]["quantity"] + ROB_AMOUNT)
                inventory["coin"]["quantity"] += ROB_AMOUNT
                print(f"You steal {ROB_AMOUNT} coins.")
            else:
                print("You leave him alone.")

    while True:
        print("\n--- Tavern ---", f"Coins: {inventory['coin']['quantity']}")
        choice = input("1. Buy beer\n2. Drink beer\n3. Fight drunk man\n4. Leave\n>>>")

        choice = input("> ")

        if choice == "1":
            buy_beer()
        elif choice == "2":
            drink_beer()
        elif choice == "3":
            confirm = input("Are you sure you want to fight? (y/n): ").lower()
            if confirm == "y":
                fight_drunk()
            elif confirm == "n":
                print("Too late. The drunk man has already been provocated.\n")
                fight_drunk()
        elif choice == "4":
            print("You leave the tavern.")
            break
        else:
            print("Invalid option.")

    return player, inventory
