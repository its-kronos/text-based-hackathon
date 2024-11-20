from colorama import init, Fore, Back,Style

init()

def color_code(level):
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
    return level