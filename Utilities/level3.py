import Utilities.map_color_code

level = [
    [" "," "," "," "," "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "," "," "," "," "],
    ["o"," "," "," "," "," "," "," "," ","<"," "," "],
    [">"," ","T"," "," ","‾","‾","o","‾","‾","‾"," "],
    ["‾","‾","‾","‾","‾"," "," ","‾"," "," "," ",")"],
]

level = Utilities.map_color_code.color_code(level)

turrets = [{"location":[3,0],
            "firerate":1,
            "tick_num":0,
            "despawn_time":100,
            "dir":"right",
            "bullets":[] #bullet: {location, time}
            },
            {"location":[2,9],
            "firerate":5,
            "tick_num":0,
            "despawn_time":4,
            "dir":"left",
            "bullets":[] #bullet: {location, time}
            }]

character_location = [3,2] # Y,X, where Y goes from top

def get_level():
    return {
        "level":level,
        "turrets":turrets,
        "character_location":character_location
    }
