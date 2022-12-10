import os
import numpy as np

def print_image(matrix, end='\n'):
    for row in matrix:
        for entry in row:
            print('#' if entry else '.', end='')
        print()
    print(end, end='')

input_enhancer = []
input_matrix = []

with open(os.getcwd() + "\\2021\\day_20\\day_20-input.txt", 'r') as file:
    phase = 0
    line = file.readline()
    while line:
        line = line.strip()
        if line == "":
            phase += 1
            line = file.readline()
            continue
        if phase == 0:
            for c in line:
                input_enhancer.append(c)
        else:
            row = []
            for c in line:
                row.append(c)
            input_matrix.append(row)
        line = file.readline()

enhancement_vector = np.zeros((len(input_enhancer), ), dtype=bool)
image_matrix = np.zeros((len(input_matrix)+10, len(input_matrix[0])+10), dtype=bool)

for i in range(len(input_enhancer)):
    enhancement_vector[i] = True if input_enhancer[i] == '#' else False

for i in range(len(input_matrix)):
    for j in range(len(input_matrix[0])):
        image_matrix[i+5, j+5] = True if input_matrix[i][j] == '#' else False

#print_image(image_matrix)
steps = 2
for step in range(steps):
    new_image = np.zeros((image_matrix.shape[0]+2, image_matrix.shape[1]+2), dtype=bool)
    for i in range(1, image_matrix.shape[0]-1):
        for j in range(1, image_matrix.shape[1]-1):
            vector = image_matrix[i-1: i+2, j-1: j+2].flatten()
            bin_str = ""
            for entry in vector:
                if entry:
                    bin_str += '1'
                else:
                    bin_str += '0'
            new_image[i+1, j+1] = enhancement_vector[int(bin_str, 2)]
    if image_matrix[0, 0]:
        # Background is '#', i.e. last element in enhacement vector
        for i in [0, 1, -2, -1]:
            new_image[i, :] = enhancement_vector[-1]
            new_image[:, i] = enhancement_vector[-1]
    else:
        # Background is '.', i.e. first element in enhacement vector
        for i in [0, 1, -2, -1]:
            new_image[i, :] = enhancement_vector[0]
            new_image[:, i] = enhancement_vector[0]
    image_matrix = new_image
    #print_image(image_matrix)
    

print("There are {} lit pixels".format(np.sum(image_matrix)))