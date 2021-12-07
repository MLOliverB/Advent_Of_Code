import os
import numpy as np

crab_input = []
max_pos = 0


with open(os.getcwd() + "\\2021\\day_7\\day_7-input.txt", 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        init_crab = line.split(",")
        for init in init_crab:
            init = int(init)
            if init > max_pos:
                max_pos = init
            crab_input.append(init)
        line = file.readline()

crab_pos = np.array(crab_input, dtype=np.int)
#for init in crab_input:
#    crab_pos[init] += 1

crab_fuel_cost = np.zeros(max_pos+1, dtype=np.int)

for pos in range(crab_fuel_cost.shape[0]):
    crab_fuel_cost[pos] = np.sum(np.absolute(pos - crab_pos))

print("Minimum fuel cost {} at position: {}".format(np.amin(crab_fuel_cost), np.argmin(crab_fuel_cost)))