from colorama import init,Fore,Style

init()

level = [
    [" "," "," "," "," "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "," "," "," "," "],
    ["o"," "," "," "," "," "," "," "," ","<"," "," "],
    [">"," ","T"," "," ","‾","‾","o","‾","‾","‾"," "],
    ["‾","‾","‾","‾","‾"," "," ","‾"," "," "," ",")"],
]

for l in level:
    for c in l:
        if c=="_":
            l[l.index(c)] = Fore.LIGHTBLACK_EX+"_"+Style.RESET_ALL
        elif c==")":
            l[l.index(c)] = Fore.BLUE+")"+Style.RESET_ALL
        elif c=="o":
            l[l.index(c)] = Fore.YELLOW+"o"+Style.RESET_ALL
        elif c=="‾":
            l[l.index(c)] = Fore.GREEN+"‾"+Style.RESET_ALL
        elif c=="T":
            l[l.index(c)] = Fore.MAGENTA+"T"+Style.RESET_ALL

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
