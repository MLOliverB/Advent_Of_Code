import os

input_polymer = ""
polymer_map = {}

with open(os.getcwd() + "\\2021\\day_14\\day_14-input.txt", 'r') as file:
    phase = 0
    line = file.readline()
    while line:
        line = line.strip()
        if line == "":
            phase += 1
            line = file.readline()
            continue
        if phase == 0:
            # Read in the input polymer string
            input_polymer = line
        else:
            # Populate the polymer map
            inp, out = line.split(" -> ")
            polymer_map[inp] = out
        line = file.readline()

steps = 10
polymer_string = input_polymer
step = 0
while step < steps:
    print("{} / {}".format(step, steps))
    new_components = []
    for pos in range(len(polymer_string)-1):
        # Look at pairs in the string
        pair = polymer_string[pos: pos+2]
        new_components.append(polymer_map[pair])
    # Insert the new components into the string
    new_string = polymer_string[0]
    for i in range(len(polymer_string)-1):
        new_string += new_components[i]
        new_string += polymer_string[i+1]
    polymer_string = new_string
    step += 1
print("{} / {}".format(step, steps))

character_map = {}
for c in polymer_string:
    if c not in character_map:
        character_map[c] = 1
    else:
        character_map[c] += 1

most_common = ""
max = 0
least_common = ""
min = len(polymer_string)
for c in character_map:
    if character_map[c] > max:
        most_common = c
        max = character_map[c]
    if character_map[c] < min:
        least_common = c
        min = character_map[c]

print("Most common: {} ({}), least common: {} ({}), difference: {}".format(most_common, max, least_common, min, max-min))