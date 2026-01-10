def items():
    inventorydict = {
        # Consumables

        "apple" : {
            "quantity" : 0,
            "name" : "Apple",
            "description" : "Food source.",
            "type" : "consumable",
            "cost" : 5,
        },

        "bread" : {
            "quantity" : 0,
            "name" : "Bread",
            "description" : "Food source.",
            "type" : "consumable",
            "cost" : 15,
        },

        "strawberry" : {
            "quantity" : 0,
            "name" : "Strawberry",
            "description" : "Food source",
            "type" : "consumable",
            "cost" : 5,
        },

        "water" : {
            "quantity" : 0,
            "name" : "Water",
            "description" : "Drink source",
            "type" : "consumable",
            "cost" : 2,
        },

        "beer" : {
            "quantity" : 0,
            "name" : "Beer",
            "description" : "Drink source",
            "type" : "consumable",
            "cost" : 30,
        },


        # Misc

        "coin" : {
            "quantity" : 5000,
            "name" : "Coin",
            "description" : "Currency and bribing",
            "type" : "misc",
        },

        "flower" : {
            "quantity" : 0,
            "name" : "Flower",
            "description" : "Beautiful, no?",
            "type" : "misc",
        },


        # Weapons

        "sword" : {
            "quantity" : 1,
            "name" : "Sword",
            "description" : "Used to fight off enemies. Good for small amounts of enemies.",
            "type" : "weapon",
            "health": 90,
            "damage" : 20,
            "areaDamage" : False
        },

        "mace" : {
            "quantity" : 1,
            "name" : "Mace",
            "description" : "Good for large hordes of enemies",
            "type" : "weapon",
            "health": 100,
            "damage" : 15,
            "areaDamage" : True
        },


        # Armour

        "helmet" : {
            "quantity" : 1,
            "name" : "Helmet",
            "description" : "A piece of armour used to protect your head",
            "type" : "armour",
            "health" : 30,
        },

        "flower_crown" : {
            "quantity" : 1,
            "name" : "Flower Crown",
            "description" : "Unexpectedly protective",
            "type" : "armour",
            "health" : 200
        },

        "chestplate" : {
            "quantity" : 1,
            "name" : "Chestplate",
            "description" : "A piece of armour used to protect your torso",
            "type" : "armour",
            "health" : 50,
        },

        "leggings" : {
            "quantity" : 1,
            "name" : "Leggings",
            "description" : "A piece of armour used to protect your legs",
            "type" : "armour",
            "health" : 20,
        },

        "boots" : {
            "quantity" : 1,
            "name" : "Boots",
            "description" : "A piece of armour used to protect your feet",
            "type" : "armour",
            "health" : 10,
        }
    }

    return inventorydict