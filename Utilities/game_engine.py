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

    def next_gamestate(self):
        pass