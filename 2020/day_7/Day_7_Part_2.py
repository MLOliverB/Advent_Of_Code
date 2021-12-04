import os

def count_recursive(rules, colour):
    count = 0
    for inner in rules[colour]:
        count += count_recursive(rules, inner[0]) * inner[1]
        count += inner[1]
    return count

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

print("Number of bag to buy:", count_recursive(rules, bag_colour))