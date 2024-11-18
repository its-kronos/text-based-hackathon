level = [
    [" "," "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," ","_"],
    ["T"," "," "," "," ","<",")"," ","o"],
    ["‾","‾","‾","‾","‾","‾","‾","‾","‾"]
]

turrets = [{"location":[2,5],
            "firerate":3,
            "tick_num":3,
            "despawn_time":5,
            "dir":"left",
            "bullets":[] #bullet: {location, time}
            }]

character_location = [2,0] # Y,X, where Y goes from top

l = [1,1,1,2,3,4,5,5,5]

l.remove(1)

print(l)

def get_level():
    return {
        "level":level,
        "turrets":turrets,
        "character_location":character_location
    }
