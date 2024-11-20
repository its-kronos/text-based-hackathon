from time import sleep
from Utilities import game_engine

print("Welcome! This is a 2D platformer. Your character is \"T\", turrets are the carot keys, and the goal is to get to the portals, which are parenthesis.\n\nThe controls are w,a, and d (all lowercase) and N to move to the next frame\n\n")

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