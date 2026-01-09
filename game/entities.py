def entities():
    entitiesdict = {
        ## Enemies
        "Guards" : {
            "name" : "Guards",
            "health" : 120,
            "damage" : 7,
            "items" : ["sword"]
        },
        "Goblin" : {
            "name" : "Goblin",
            "health" : 50,
            "damage" : 5,
            "items" : ["coins"]
        },
        "Spider" : {
            "name" : "Spider",
            "health" : 140,
            "damage" : 17,
            "items" : 0
        },

        ## Friendlies
        "Drunk" : {
            "name" : "Drunk",
            "health" : 50,
            "damage" : 2,
            "items" : ["coins"]
        },
        "Storeperson" : {
            "name" : "Storeperson",
            "health" : 50,
            "damage" : 300,
            "items" : ["coins", "bread"]
        },
        "Blacksmith" : {
            "name" : "Blacksmith",
            "health" : 50,
            "damage" : 300,
            "items" : ["coins", "sword", "mace", "helmet", "chestplate", "leggings", "boots"]
        },
        "Bartender" : {
            "name" : "Bartender",
            "health" : 50,
            "damage" : 300,
            "items" : ["coins", "beer"]
        }
    }