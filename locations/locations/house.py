import sys
from skills import *
from items import *
from inventory import *
import random as r
import time as t

def house():
    print("// Welcome to house.")
    print("Information about the surroundings")
    input(print("/* Something about user input */"))


    def bed():
        if sleeping >= 30:
            print("Sleeping...")
            return sleeping = 0

        elif sleeping < 30:
            print("Cannot sleep right now.")

    def chest():
        #Random amount of coins
        chest_coins = (r.randint(1, 5))
        input(print("You have found " + str(chest_coins) + " coins. Would you like to take them?" ))
        if input("Y" or "y"):
            print("+5 coins")
            inventory.update({coins: +chest_coins})
        elif input("N" or "n"):
            print("Okay. no coins for you then.")

        # Random weapon
        weapon = (r.randint(1, 4))
        if weapon == 1:
            print(" ")
            # /* TODO */
        elif weapon == 2:
            input(print("You have found a sword. How lucky. Do you want to take it? (Y/n) "))
            if input("Y" or "y"):
                inventory.update({sword: 40})
                print("+1 sword - 40 health")
            elif input("N" or "n"):
                print("Suit yourself.")
                weapon = 0

        elif weapon == 3:
            input(print("You have found a mace. How lucky. Do you want to take it? (Y/n) "))
            if input("Y" or "y"):
                inventory.update({mace: 60})
                print("+1 mace - 60 health")
            elif input("N" or "n"):
                print("Suit yourself.")
                weapon = 0

        elif weapon == 4:
            input(print("You have found a __. How lucky. Do you want to take it? (Y/n) "))
            if input("Y" or "y"):
                inventory.update({weapon : 100})
                print("+1 weapon - 100 health")
            elif input("N" or "n"):
                print("Suit yourself.")
                weapon = 0


        # Consumables
        chance = (r.randint(1, 30))
        food = {
            1 : "strawberry",
            2 : "apple",
            3 : "bread"
        }

        if chance <= 1 and chance >=10:
            chest_food = food[1]
        elif chance <=11 and chance >=20:
            chest_food = food[2]
        elif chance <=21 and chance >=30:
            chest_food = food[3]

        quantity = (r.randint(1, 4))

        if chest_food == food[1]:
            print("Wow! there is food in here!\n")
            print("You have a found", quantity, "strawberry. Congrats.\n")
            inventory.update({strawberry : quantity})
            print("+", quantity, "strawberry.")

        elif chest_food == food[2]:
            print("Wow! there is food in here!\n")
            print("You have a found", quantity, "apple. Congrats.\n")
            inventory.update({apple : quantity})
            print("+", quantity, "apple.")

        elif chest_food == food[3]:
            print("Wow! there is food in here!\n")
            print("You have a found", quantity, "bread. Congrats.\n")
            inventory.update({bread : quantity})
            print("+", quantity, "bread.")


    def window():
        input("\n\n Ahead is a window. Open it? (Y/n) ")
        if input("Y" or "y"):
            print("You open the window.\nThe window kills you.")
            t.sleep(2)

            sys.exit()
        elif input("N" or "n"):
            print("You didn't open the window. Good choice.")