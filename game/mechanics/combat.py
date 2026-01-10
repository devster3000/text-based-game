from game.entities import *
from game.player import *

def combat(player, enemy):

    print(f"\nCombat Start! You are fighting a {enemy['name']}\n")

    while enemy["health"] > 0 and player["health"] > 0:
        # --- Display status ---
        print(f"Your HP: {player['health']} | {enemy['name']} HP: {enemy['health']}")
        print("Choose your action:")
        print("1: Attack")
        print("2: Eat food (+20 HP)")

        choice = input(">>> ")

        # --- Player's turn ---
        if choice == "1":
            combat_skill = player.get("skills", {}).get("combat", 0)
            damage_done = player["damage"] + int(combat_skill * 0.2)  # +0.2 per XP point
            enemy["health"] -= damage_done
            print(f"\nYou hit {enemy['name']} for {damage_done} damage!")
        elif choice == "2":
            player["health"] += 5
            print(f"\nYou eat some food and restore 5 HP. Your health is now {player['health']}.")
        else:
            print("\nInvalid choice! You lose your turn.")

        # Check if enemy is defeated
        if enemy["health"] <= 0:
            print(f"\nYou have defeated the {enemy['name']}!")
            break

        # --- Enemy's turn ---
        player["health"] -= enemy["damage"]
        print(f"{enemy['name']} hits you for {enemy['damage']} damage. Your HP is now {player['health']}.\n")

        if player["health"] <= 0:
            print("\nYou have been defeated. Game Over!")
            break