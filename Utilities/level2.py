
level = [
    [" "," "," "," "," "," "," ",")"],
    ["T"," "," "," "," ","‾","‾","‾"],
    ["‾","‾","‾","‾","‾"," "," "]
]

turrets = []
character_location = [1,0] # Y,X, where Y goes from top

def get_level():
    return {
        "level":level,
        "turrets":turrets,
        "character_location":character_location
    }
