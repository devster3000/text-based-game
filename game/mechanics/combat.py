from game.entities import *
from game.player import *

def apply_damage(player, damage):
    DAMAGE_REDUCTION = 0.25  # 25% reduction when armour exists

    if player["armour_health"] > 0:
        reduced_damage = int(damage * (1 - DAMAGE_REDUCTION))

        absorbed = min(player["armour_health"], reduced_damage)
        player["armour_health"] -= absorbed
        remaining = reduced_damage - absorbed

        print(f"Armour absorbed {absorbed} damage!")

        if remaining > 0:
            player["health"] -= remaining
            print(f"You take {remaining} HP damage!")
    else:
        player["health"] -= damage
        print(f"You take {damage} HP damage!")


def combat(player, enemy):

    print(f"\nCombat Start! You are fighting a {enemy['name']}\n")

    while enemy["health"] > 0 and player["health"] > 0:
        # --- Display status ---
        print(f"HP: {player['health']} | Armour: {player['armour_health']} | "f"{enemy['name']} HP: {enemy['health']}","\nChoose your action:\n1. Attack\n2. Eat food")
        choice = input(">>>")

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
        apply_damage(player, enemy["damage"])
        print(f"{enemy['name']} hits you for {enemy['damage']} damage. Your HP is now {player['health']}.\n")

        if player["health"] <= 0:
            print("\nYou have been defeated. Game Over!")
            break