import random as r

def castle(player, inventory, entities_dict, combat):
    print("\n// You enter the Castle.\nGuards patrol the halls. Gold is everywhere.\n")

    robbed_total = 0
    guard_spawn_chance = 0.2  # 20% base chance

    while True:
        choice = input("\nWhat do you want to do?\n1. Rob 100 coins\n2. Look for guards\n3. Leave castle\n>>>")

        if choice == "1":
            print("You attempt to rob 100 coins...")

            if r.random() < guard_spawn_chance:
                print("A guard spots you!")

                guard = entities_dict["Guards"].copy()
                player = combat(player, guard)

                if not player["alive"]:
                    return player, inventory

            inventory["coin"]["quantity"] += 100
            robbed_total += 100
            guard_spawn_chance += 0.15

            print(f"+100 coins stolen (Total robbed: {robbed_total})")
            print(f"Guard spawn chance now {int(guard_spawn_chance * 100)}%")

            if robbed_total >= 1000:
                print("The castle treasury is empty.")
                break

        elif choice == "2":
            print("You look for trouble...")

            if r.random() < 0.7:
                guard = entities_dict["Guards"].copy()
                player = combat(player, guard)

                if not player["alive"]:
                    return player, inventory
            else:
                print("No guards engage you.")

        elif choice == "3":
            print("You leave the castle.")
            break

        else:
            print("Invalid choice.")

    return player, inventory
