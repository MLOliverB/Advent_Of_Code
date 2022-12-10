import os

depths = []

with open(os.getcwd() + "\\2021\\day_1\\day_1-input.txt", 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        depths.append(int(line))
        line = file.readline()

inc_counter = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]:
        inc_counter += 1

print("Count of increasing depth:", inc_counter)