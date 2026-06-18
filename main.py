import time as t
import matplotlib.pyplot as plt


def convert_skills(choice):
    if choice == 1:
        conv_choice = "Defence"
    elif choice == 2:
        conv_choice = "Attack"
    elif choice == 3:
        conv_choice = "Thirst"
    elif choice == 4:
        conv_choice = "Hunger"
    elif choice == 5:
        conv_choice = "Strawberry Picking"
    else:
        conv_choice = "N/A"

    return conv_choice

def main():
    print(f"{'*'*7} Welcome to this Game!!! {'*'*7}")
    
    while True:
        try:
            username = str(input("What's your name, brave adventurer?\n>>> "))
        except:
            if len(username) < 3:
                print("Sorry, your name must be longer than 3 characters.")
                continue
            else:
                print(f"Welcome, {username}!")
                break

    # Skills variables definitions.
    skill_points = 7

    defence_skill = 0
    attack_skills = 0
    thirst_skill = 0
    hunger_skill = 0
    strawberry_skill = 0

    while True:

        print(f"Your current skillset is:\n \
            !! Skill Points Remaining: {skill_points} !!\n \
            1. Defence: {defence_skill}\n \
            2. Attack: {attack_skills}\n \
            3. Thirst: {thirst_skill}\n \
            4. Hunger: {hunger_skill}\n \
            5. Strawberry Picking: {strawberry_skill}")
        
        try:
            choice = int(input("Enter the skill you want to assign a skill point to\n>>> "))

            if choice < 1 or choice > 5:
                print("Sorry, you must enter a valid integer (1-5)")
                continue
            else:
                skill_points -= 1
                choice = convert_skills(choice)
                print(f"You chose {choice}. Good choice. You now have {skill_points} remaining.")

                if skill_points <= 0:
                    break
                else: continue

        except:
            print("Sorry, your input must be an integer.")
            continue

    print("Skill points have been assigned.")