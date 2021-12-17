import os
from parse import compile
import numpy as np

target_box = ()

with open(os.getcwd() + "\\2021\\day_17\\day_17-input.txt", 'r') as file:
    parser = compile("target area: x={:d}..{:d}, y={:d}..{:d}")
    line = file.readline()
    while line:
        line = line.strip()
        x1, x2, y1, y2 = parser.search(line)
        target_box = ((x1, x2), (y1, y2))
        line = file.readline()

def simulate(init_vels):
    x_vel, y_vel = init_vels
    x = 0
    y = 0
    steps = [(x, y), ]
    max_y = 0
    while True:
        x += x_vel
        y += y_vel
        if y > max_y:
            max_y = y
        if x_vel > 0:
            x_vel -= 1
        elif x_vel < 0:
            x_vel += 1
        y_vel -= 1
        if x > max(target_box[0]) or y < min(target_box[1]):
            break
        else:
            steps.append((x, y))
    last_x, last_y = steps[-1]
    if target_box[0][0] <= last_x and last_x <= target_box[0][1] and target_box[1][0] <= last_y and last_y <= target_box[1][1]:
        return (True, max_y, 0)
    else:
        if last_x > target_box[0][1]:
            return (False, max_y, 1)
        else:
            return (False, max_y, -1)


# Optimisation algorithm
opt_vels = None
opt_y = None
count = 1
count_max = target_box[0][0] * 10*target_box[0][0]
for i in range(1, target_box[0][0]):
    for j in range(1, 10*target_box[0][0]):
        print("\r{} / {}".format(count, count_max), end=' ')
        success, y_max, bias = simulate((i, j))
        if success:
            if opt_vels:
                if y_max > opt_y:
                    opt_vels = (i, j)
                    opt_y = y_max
            else:
                opt_vels = (i, j)
                opt_y = y_max
        count += 1
print()

print(opt_vels, opt_y)