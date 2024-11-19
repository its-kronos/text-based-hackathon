from colorama import init,Fore,Style

init()

level = [
    [" "," "," "," "," "," "," "," "," "," "],
    [" "," "," ","o"," "," ","o"," "," "," "],
    ["_","_"," "," "," "," "," "," "," "," "],
    ["T"," "," ","o","‾","‾","‾"," "," ",")"],
    ["‾","‾","‾","‾"," "," "," ","‾","‾","‾"]
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

turrets = []

character_location = [3,0] # Y,X, where Y goes from top

def get_level():
    return {
        "level":level,
        "turrets":turrets,
        "character_location":character_location
    }
