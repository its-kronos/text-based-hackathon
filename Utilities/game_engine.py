from time import sleep

back_fov = 2
front_fov = 5

class game_engine():
    def __init__(self,game_map,turret_locations,character_location):
        self.map = game_map
        self.turret_locations = turret_locations
        self.coins = 0
        self.character_location = character_location
        self.game_moves = []

    def change_map(self,new_map,turret_locations,character_location):
        self.map = new_map
        self.turret_locations = turret_locations
        self.character_location = character_location

    def check_collision(self,dir,location_to_check):
        if dir == "a":
            if location_to_check[1]<0:
                return "blocked"
        elif dir == "d":
            if location_to_check[1]>len(self.map[1])-1:
                return "blocked"
        map_object = self.map[location_to_check[0]][location_to_check[1]]
        if map_object==" ":
            return "empty"
        elif map_object=="_":
            return "blocked"
        elif map_object=="o":
            return "coin"
        elif map_object=="-":
            return "laser"

    def move(self,move_to,coll):
        self.map[self.character_location[0]][self.character_location[1]]=" "
        self.character_location = [move_to[0],move_to[1]]
        self.map[self.character_location[0]][self.character_location[1]]="T"
        if coll == "coin":
             self.coins+=1
        self.render()

    def next_gamestate(self):
        if self.game_moves == []:
            self.game_moves.append("placeholder")
        for move in self.game_moves:
            coll = None
            location_to_check = self.character_location[:]
            if move == "w":
                location_to_check[0]-=1
                coll = self.check_collision("w",location_to_check)
            elif move == "d":
                location_to_check[1]+=1
                coll = self.check_collision("d",location_to_check)
            elif move == "a":
                location_to_check[1]-=1
                coll = self.check_collision("a",location_to_check)
            if coll == "empty" or coll == "coin":
                self.move(location_to_check,coll)
            

            if move != "w":
                location_to_check = [self.character_location[0]+1,self.character_location[1]]
                check_gravity = self.check_collision("",location_to_check)
                if check_gravity == "empty" or check_gravity == "coin":
                    self.move(location_to_check,check_gravity)
        
        self.game_moves = []
                
    def render(self):
        print(self.map)
        sleep(0.5)