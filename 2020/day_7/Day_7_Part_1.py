import os

bag_colour = "shiny gold"
outer_bag_options = []
# Mapping colour names to list of tuples [("colour name", count), ...]
rules = {}

with open(os.getcwd() + "\\2020\\day_7\\day_7-input.txt", 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        outer, inner = line.split(" bags contain ")
        inner = inner[:-1] # Remove '.' at EOL
        inner = inner.replace(" bags", "")
        inner = inner.replace(" bag", "")
        inner = inner.split(", ")
        rules[outer] = []
        for bag in inner:
            if bag != "no other":
                count_str = bag.split(" ")[0]
                count = int(count_str)
                colour_str = bag[len(count_str)+1: ]
                rules[outer].append((colour_str, count))
        line = file.readline()

prev_iteration_size = 0

for bag in rules:
    for inner in rules[bag]:
        if inner[0] == bag_colour:
            outer_bag_options.append(bag)
            break

while len(outer_bag_options) > prev_iteration_size:
    prev_iteration_size = len(outer_bag_options)
    for bag in rules:
        if bag not in outer_bag_options:
            for inner in rules[bag]:
                if inner[0] in outer_bag_options:
                    outer_bag_options.append(bag)
                    break

print("Outer bag options:", len(outer_bag_options))