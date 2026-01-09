from game.player import *
from game.locations import *
from game.inventory import *
from game.skills import *
import time as t


def main():
    skilldict = skills()
    inventorydict = items()

    print("Hello and also welcome to this game.\n")


    ### NAME GIVING ####

    name = input("What is your name? \n>>>")
    p = player(name)
    print("Hello, ",p["name"])


    ### SKILL GIVING ###

    def skill_display():
        print("Your current skill levels are as follows: \n")

        for skill_key, skill_data in skilldict.items():
            print(skill_data["name"], "XP:", skill_data["xp"])

    def skill_picker():
        total_xp = 15
        while total_xp > 0:
            selection = input("Which skill do you want? \n- Press 's' for Strawberry Picking skill\n- Press 'sp' for Speed skill\n- Press 'd' for Drunk skill\n- Press 'c' for Combat skill.\n-- Press 'h' for current skill levels.\n>>>")

            match selection:
                case "s":
                    total_xp -= 1
                    skilldict["strawberry_picking"]["xp"] += 1
                    print("+1 XP to strawberry picking. There is ", skilldict["strawberry_picking"]["xp"]," strawberry picking XP in total.\n",total_xp,"XP Remaining")
                    skill_display()

                case "sp":
                    total_xp -= 1
                    skilldict["speed"]["xp"] += 1
                    print("+1 XP to speed. There is ", skilldict["speed"]["xp"],"speed XP in total.\n",total_xp,"XP Remaining")
                    skill_display()
                case "d":
                    total_xp -= 1
                    skilldict["drunk"]["xp"] += 1
                    print("+1 XP to drunk. There is ", skilldict["drunk"]["xp"],"drunk XP in total.\n",total_xp,"XP Remaining")
                    skill_display()

                case "c":
                    total_xp -= 1
                    skilldict["combat"]["xp"] += 1
                    print("+1XP to combat There is ", skilldict["combat"]["xp"],"combat XP in total.\n",total_xp,"XP Remaining")
                    skill_display()
                case "h":
                    print("### CURRENT XP LEVELS ###")
                    skill_display()

    print("Loading...")
    t.sleep(2)
    print("Please select your skills.\n")
    t.sleep(1)
    skill_display()
    t.sleep(2)
    print("\n")
    skill_picker()



    ## Combat





main()