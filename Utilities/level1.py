import Utilities.map_color_code

level = [
    [" "," "," "," "," "," "," "," "," "," "],
    [" "," "," ","o"," "," ","o"," "," "," "],
    ["_","_"," "," "," "," "," "," "," "," "],
    ["T"," "," ","o","‾","‾","‾"," "," ",")"],
    ["‾","‾","‾","‾"," "," "," ","‾","‾","‾"]
]

level = Utilities.map_color_code.color_code(level)

turrets = []

character_location = [3,0] # Y,X, where Y goes from top

def get_level():
    return {
        "level":level,
        "turrets":turrets,
        "character_location":character_location
    }
