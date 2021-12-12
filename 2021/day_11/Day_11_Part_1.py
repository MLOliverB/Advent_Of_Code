import os
import numpy as np

input_matrix = []
steps = 2

with open(os.getcwd() + "\\2021\\day_11\\day_11-testinput.txt", 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        row = []
        for c in line:
            row.append(int(c))
        input_matrix.append(row)
        line = file.readline()

row_size = len(input_matrix)
col_size = len(input_matrix[0])
octopus_matrix = np.zeros((row_size+2, col_size+2), dtype=np.short)
octopus_flashes = np.zeros((row_size+2, col_size+2), dtype=bool)

for i in range(0, row_size):
    for j in range(0, col_size):
        octopus_matrix[i+1, j+1] = input_matrix[i][j]

step = 0
while step < steps:
    # Reset all flashes
    octopus_flashes[:, :] = False
    # Increment all energy by 1
    octopus_matrix += 1
    # Set all padding to zero again
    octopus_matrix[0, :] = 0
    octopus_matrix[-1, :] = 0
    octopus_matrix[:, 0] = 0
    octopus_matrix[:, -1] = 0

    # Find all octopi with energy > 9 which haven't flashed
    #print((octopus_matrix > 9) & (~octopus_flashes))
    print(octopus_matrix[(octopus_matrix > 9) & (~octopus_flashes)])
    step += 1
    print()




# for row in input_matrix:
#     octopus_row = []
#     for entry in row:
#         octopus_row.append(Octopus(entry))
#     octopus_matrix.append(octopus_row)

# for i in range(row_size):
#     for j in range(col_size):
#         #print(row_size, col_size, i, j)
#         octopus = octopus_matrix[i][j]
#         adjacent_list = []
#         if i > 0 and j > 0:
#             adjacent_list.append(octopus_matrix[i-1][j-1])
#         if i > 0:
#             adjacent_list.append(octopus_matrix[i-1][j])
#         if i > 0 and j < col_size-1:
#             adjacent_list.append(octopus_matrix[i-1][j+1])
#         if j > 0:
#             adjacent_list.append(octopus_matrix[i][j-1])
#         if j < col_size-1:
#             adjacent_list.append(octopus_matrix[i][j+1])
#         if i < row_size-1 and j > 0:
#             adjacent_list.append(octopus_matrix[i+1][j-1])
#         if i < row_size-1:
#             adjacent_list.append(octopus_matrix[i+1][j])
#         if i < row_size-1 and j < col_size-1:
#             adjacent_list.append(octopus_matrix[i+1][j+1])
#         octopus.set_adjacent_list(adjacent_list)

# flash_sum = 0

# for row in octopus_matrix:
#     for octopus in row:
#         print(octopus.energy, end=' ')
#     print()
# print()

# for step in range(steps):
#     for row in octopus_matrix:
#         for ocotpus in row:
#             octopus.energy += 1
#     for row in octopus_matrix:
#         for ocotpus in row:
#             if octopus.energy > 9:
#                 octopus.step_flash()
#     for row in octopus_matrix:
#         for octopus in row:
#             if octopus.flashed:
#                 flash_sum += 1
#     for row in octopus_matrix:
#         for octopus in row:
#             octopus.reset_step()
#     for row in octopus_matrix:
#         for octopus in row:
#             print(octopus.energy, end=' ')
#         print()
#     print()

#print(flash_sum)

#print("Total Syntax Error Score: {}".format(syntax_error_score))