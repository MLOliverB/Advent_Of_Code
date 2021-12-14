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

steps = 40

letter_counts = {}
for l in input_polymer:
    letter_counts[l] = 1 if l not in letter_counts else letter_counts[l] + 1

pair_counts = {}
for i in range(len(input_polymer)-1):
    pair = input_polymer[i:i+2]
    pair_counts[pair] = 1 if pair not in pair_counts else pair_counts[pair] + 1

step = 0
while step < steps:
    p = list(pair_counts.keys())
    pc = []
    for s in p:
        pc.append(pair_counts[s])
    for i in range(len(p)):
        pair = p[i]
        count = pc[i]
        c = polymer_map[pair]
        np1 = pair[0] + c
        np2 = c + pair[1]
        pair_counts[np1] = count if np1 not in pair_counts else pair_counts[np1] + count
        pair_counts[np2] = count if np2 not in pair_counts else pair_counts[np2] + count
        pair_counts[pair] -= count
        letter_counts[c] = count if c not in letter_counts else letter_counts[c] + count
    step += 1

length = 0
for c in letter_counts:
    length += letter_counts[c]

most_common = ""
max = 0
least_common = ""
min = length
for c in letter_counts:
    if letter_counts[c] > max:
        most_common = c
        max = letter_counts[c]
    if letter_counts[c] < min:
        least_common = c
        min = letter_counts[c]

print("Most common: {} ({}), least common: {} ({}), difference: {}".format(most_common, max, least_common, min, max-min))



# final_length = len(input_polymer)
# for i in range(steps):
#     final_length = final_length + (final_length-1)

# def add_char_count(c):
#     global map_size
#     map_size += 1
#     if c not in character_map:
#         character_map[c] = 1
#     else:
#         character_map[c] += 1

# def polymer_creation(c1, c2, steps):
#     if steps > 0:
#         print("\r" + str(character_map) + " {} / {} ({}%)".format(map_size, final_length, (map_size/final_length)*100), end='')
#         c = polymer_map[c1+c2]
#         add_char_count(c)
#         polymer_creation(c1, c, steps-1)
#         polymer_creation(c, c2, steps-1)


# for c in input_polymer:
#     add_char_count(c)
# for i in range(len(input_polymer)-1):
#     polymer_creation(input_polymer[i], input_polymer[i+1], steps)
# print()

# print(character_map)

# sum = 0
# for c in character_map:
#     sum += character_map[c]
# print("Polymer length: {}".format(sum))

# most_common = ""
# max = 0
# least_common = ""
# min = sum
# for c in character_map:
#     if character_map[c] > max:
#         most_common = c
#         max = character_map[c]
#     if character_map[c] < min:
#         least_common = c
#         min = character_map[c]

# print("Most common: {} ({}), least common: {} ({}), difference: {}".format(most_common, max, least_common, min, max-min))


# strlen = len(input_polymer)
# inplen = strlen
# for i in range(steps):
#     strlen = strlen + (strlen-1)

# #polymer = np.array([c for c in "-"*strlen])
# polymer = np.full((strlen,), ['-'], dtype=str)
# for i in range(0, polymer.shape[0], int((polymer.shape[0]-1)/(inplen-1))):
#     polymer[i] = input_polymer[0]
#     input_polymer = input_polymer[1:]

# step = 0
# skip = int((polymer.shape[0]-1)/(inplen-1))
# chars = inplen
# while step < steps:
#     print("{} / {}".format(step, steps))
#     for i in range(chars-1):
#         #print("{} + {} => {}".format(polymer[i*skip], polymer[(i+1)*skip], polymer_map[polymer[i*skip] + polymer[(i+1)*skip]]))
#         polymer[int(i*skip+(skip/2))] = polymer_map[polymer[i*skip] + polymer[(i+1)*skip]]
#     step += 1
#     skip = int(skip/2)
#     chars = chars + chars-1
# print("{} / {}".format(step, steps))
#print(polymer)

# polymer_string = input_polymer
# step = 0
# while step < steps:
#     print("{} / {}".format(step, steps))
#     new_components = []
#     for pos in range(len(polymer_string)-1):
#         # Look at pairs in the string
#         pair = polymer_string[pos: pos+2]
#         new_components.append(polymer_map[pair])
#     # Insert the new components into the string
#     new_string = polymer_string[0]
#     for i in range(len(polymer_string)-1):
#         new_string += new_components[i]
#         new_string += polymer_string[i+1]
#     polymer_string = new_string
#     step += 1
# print("{} / {}".format(step, steps))

# character_map = {}
# for c in polymer_string:
#     if c not in character_map:
#         character_map[c] = 1
#     else:
#         character_map[c] += 1

# most_common = ""
# max = 0
# least_common = ""
# min = len(polymer_string)
# for c in character_map:
#     if character_map[c] > max:
#         most_common = c
#         max = character_map[c]
#     if character_map[c] < min:
#         least_common = c
#         min = character_map[c]

# print("Most common: {} ({}), least common: {} ({}), difference: {}".format(most_common, max, least_common, min, max-min))