# fishing.py
import time as t

def fishing_pier(player, inventory):
    print("\n// Fishing Pier\nThe water is calm. The smell of salt fills the air.")
    t.sleep(1)

    while True:
        choice = input("\n--- Fishing Pier ---\n1. Look at the water\n2. Sit and rest\n3. Leave the pier\n>>>")


        if choice == "1":
            print("You watch the water ripple gently. Fish dart beneath the surface.")
        elif choice == "2":
            print("You sit down and rest for a while.")
            player["health"] = min(player["health"] + 5, 100)
            print("You feel slightly refreshed.")
        elif choice == "3":
            print("You leave the fishing pier.")
            break
        else:
            print("Invalid option.")

    return player, inventory
