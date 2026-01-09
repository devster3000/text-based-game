def locations():
    return {
        # Village Locations

        "village" : {
            "name" : "Village",
            "description" : "A small medieval village with wooden houses, thatch roofs and muddy paths.",
            "items" : None,
            "enemy" : None,
            "visited" : False
        },

        "arena" : {
            "name": "Fighting Arena",
            "description" : "A place where knights go to fight for money",
            "items" : "coin",
            "enemy" : "knight",
            "visited" : False
        },

        "well" : {
            "name": "Well",
            "description" : "It's a well.",
            "items" : "coin",
            "enemy" : "well monster",
            "visited" : False
        },

        "castle": {
            "name": "Castle",
            "description": "stone walls as high as mountain tops.",
            "items": "map",
            "enemy": "homeless",
            "visited": False
        },

        "market" : {
            "name" : "Market",
            "description" : "Where you go to buy things.",
            "items" : ["apple", "bread", "water", "beer"],
            "enemy" : "pickpocket",
            "visited" : False
        },

        "tavern" : {
            "name": "Tavern",
            "description" : "Buy a beer and hangout with your fellow medieval buddies",
            "items" : ["beer", "coin"],
            "enemy" : "drunk",
            "visited" : False
        },

        "house": {
            "name": "House",
            "description": "Your home. It's nice, isn't it?",
            "items": ["coin", "map", "apple"],
            "enemy": None,
            "visited": False
        },

        "cemetery" : {
            "name" : "Cemetery",
            "description" : "This is where you'll end up if you're not careful.",
            "items" : None,
            "enemy" : None,
            "visited" : False
        },


        # Forest Locations

        "forest" : {
            "name" : "Forest",
            "description" : "a dark, moody forest. Filled with an assortment of trees.",
            "items" : None,
            "enemy" : ["witch", "ogre"],
            "visited" : False
        },

        "witch hut" : {
            "name": "Witch Hut",
            "description" : "An old withering hut in the middle of the forest.",
            "items" : None,
            "enemy" : "witch",
            "visited" : False
        },


        # Mine Locations

        "mine" : {
            "name": "Mine",
            "description" : "Lots of miners here. And stone. And coal.",
            "items" : ["pickaxe", "stone"],
            "enemy" : None,
            "visited" : False
        },


        # Other Locations

        "strawberry field" : {
            "name" : "Strawberry Field",
            "description" : "pick some strawberries.",
            "items" : "strawberry",
            "enemy" : None,
            "visited" : False
        },

        "flower_field" : {
            "name" : "Flower Field",
            "description" : "stop and smell the flowers. relax.",
            "items" : "flower",
            "enemy" : "None",
            "visited" : False
        }

    }