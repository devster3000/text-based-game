def player(name):
    player_dict = {
        "name": name,
        "health" : 100,
        "armour_health" : 0,
        "damage" : 20,
        "inventory" : [],
        "skills" : {
            "strawberry_picking" : 0,
            "speed" : 0,
            "combat" : 0,
            "swordsmanship" : 0,
            "mace_proficiency" : 0
        }
    }

    return player_dict