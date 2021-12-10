import os
import numpy as np

heightmap_input = []

def is_minimum(heightmap, row, col):
    row_size, col_size = heightmap.shape
    loss = heightmap[row, col]
    min_loss = 10
    if row > 0:
        # We can check left
        if heightmap[row-1, col] < min_loss:
            min_loss = heightmap[row-1, col]
    if row < row_size-1:
        # We can check right:
        if heightmap[row+1, col] < min_loss:
            min_loss = heightmap[row+1, col]
    if col > 0:
        # We can check top
        if heightmap[row, col-1] < min_loss:
            min_loss = heightmap[row, col-1]
    if col < col_size-1:
        # We can check bottom
        if heightmap[row, col+1] < min_loss:
            min_loss = heightmap[row, col+1]
    if loss < min_loss:
        return True
    else:
        return False


with open(os.getcwd() + "\\2021\\day_9\\day_9-input.txt", 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        row = []
        for digit in line:
            row.append(int(digit))
        heightmap_input.append(row)
        line = file.readline()

heightmap = np.array(heightmap_input, dtype=np.short)

local_mins = []
for row in range(heightmap.shape[0]):
    for col in range(heightmap.shape[1]):
        is_min = is_minimum(heightmap, row, col)
        if is_min:
            local_mins.append((row, col))

min_values = np.zeros((len(local_mins, )), dtype=np.short)
for i in range(len(local_mins)):
    min_values[i] = heightmap[local_mins[i][0], local_mins[i][1]]

risk_levels = min_values + 1

risk_levels_sum = np.sum(risk_levels)

print("Sum of lava tubes risk levels: {}".format(risk_levels_sum))