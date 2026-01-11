# market.py
import time as t

def market(player, inventory):
    print("\n// Market\nThe market is busy and full of shouting merchants.")
    t.sleep(1)

    def get_price(item_key):
        if item_key == "flower_crown":
            return 10000
        return inventory[item_key]["cost"]

    def buy(item_key):
        price = get_price(item_key)

        if inventory["coin"]["quantity"] < price:
            print("You don't have enough coins.")
            return

        inventory["coin"]["quantity"] -= price
        inventory[item_key]["quantity"] += 1
        print(f"You bought 1 {inventory[item_key]['name']} for {price} coins.")

    while True:
        print("\n--- Market ---")
        print(f"Coins: {inventory['coin']['quantity']}")
        print(f"1. Buy apple ({inventory['apple']['cost']} coins)")
        print(f"2. Buy bread ({inventory['bread']['cost']} coins)")
        choice = input("3. Buy flower crown (10,000 coins)\n4. Leave\n>>>")

        if choice == "1":
            buy("apple")
        elif choice == "2":
            buy("bread")
        elif choice == "3":
            buy("flower_crown")
        elif choice == "4":
            print("You leave the market.")
            break
        else:
            print("Invalid option.")

    return player, inventory
