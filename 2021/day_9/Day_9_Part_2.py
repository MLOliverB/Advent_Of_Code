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

def get_basin_size(heightmap, loc):
    row_size, col_size = heightmap.shape
    old_size = 0
    locations = [loc, ]
    locations_len = 1
    while locations_len > old_size:
        old_size = locations_len
        for location in locations:
            if location[0] > 0:
                # We can check left
                if heightmap[location[0]-1, location[1]] < 9:
                    new_loc = (location[0]-1, location[1])
                    if new_loc not in locations:
                        locations.append(new_loc)
                        locations_len += 1
            if location[0] < row_size-1:
                # We can check right:
                if heightmap[location[0]+1, location[1]] < 9:
                    new_loc = (location[0]+1, location[1])
                    if new_loc not in locations:
                        locations.append(new_loc)
                        locations_len += 1
            if location[1] > 0:
                # We can check top
                if heightmap[location[0], location[1]-1] < 9:
                    new_loc = (location[0], location[1]-1)
                    if new_loc not in locations:
                        locations.append(new_loc)
                        locations_len += 1
            if location[1] < col_size-1:
                # We can check bottom
                if heightmap[location[0], location[1]+1] < 9:
                    new_loc = (location[0], location[1]+1)
                    if new_loc not in locations:
                        locations.append(new_loc)
                        locations_len += 1
    return locations_len


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

basin_sizes = []
for min in local_mins:
    basin_sizes.append(get_basin_size(heightmap, min))

basin_sizes.sort()
l1 = basin_sizes[-3]
l2 = basin_sizes[-2]
l3 = basin_sizes[-1]
print("3 largest basins: {} * {} * {} = {}".format(l1, l2, l3, l1*l2*l3))