import os

depths = []

with open(os.getcwd() + "\\2021\\day_1\\day_1-input.txt", 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        depths.append(int(line))
        line = file.readline()

inc_counter = 0
for i in range(3, len(depths)):
    window_cur = depths[i] + depths[i-1] + depths[i-2]
    window_prev = depths[i-1] + depths[i-2] + depths[i-3]
    if window_cur > window_prev:
        inc_counter += 1

print("Count of increasing depth (3 wide sliding window):", inc_counter)