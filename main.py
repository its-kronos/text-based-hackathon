from time import sleep
from Utilities import game_engine

engine = game_engine.game_engine()

while True:
    move = input("Input: ")
    if not engine.game_over:
        if move == "N":
            engine.next_gamestate()
        elif move == "w" or move == "a" or move=="s" or move=="d":
            engine.game_moves.append(move)
    else:
        if move == "R":
            engine.restart()
    sleep(0.1)