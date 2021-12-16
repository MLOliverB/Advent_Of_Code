import os
import sys
import numpy as np

def print_matrix(m, end=""):
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
    print("", end=end)

class Vertex:
    def __init__(self, weight, x, y):
        self.weight = weight
        self.x = x
        self.y = y
        self.distance = np.inf
        self.known = False

    def __str__(self):
        return "V({})[{},{}]".format(self.weight, self.x, self.y)

    def __lt__(self, other):
        return self.distance < other.distance

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_map = {}

    def set_edges(self, vertex, edges):
        self.adjacency_map[vertex] = edges

    def get_edges(self, vertex):
        return self.adjacency_map[vertex]
 



input_matrix = []

with open(os.getcwd() + "\\2021\\day_15\\day_15-input.txt", 'r') as file:
    phase = 0
    line = file.readline()
    while line:
        line = line.strip()
        row = [int(c) for c in line]
        input_matrix.append(row)
        line = file.readline()

vertex_matrix = np.full((len(input_matrix), len(input_matrix[0])), None, dtype=object)
# Initialize the vertices
for i in range(vertex_matrix.shape[0]):
    for j in range(vertex_matrix.shape[1]):
        v = Vertex(input_matrix[i][j], i, j)
        vertex_matrix[i, j] = v

cave_graph = Graph(list(vertex_matrix.flatten()))

# Initialize the edges
for i in range(vertex_matrix.shape[0]):
    for j in range(vertex_matrix.shape[1]):
        edges = []
        if i > 0:
            edges.append(vertex_matrix[i-1, j])
        if i < vertex_matrix.shape[0]-1:
            edges.append(vertex_matrix[i+1, j])
        if j > 0:
            edges.append(vertex_matrix[i, j-1])
        if j < vertex_matrix.shape[1]-1:
            edges.append(vertex_matrix[i, j+1])
        cave_graph.set_edges(vertex_matrix[i, j], edges)

start = vertex_matrix[0, 0]
start.distance = 0
start.known = True
for v in cave_graph.get_edges(start):
    v.distance = v.weight
end = vertex_matrix[-1, -1]

total_vertices = len(cave_graph.vertices)
set_size = 1
unknown_set = []
for v in cave_graph.vertices:
    if v != start:
        unknown_set.append(v)

# for v in unknown_set:
#     print(str(v), end= ' ')

while set_size < total_vertices:
    print("\r{} / {}".format(set_size, total_vertices), end=' ')
    # Find v not in known_set with distance(v) minimum
    unknown_set.sort()
    min = unknown_set.pop(0)
    # Add v to known_set
    min.known = True
    set_size += 1
    # Edge relaxation
    for v in cave_graph.get_edges(min):
        if not v.known:
            if (min.distance + v.weight) < v.distance:
                v.distance = min.distance + v.weight

print()
print("Total lowest risk from start to end: {}".format(end.distance))