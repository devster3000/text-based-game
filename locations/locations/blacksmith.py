from game.items import *
from game.player import *

def blacksmith():
    print("// Welcome to blacksmith store.\n")
    input("// Have you things to upgrade (Y/n)\n")
    if input("Y" or "y"):
        print("Great. What would you like to upgrade?\n")
        print(" // WEAPONS INVENTORY // \n\n")
        print(items.get("weapons"))
    #Printing Weapons inventory
        if items["weapons"]["sword"]["quantity"] != 0:
            print("Sword Quantity: ", items["weapons"]["sword"]["quantity"])
        else:
            print("Sword Quantity: 0")

        if items["weapons"]["mace"]["quantity"] != 0:
            print("Mace Quantity: ", items["weapons"]["mace"]["quantity"])
        else:
            print("Mace Quantity: 0")

    #Upgrading weapons
    input("\nEnter item to upgrade: ")
    if input("sword" or "Sword"):
        print("Not implemented.")
    elif input("mace" or "Mace"):
        print("Not implemented.")

    input("\n\nWould you also like to upgrade any armour pieces?: ")
    if input("Y" or "y"):
        print(" // ARMOUR INVENTORY // \n\n")
        print(print(items.get("armour")))
    #Printing Armour Inventory
        if items["armour"]["helmet"]["quantity"] != 0:
            print("Helmet Quantity: ", items["armour"]["helmet"]["quantity"])
        else:
            print("\nNo helmet available\n")

        if items["armour"]["chestplate"]["quantity"] != 0:
            print("Chestplate Quantity: ", items["armour"]["chestplate"]["quantity"])
        else:
            print("\nNo chestplate available\n")

        if items["armour"]["leggings"]["quantity"] != 0:
            print("Leggings Quantity: ", items["armour"]["leggings"]["quantity"])
        else:
            print("\nNo leggings available\n")

        if items["armour"]["boots"]["quantity"] != 0:
            print("Boots Quantity: ", items["armour"]["boots"]["quantity"])
        else:
            print("\nNo boots available\n")