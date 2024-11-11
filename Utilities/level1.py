
level = [
    [" "," "," "," "," "," "," "],
    ["T"," "," "," "," ","‾","‾"],
    ["‾","‾","‾","‾","‾"," "," "]
]

level_1 = [
    ["T","_","_","_","_","_","_"],
    ["_","_","_","_","_","_","_"],
    ["_","_","_","_","_","_","_"]
]

i=0
j=0
index=0
output = ""

turret_locations = []
character_location = [1,0] # Y,X, where Y goes from top

def get_level():
    return {
        "level":level,
        "turret_locations":turret_locations,
        "character_location":character_location
    }


while index < len(level):
    item = level[index]
    index += 1 
    for j in range(j, 20):
        item.append("‾")
    #reset the value of J to 0
    j = 0


for row in level:
    output += " ".join(row) + "\n"
print(output)