from colorama import init,Fore,Style

init()

level = [
    [" "," "," "," "," "," "," "," "," "," "," "," "],
    ["T"," "," "," ","o"," "," "," "," "," "," ","<"],
    ["‾","‾","‾","‾","‾"," "," ","o"," "," ",")","‾"],
    [" "," "," "," "," ","‾","‾","‾","‾","‾","‾"," "],
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
