import Utilities.map_color_code

level = [
    [" "," "," "," "," "," "," "," "," "," "," "," "],
    ["T"," "," "," ","o"," "," "," "," "," "," ","<"],
    ["‾","‾","‾","‾","‾"," "," ","o"," "," ",")","‾"],
    [" "," "," "," "," ","‾","‾","‾","‾","‾","‾"," "],
]

level = Utilities.map_color_code.color_code(level)

turrets = [{"location":[1,11],
            "firerate":1,
            "tick_num":1,
            "despawn_time":1000,
            "dir":"left",
            "bullets":[] #bullet: {location, time}
            }]

character_location = [1,0] # Y,X, where Y goes from top

def get_level():
    return {
        "level":level,
        "turrets":turrets,
        "character_location":character_location
    }
