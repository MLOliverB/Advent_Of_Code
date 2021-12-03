import os

encounters = []
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
rows = []

with open(os.getcwd() + "\\2020\\day_3\\day_3-input.txt", 'r') as file:
    line = file.readline()
    while line:
        rows.append(line.strip())
        line = file.readline()


for slope in slopes:
    x_pos = 0
    y_pos = 0
    tree_count = 0
    while y_pos < len(rows):
        if rows[y_pos][x_pos] == '#':
            tree_count += 1
        
        x_pos = (x_pos + slope[0]) % len(rows[0])
        y_pos = y_pos + slope[1]

    encounters.append(tree_count)
    print(slope, "- Tree encounters:", tree_count)

encounters_product = 1
for encounter in encounters:
    encounters_product = encounters_product * encounter

print("Collisions multiplied", encounters_product)