def blacksmith(player, inventory):
    choice = input("\n--- Blacksmith ---\n1. Repair armour (10 coins = +10 armour)\n2. Leave\n>>>")

    if choice == "1":
        coins = inventory["coin"]["quantity"]

        if coins < 10:
            print("Not enough coins.")
            return player, inventory

        max_repair = coins // 10
        print(f"You can repair up to {max_repair * 10} armour.")
        amount = input("How much armour do you want to repair? ")

        if not amount.isdigit():
            print("Invalid input.")
            return player, inventory

        amount = int(amount)

        cost = amount
        if cost > max_repair * 10:
            print("You don't have enough coins.")
            return player, inventory

        inventory["coin"]["quantity"] -= cost
        player["armour_health"] += amount

        print(f"+{amount} armour repaired!")
        print(f"Coins left: {inventory['coin']['quantity']}")

    print("You leave the blacksmith.\n")
    return player, inventory
