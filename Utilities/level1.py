level = [
    [" "," "," "," "," "," "," "," "],
    ["o"," "," "," "," "," ","o",")"],
    ["T"," ","o"," "," ","‾","‾","‾"],
    ["‾","‾","‾","‾","‾"," "," "," "]
]

turret_locations = []
character_location = [2,0] # Y,X, where Y goes from top

def get_level():
    return {
        "level":level,
        "turret_locations":turret_locations,
        "character_location":character_location
    }
