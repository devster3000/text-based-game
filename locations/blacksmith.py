# blacksmith.py
from game.inventory import items
import time as t

def blacksmith(inv):

    shop_items = {
        "sword": 100,
        "mace": 150,
        "helmet": 50,
        "chestplate": 80,
        "leggings": 60,
        "boots": 40
    }

    inventorydict = inv

    print("\n// Welcome to the Blacksmith.")
    print("You see all sorts of weapons and armour on display.\n")
    t.sleep(1)

    coins = inventorydict.get("coin", {"quantity": 0})["quantity"]

    while True:
        print(f"You currently have {coins} coins.\n")
        print("Items available for purchase:")
        for item, price in shop_items.items():
            print(f"- {item.capitalize()} : {price} coins")

        choice = input("\nType the item name to buy, or 'leave' to exit the blacksmith.\n>>>").lower()

        if choice == "leave":
            print("You leave the blacksmith.\n")
            break

        if choice not in shop_items:
            print("Item not available. Try again.\n")
            continue

        price = shop_items[choice]

        if coins < price:
            print("Not enough coins!\n")
            continue

        # Add item to inventory
        item_entry = inventorydict.get(choice)
        if item_entry:
            item_entry["quantity"] += 1
        else:
            inventorydict[choice] = {"quantity": 1}  # fallback

        coins -= price
        inventorydict["coin"]["quantity"] = coins
        print(f"You purchased a {choice.capitalize()}! You now have {coins} coins remaining.\n")

    return inventorydict
