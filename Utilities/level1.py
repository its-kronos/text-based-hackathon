level = [
    [" ", " ", " ", " ", " "," "],
    ["T"," "," "," "," ","_","_"],
    ["_","_","_","_","_"," "," "]
]

turret_locations = []

character_location = [1,0] # Y,X, where Y goes from top

def get_level():
    return [level,turret_locations]