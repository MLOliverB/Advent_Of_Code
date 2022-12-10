import os
import numpy as np

def print_matrix(m, verticalSpace):
    max_len = 0
    for row in m:
        for entry in row:
            slen = len(str(entry))
            if slen > max_len:
                max_len = slen
    for row in m:
        for entry in row:
            s = str(entry)
            padding_len = max_len-len(s)
            l_len = int(padding_len/2)
            r_len = padding_len - l_len
            l_padding = " " * l_len
            r_padding = " " * r_len
            print(l_padding + s + r_padding, end=' ')
        print()
    if verticalSpace:
        print()

class Octopus:
    def __init__(self, energy):
        self.energy = energy
        self.flashed = False

    def __str__(self):
        return "O(" + str(self.energy) + ", " + str(self.flashed) + ")"

class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_map = {}
        for i in range(len(vertices)):
            self.adjacency_map[vertices[i]] = edges[i]

input_matrix = []

with open(os.getcwd() + "\\2021\\day_11\\day_11-input.txt", 'r') as file:
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
octopus_matrix = np.zeros((row_size+2, col_size+2), dtype=np.object)
octopus_matrix[0, :] = None
octopus_matrix[-1, :] = None
octopus_matrix[:, 0] = None
octopus_matrix[:, -1] = None
octopus_matrix[0, 0] = None
for i in range(0, row_size):
    for j in range(0, col_size):
        octopus = Octopus(input_matrix[i][j])
        octopus_matrix[i+1, j+1] = octopus

vertices = []
edges = []
for i in range(1, row_size+1):
    for j in range(1, col_size+1):
        vertices.append(octopus_matrix[i][j])

for i in range(1, row_size+1):
    for j in range(1, col_size+1):
        edge = []
        selection = octopus_matrix[i-1:i+2, j-1:j+2]
        if selection[0, 0]:
            edge.append(selection[0, 0])
        if selection[0, 1]:
            edge.append(selection[0, 1])
        if selection[0, 2]:
            edge.append(selection[0, 2])
        if selection[1, 0]:
            edge.append(selection[1, 0])
        if selection[1, 2]:
            edge.append(selection[1, 2])
        if selection[2, 0]:
            edge.append(selection[2, 0])
        if selection[2, 1]:
            edge.append(selection[2, 1])
        if selection[2, 2]:
            edge.append(selection[2, 2])
        edges.append(edge)

octopus_graph = Graph(vertices, edges)

sync_step = -1

#print_matrix(octopus_matrix, True)

step = 1
while True:
    flash_sum = 0
    for octopus in octopus_graph.vertices:
        octopus.flashed = False
    flash_q = []
    q_size = 0
    for octopus in octopus_graph.vertices:
        octopus.energy += 1
        if octopus.energy == 10:
            flash_q.append(octopus)
            q_size += 1
            octopus.flashed = True
    while q_size > 0:
        octopus = flash_q.pop(0)
        q_size -= 1
        for adj in octopus_graph.adjacency_map[octopus]:
            adj.energy += 1
            if adj.energy == 10 and adj.flashed == False:
                flash_q.append(adj)
                q_size += 1
                adj.flashed = True
    for octopus in octopus_graph.vertices:
        if octopus.flashed:
            flash_sum += 1
        if octopus.energy > 9:
            octopus.energy = 0
    #print_matrix(octopus_matrix, True)
    if flash_sum == len(octopus_graph.vertices):
        sync_step = step
        break
    step += 1

print("First step of synchronized flashes {}".format(sync_step))