from time import sleep
import Utilities.level1 as level1
import Utilities.level2 as level2
import Utilities.level3 as level3
from colorama import init, Fore, Back,Style

init()

already_jumped = False

#back_fov = 2
#front_fov = 5

def deep_copy(mutable):
    if type(mutable)==list:
        return [deep_copy(m) for m in mutable]
    elif type(mutable)==dict:
        return {key: deep_copy(val) for key,val in mutable.items()}
    else:
        return mutable

class game_engine():
    def __init__(self):
        self.total_levels = 3

        self.game_maps = [level1.get_level(),level2.get_level(),level3.get_level()]

        self.game_maps_copy = deep_copy(self.game_maps) #mutability :C

        self.current_level = 1
        self.current_level_data = self.game_maps[self.current_level-1]

        self.map = self.current_level_data["level"]
        self.turrets = self.current_level_data["turrets"]
        self.character_location = self.current_level_data["character_location"]
        self.coins = 0
        self.game_moves = []

        self.game_over = False
        self.previous_render = None
        self.render()

    def restart(self):
        self.game_maps = deep_copy(self.game_maps_copy)
        self.current_level = 1
        self.current_level_data = self.game_maps[self.current_level-1]

        self.map = self.current_level_data["level"]
        self.turrets = self.current_level_data["turrets"]
        self.character_location = self.current_level_data["character_location"]
        self.coins = 0
        self.game_moves = []

        self.game_over = False

        self.render()


    def change_map(self):
        if self.current_level < self.total_levels:
            self.current_level +=1
            self.current_level_data = self.game_maps[self.current_level-1]
            self.map = self.current_level_data["level"]
            self.turrets = self.current_level_data["turrets"]
            self.character_location = self.current_level_data["character_location"]
            self.render()
        else:
            if not self.game_over:
                self.game_over_func("Win")

    def game_over_func(self,condition):
        if not self.game_over:
            self.game_over = True
            if condition=="loss":
                print('Game Over!')
            else:
                print("You Won!")
            print(f"Total score: {self.coins}")
            print("Enter \"R\" to restart")

    def check_collision(self,dir,location_to_check):
        if dir == "a":
            if location_to_check[1]<0:
                return "blocked"
        elif dir == "d":
            if location_to_check[1]>len(self.map[1])-1:
                return "blocked"
        elif dir=="w":
            if location_to_check[0]<0:
                return "blocked"
        elif dir=="s":
            if location_to_check[0]>len(self.map):
                return "blocked"
        map_object = self.map[location_to_check[0]][location_to_check[1]]
        if map_object==" ":
            return "empty"
        elif map_object==Fore.GREEN+"‾"+Style.RESET_ALL or map_object==Fore.LIGHTBLACK_EX+"_"+Style.RESET_ALL:
            return "blocked"
        elif map_object==Fore.YELLOW+"o"+Style.RESET_ALL:
            return "coin"
        elif map_object==Fore.RED+"-"+Style.RESET_ALL:
            return "laser"
        elif map_object==Fore.BLUE+")"+Style.RESET_ALL:
            return "portal"
        elif map_object==Fore.MAGENTA+"T"+Style.RESET_ALL:
            return "player"
    def move(self,move_to,coll):
        if coll!="laser" and coll!="portal":
            self.map[self.character_location[0]][self.character_location[1]]=" "
            self.character_location = [move_to[0],move_to[1]]
            self.map[self.character_location[0]][self.character_location[1]]=Fore.MAGENTA+"T"+Style.RESET_ALL
            if coll == "coin":
                self.coins+=1
        else:
            self.map[self.character_location[0]][self.character_location[1]]=" "
        self.render()

    def next_gamestate(self):
        global already_jumped
        if self.game_moves == []:
            self.game_moves.append("placeholder")
        for move in self.game_moves:
            coll = None
            location_to_check = self.character_location[:]
            if move == "w":
                if not already_jumped:
                    location_to_check[0]-=1
                    coll = self.check_collision("w",location_to_check)
                    already_jumped = True
                else:
                    coll = "blocked"
            elif move == "d":
                location_to_check[1]+=1
                coll = self.check_collision("d",location_to_check)
                already_jumped = False
            elif move == "a":
                location_to_check[1]-=1
                coll = self.check_collision("a",location_to_check)
                already_jumped = False
            if coll == "empty" or coll == "coin":
                self.move(location_to_check,coll)
            elif coll == "portal":
                self.move(location_to_check,coll)
                self.change_map()
                break
            elif coll == "laser":
                self.move(location_to_check,coll)
                self.game_over_func("loss")
                break
            

            if move != "w":
                location_to_check = [self.character_location[0]+1,self.character_location[1]]
                check_gravity = self.check_collision("",location_to_check)
                if check_gravity == "empty" or check_gravity == "coin":
                    self.move(location_to_check,check_gravity)
                elif check_gravity == "portal":
                    self.move(location_to_check,check_gravity)
                    self.change_map()
                    break
                elif check_gravity == "laser":
                    self.move(location_to_check,check_gravity)
                    self.game_over_func("loss")
                    break

            for turret in self.turrets:
                bullets_to_remove = []

                if turret["tick_num"]<turret["firerate"]-1:
                    turret["tick_num"]+=1
                else:
                    turret["tick_num"]=0
                    turret["bullets"].append({"loc":turret["location"],
                                              "time":0})
                for bullet in turret["bullets"]:
                    bullet["time"]+=0
                    if bullet["time"]<=turret["despawn_time"]:
                        if turret["dir"]=="left":
                            location_to_check = [bullet["loc"][0],bullet["loc"][1]-1]
                            coll = self.check_collision("a",location_to_check) 
                        elif turret["dir"]=="up":
                            location_to_check = [bullet["loc"][0]-1,bullet["loc"][1]]
                            coll = self.check_collision("w",location_to_check)
                        elif turret["dir"]=="right":
                            location_to_check = [bullet["loc"][0],bullet["loc"][1]+1]
                            coll = self.check_collision("d",location_to_check)
                        elif turret["dir"]=="down":
                            location_to_check = [bullet["loc"][0]+1,bullet["loc"][1]]
                            coll = self.check_collision("s",location_to_check)
                        if coll == "player":

                            if self.map[bullet["loc"][0]][bullet["loc"][1]] == Fore.RED+"-"+Style.RESET_ALL:
                                self.map[bullet["loc"][0]][bullet["loc"][1]] = " "
                            bullet["loc"] = location_to_check
                            self.map[bullet["loc"][0]][bullet["loc"][1]] = Fore.RED+"-"+Style.RESET_ALL

                            self.game_over_func("loss")
                            break
                        elif coll == "empty" or coll=="laser":
                            if self.map[bullet["loc"][0]][bullet["loc"][1]] == Fore.RED+"-"+Style.RESET_ALL:
                                self.map[bullet["loc"][0]][bullet["loc"][1]] = " "
                            bullet["loc"] = location_to_check
                            self.map[bullet["loc"][0]][bullet["loc"][1]] = Fore.RED+"-"+Style.RESET_ALL
                        else:
                            bullets_to_remove.append(bullet)
                    else:
                        self.map[bullet["loc"][0],bullet["loc"][1]]==" "
                        bullets_to_remove.append(bullet)
                for bullet in bullets_to_remove:
                    turret["bullets"].remove(bullet)
                    if bullet not in turret["bullets"]:
                        self.map[bullet["loc"][0]][bullet["loc"][1]] = " "
                bullets_to_remove = []
        self.render()
        self.game_moves = []
                
    def render(self):
        to_print = f"Coins:{self.coins}\n"
        for line in self.map:
            to_print+="".join(line)
            to_print+="\n"
        if self.previous_render!=to_print:
            self.previous_render = to_print
            print(to_print)
            sleep(0.5)