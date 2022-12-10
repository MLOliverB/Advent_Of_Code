import os
import numpy as np
from parse import compile

def lerp(v0, v1, t):
    return (1-t) * v0 + t * v1

line_sequence = []
max_x = 0
max_y = 0

with open(os.getcwd() + "\\2021\\day_5\\day_5-input.txt", 'r') as file:
    p = compile("{:d},{:d} -> {:d},{:d}")
    line = file.readline()
    while line:
        line = line.strip()
        x_1, y_1, x_2, y_2 = p.search(line)

        max_x = x_1 if x_1 > max_x else max_x
        max_x = x_2 if x_2 > max_x else max_x
        max_y = y_1 if y_1 > max_y else max_y
        max_y = y_2 if y_2 > max_y else max_y

        arr = None
        if x_1 == x_2:
            # vertical Line
            arr = np.zeros((2, max(y_1, y_2) + 1 - min(y_1, y_2)), dtype=np.int)
            arr[0] += x_1
            arr[1] = np.arange(min(y_1, y_2), max(y_1, y_2) + 1)
        elif y_1 == y_2:
            # Horizontal Line
            arr = np.zeros((2, max(x_1, x_2) + 1 - min(x_1, x_2)), dtype=np.int)
            arr[0] = np.arange(min(x_1, x_2), max(x_1, x_2) + 1)
            arr[1] += y_1
        else:
            # Diagonal Line
            line = file.readline()
            continue
            
        line_sequence.append(arr)
        line = file.readline()

# Initialize grid of zeros
grid = np.zeros((max_x+1, max_y+1), dtype=np.int)

for line in line_sequence:
    grid[line[0], line[1]] += 1

overlapping_points = 0

for row in grid:
    #print(row)
    for entry in row:
        if entry >= 2:
            overlapping_points += 1

print("Number of points overlapping (- diagonals):", overlapping_points)