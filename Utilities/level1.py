from colorama import init,Fore,Style

init()

level = [
    [" "," "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," ","_"],
    ["T"," "," "," "," ","<",")"," ","o"],
    ["‾","‾","‾","‾","‾","‾","‾","‾","‾"]
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
