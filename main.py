from time import sleep
from Utilities import game_engine
from Utilities import level1

total_levels = 1

game_maps = [level1.get_level()]
engine = game_engine.game_engine(game_maps[0]["level"],game_maps[0]["turret_locations"],game_maps[0]["character_location"])
engine.render()




while True:
    move = input("Input: ")
    if move == "N":
        engine.next_gamestate()
    elif move == "w" or move == "a" or move=="s" or move=="d":
        engine.game_moves.append(move)
    sleep(0.1)