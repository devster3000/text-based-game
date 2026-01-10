from game.locations import locations

def map_system(start_pos):
    MAP_WIDTH = 10
    MAP_HEIGHT = 10

    locationdict = locations()  # must return the dict in locations.py

    # Coordinates for each location (inside moat)
    location_coords = {
        "house": (1, 4),
        "arena": (2, 8),
        "blacksmith": (4, 5),
        "market": (4, 3),
        "tavern": (4, 4),
        "well": (2, 3),
        "castle": (3, 1),
        "strawberry_field": (8, 4),
        "flower_field": (8, 3),
        "forest": (5, 8),
        "witch_hut": (8, 8),
        "fishing": (3, 8),
        "mines": (8, 1)
    }

    # Symbols for each location
    location_symbols = {
        "house": "H",
        "arena": "A",
        "blacksmith": "B",
        "market": "M",
        "tavern": "T",
        "well": "W",
        "castle": "C",
        "strawberry_field": "S",
        "flower_field": "F",
        "forest": "R",    # R for forest
        "witch_hut": "U", # U for hut
        "fishing": "P",
        "mines": "N"
    }

    EMPTY = "."
    PLAYER = "@"
    MOAT = "~"

    # Ensure mutable copy of start_pos
    player_pos = list(start_pos)

    # ---------------- Draw the map ----------------
    def draw_map():
        print("\nMap:")
        for y in range(MAP_HEIGHT):
            row = ""
            for x in range(MAP_WIDTH):
                # moat edges
                if x == 0 or x == MAP_WIDTH-1 or y == 0 or y == MAP_HEIGHT-1:
                    row += MOAT + " "
                elif (x, y) == tuple(player_pos):
                    row += PLAYER + " "
                elif (x, y) in location_coords.values():
                    loc_names = [name for name, coords in location_coords.items() if coords == (x, y)]
                    if loc_names:
                        loc_name = loc_names[0]
                        row += location_symbols.get(loc_name, "?") + " "
                    else:
                        row += "?" + " "
                else:
                    row += EMPTY + " "
            print(row)

        # Legend
        print("\nLegend:")
        print(f"{PLAYER} = Player, {MOAT} = Moat, {EMPTY} = Empty")
        for loc_name, symbol in location_symbols.items():
            if locationdict.get(loc_name):
                print(f"{symbol} = {locationdict[loc_name]['name']}")
        print("")

    # Movement
    def move_player(direction):
        x, y = player_pos
        if direction.lower() == "w" and y > 1:
            player_pos[1] -= 1
        elif direction.lower() == "s" and y < MAP_HEIGHT - 2:
            player_pos[1] += 1
        elif direction.lower() == "a" and x > 1:
            player_pos[0] -= 1
        elif direction.lower() == "d" and x < MAP_WIDTH - 2:
            player_pos[0] += 1
        else:
            print("Can't move there! The moat blocks your path.")

    # On-location checker
    def check_location():
        for loc_name, coords in location_coords.items():
            if coords == tuple(player_pos):
                print(f"\nYou have arrived at {locationdict[loc_name]['name']}!")
                return loc_name
        return None

    #
    while True:
        draw_map()
        cmd = input("Move (wasd) or quit: ").lower()
        if cmd == "quit":
            break
        move_player(cmd)
        current_loc = check_location()
        if current_loc:
            return player_pos, current_loc  # trigger location in main.py

    return player_pos, None
