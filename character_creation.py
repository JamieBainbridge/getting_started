"""
auto create up to 7 players using random selection on predefined lists
"""
import random

def show_players(created_players: dict, player_select = -1):
    """show either all created players or a selected players stats and attributes"""

    # create empty list to reference all created players or selected player only
    characters = []
    for keys in created_players:
        characters.append(keys)
    if player_select > -1:
        character = characters.pop(player_select)
        characters.clear()
        characters.append(character)

    # loop through list of character(s) and print the character details
    for i in characters:
        character_dict = created_players[i]
        print(f"\n{i}")
        for sub_keys in character_dict:
            attribute = created_players[i][sub_keys]
            print(f"{sub_keys}: {attribute}")

def player_dict(name, player_class, race, origin):
    """create a dictionary to hold players details selected from list"""
    player = dict()
    player["name"] = name
    player["player_class"] = player_class
    player["race"] = race
    player["origin"] = origin
    player["stats"] = assign_stats(21)
    return player

def assign_stats(stats_pool: int):
    """randomly assign stats to attribute"""
    # create dict of stat categories
    stats = {
        "Strength": 0,
        "Agility": 0,
        "Stamina": 0,
        "Intellect": 0,
        "Wisdom": 0,
        "Perception": 0,
        "Resolve": 0
        }
    # randomly assign stats to stat categories until no stat points remain
    while stats_pool > 0:
        for x, y in stats.items():
            if stats_pool > 4:
                increase = random.randrange(0,3)
                y += increase
                stats.update({x: y})
                stats_pool -= increase
            elif stats_pool > 0:
                increase = 1
                y += increase
                stats.update({x: y})
                stats_pool -= increase
    return stats

def player_create(num_players: int):
    """for number of players selected, randomly generate unique characters and return as dict"""
    # loop to select random item from each charecteristic list and assign to player
    while num_players >= 1:
        player_number = player_numbers.pop(0)
        name = names.pop(random.randrange(0,len(names)))
        player_class = player_classes.pop(random.randrange(0,len(player_classes)))
        race = races.pop(random.randrange(0,len(races)))
        origin = origins.pop(random.randrange(0,len(origins)))
        players_dict.update({player_number: player_dict(name, player_class, race, origin)})
        num_players -= 1
    return players_dict

def user_input(stock_msg="Please enter a number: ", start= 0, end= -1):
    """Requests input from user to make selection between a given range

    Args:
        stock_msg (str, optional): message displayed to user. Defaults to "Please enter a number: ".
        start (int, optional): bottom limit of range. Defaults to 0.
        end (int, optional): top limit of range. Defaults to -1.
    """
    while True:
        try:
            selection = int(input(f"{stock_msg}"))
        except ValueError:
            print("Sorry, that input was not recognised. Please try again.\n")
            continue
        if not start <= selection <= end:
            print("Sorry, that input was not recognised. Please try again.\n")
            continue
        return selection

# set lists for player designations, names, classes, races and origins
players_dict = {}
player_numbers = ["Player_1","Player_2","Player_3","Player_4","Player_5","Player_6","Player_7"]
names = ["Jane","Jeremy","Jackie","Janice","John","Jeremiah","Jill"]
player_classes = ["Paladin","Ranger","Barbarian","Berserker","Cleric","Rogue","Monk"]
races = ["Elf","Human","Orc","Goblin","Gnome","Dwarve","Dragon"]
origins = ["Gladiator","Trader","Raider","Poacher","Lord","Prisoner","Peasant"]

print("Hello! Welcome to Character Creation. This program will create up to 7 unique characters.")

number_players = user_input("Please enter number of players to create: ", 1, 7)
players = player_create(number_players)

show_players(players)
