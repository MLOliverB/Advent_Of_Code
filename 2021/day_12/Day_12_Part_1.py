import os
import numpy as np

class Cave:
    def __init__(self, label, is_large):
        self.label = label
        self.is_large = is_large

    def __str__(self):
        if self.is_large:
            return "cave_(" + self.label + ", large)"
        else:
            return "cave_(" + self.label + ", small)"

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_map = {}
        for vertex in self.vertices:
            self.adjacency_map[vertex] = []

    def add_edge(self, edge):
        a, b = edge
        self.adjacency_map[a].append(b)
        self.adjacency_map[b].append(a)

input_edges = []
input_vertices = []
label_map = {}

with open(os.getcwd() + "\\2021\\day_12\\day_12-input.txt", 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        v1, v2 = line.split("-")
        if v1 not in input_vertices:
            input_vertices.append(v1)
        if v2 not in input_vertices:
            input_vertices.append(v2)
        input_edges.append((v1, v2))
        line = file.readline()

vertices = []
edges = []

for v in input_vertices:
    lower_label = v.lower()
    c = None
    if lower_label == v:
        c = Cave(v, False)
    else:
        c = Cave(v, True)
    label_map[v] = c
    vertices.append(c)

for e in input_edges:
    edge = (label_map[e[0]], label_map[e[1]])
    edges.append(edge)

cave_graph = Graph(vertices)

for edge in edges:
    cave_graph.add_edge(edge)

start = None
end = None

for v in cave_graph.vertices:
    if v.label == "start":
        start = v
    elif v.label == "end":
        end = v

paths = [[start, ], ]

def copy(path):
    return [p for p in path]

while True:
    do_continue = False
    path_len = len(paths)
    for ip in range(0, path_len, 1):
        path = paths[ip]
        last_cave = path[-1]
        if last_cave == end:
            # This path has already reached it's end
            continue
        connected_caves = cave_graph.adjacency_map[last_cave]
        cc_len = len(connected_caves)
        include_ix = list(range(cc_len))
        for i in range(cc_len-1, -1, -1):
            if connected_caves[i] == start:
                # We don't want to go back to the start
                include_ix.pop(i)
            elif not connected_caves[i].is_large:
                # If it is a small cave
                if connected_caves[i] in path:
                    # If we have already visited the small cave
                    include_ix.pop(i)
        if len(include_ix) > 0:
            # We will add at least one new path - Continue exploring
            do_continue = True
        else:
            continue
        for ic in range(1, len(include_ix)):
            path_copy = copy(path)
            path_copy.append(connected_caves[include_ix[ic]])
            paths.append(path_copy)
        path.append(connected_caves[include_ix[0]])
    if not do_continue:
        break

for i in range(len(paths)-1, -1, -1):
    if paths[i][-1] != end:
        paths.pop(i)

paths.sort(key=lambda x: str(x))
path_count = len(paths)
print("Total number of possible paths {}".format(path_count))