def entities():
    return {
        ## Enemies
        "Guards" : {
            "name" : "Guards",
            "health" : 120,
            "damage" : 7,
            "items" : ["sword"],
            "skills" : ["combat"],
            "alive" : True,
        },
        "Goblin" : {
            "name" : "Goblin",
            "health" : 50,
            "damage" : 5,
            "items" : ["coins"],
            "skills" : ["drunk"],
            "alive" : True,
        },
        "Spider" : {
            "name" : "Spider",
            "health" : 140,
            "damage" : 17,
            "items" : 0,
            "skills" : ["combat"],
            "alive" : True,
        },

        ## Friendlies
        "Drunk" : {
            "name" : "Drunk",
            "health" : 50,
            "damage" : 2,
            "items" : ["coins"],
            "skills" : ["drunk"],
            "alive" : True,
        },
        "Storeperson" : {
            "name" : "Storeperson",
            "health" : 50,
            "damage" : 300,
            "items" : ["coins", "bread"],
            "skills" : ["speed"],
            "alive" : True,
        },
        "Blacksmith" : {
            "name" : "Blacksmith",
            "health" : 50,
            "damage" : 300,
            "items" : ["coins", "sword", "mace", "helmet", "chestplate", "leggings", "boots"],
            "skills" : ["speed"],
            "alive" : True,
        },
        "Bartender" : {
            "name" : "Bartender",
            "health" : 50,
            "damage" : 300,
            "items" : ["coins", "beer"],
            "skills" : ["speed"],
            "alive" : True,
        }
    }