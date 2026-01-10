# blacksmith.py
import time as t

def blacksmith(inventory):
    print("\n// Blacksmith")
    print("The forge is blazing. The blacksmith eyes you up.\n")
    t.sleep(1)

    shop_prices = {
        "sword": 100,
        "mace": 150,
        "helmet": 50,
        "chestplate": 80,
        "leggings": 60,
        "boots": 40
    }

    def get_coins():
        return inventory["coin"]["quantity"]

    def spend_coins(amount):
        inventory["coin"]["quantity"] -= amount

    def show_inventory():
        print("\nYour inventory:")
        for key, data in inventory.items():
            if data["quantity"] > 0:
                print(f"- {data['name']} x{data['quantity']}")
        print()

    def buy_item():
        print("\nItems for sale:")
        for item, price in shop_prices.items():
            print(f"{item} - {price} coins")

        choice = input("Buy what? (or 'back'): ").lower()
        if choice == "back":
            return

        if choice not in shop_prices:
            print("That’s not sold here.")
            return

        price = shop_prices[choice]
        if get_coins() < price:
            print("You’re broke.")
            return

        inventory[choice]["quantity"] += 1
        spend_coins(price)
        print(f"You bought a {inventory[choice]['name']}.")

    def repair_item():
        repairables = {
            k: v for k, v in inventory.items()
            if v.get("health") and v["quantity"] > 0
        }

        if not repairables:
            print("Nothing to repair.")
            return

        print("\nRepairable items:")
        for item in repairables:
            print(item)

        choice = input("Repair what? (or 'back'): ").lower()
        if choice == "back":
            return

        if choice not in repairables:
            print("Can’t repair that.")
            return

        cost = 20
        if get_coins() < cost:
            print("Not enough coins.")
            return

        inventory[choice]["health"] += 10
        spend_coins(cost)
        print(f"{inventory[choice]['name']} repaired (+10 health).")

    def upgrade_item():
        upgradable = {
            k: v for k, v in inventory.items()
            if v["type"] in ["weapon", "armour"] and v["quantity"] > 0
        }

        if not upgradable:
            print("Nothing to upgrade.")
            return

        print("\nUpgradeable items:")
        for item in upgradable:
            print(item)

        choice = input("Upgrade what? (or 'back'): ").lower()
        if choice == "back":
            return

        if choice not in upgradable:
            print("Invalid choice.")
            return

        cost = 50
        if get_coins() < cost:
            print("You can’t afford that.")
            return

        if inventory[choice]["type"] == "weapon":
            inventory[choice]["damage"] += 5
            print(f"{inventory[choice]['name']} damage increased.")
        else:
            inventory[choice]["health"] += 15
            print(f"{inventory[choice]['name']} durability increased.")

        spend_coins(cost)

    while True:
        print(f"\nCoins: {get_coins()}")
        choice = input("1. Buy\n2, Repair\n3. Upgrade\n4. View Inventory\n5. Leave\n>>>")

        if choice == "1":
            buy_item()
        elif choice == "2":
            repair_item()
        elif choice == "3":
            upgrade_item()
        elif choice == "4":
            show_inventory()
        elif choice == "5":
            print("You leave the blacksmith.")
            break
        else:
            print("Pick a real option.")

    return inventory
