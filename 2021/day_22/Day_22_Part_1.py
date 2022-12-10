import os
from parse import compile

class Cuboid:
    def __init__(self, x_1, y_1, z_1, x_2, y_2, z_2):
        self.x_1 = x_1
        self.y_1 = y_1
        self.z_1 = z_1
        self.x_2 = x_2
        self.y_2 = y_2
        self.z_2 = z_2

    def __str__(self):
        return str(((self.x_1, self.x_2), (self.y_1, self.y_2), (self.z_1, self.z_2)))

def get_intersection(cuboid_1, cuboid_2):
    if cuboid_2.x_1 in range(cuboid_1.x_1, cuboid_1.x_2 + 1):
        if cuboid_2.y_1 in range(cuboid_1.y_1, cuboid_1.y_2 + 1):
            if cuboid_2.z_1 in range(cuboid_1.z_1, cuboid_1.z_2 + 1):
                # Cuboid 2 pos_1 lies within Cuboid 1
                x_1 = cuboid_2.x_1
                y_1 = cuboid_2.y_1
                z_1 = cuboid_2.z_1
                x_2 = cuboid_1.x_2 if cuboid_1.x_2 < cuboid_2.x_2 else cuboid_2.x_2
                y_2 = cuboid_1.y_2 if cuboid_1.y_2 < cuboid_2.y_2 else cuboid_2.y_2
                z_2 = cuboid_1.z_2 if cuboid_1.z_2 < cuboid_2.z_2 else cuboid_2.z_2
                return Cuboid(x_1, y_1, z_1, x_2, y_2, z_2)
    elif cuboid_1.x_1 in range(cuboid_2.x_1, cuboid_2.x_2 + 1):
        if cuboid_1.y_1 in range(cuboid_2.y_1, cuboid_2.y_2 + 1):
            if cuboid_1.z_1 in range(cuboid_2.z_1, cuboid_2.z_2 + 1):
                # Cuboid 1 pos_1 lies within Cuboid 2
                x_1 = cuboid_1.x_1
                y_1 = cuboid_1.y_1
                z_1 = cuboid_1.z_1
                x_2 = cuboid_1.x_2 if cuboid_1.x_2 < cuboid_2.x_2 else cuboid_2.x_2
                y_2 = cuboid_1.y_2 if cuboid_1.y_2 < cuboid_2.y_2 else cuboid_2.y_2
                z_2 = cuboid_1.z_2 if cuboid_1.z_2 < cuboid_2.z_2 else cuboid_2.z_2
                return Cuboid(x_1, y_1, z_1, x_2, y_2, z_2)
    return None


def get_on_count(grid, target_area=None):
    sum = 0
    for cuboid in grid.cuboids:
        cuboid_in_target = get_intersection(target_area, cuboid)
        if cuboid_in_target:
            for x in range(cuboid_in_target.x_1, cuboid_in_target.x_2 + 1):
                for y in range(cuboid_in_target.y_1, cuboid_in_target.y_2 + 1):
                    for z in range(cuboid_in_target.z_1, cuboid_in_target.z_2 + 1):
                        sum += 1
    return sum

reboot_steps = []

with open(os.getcwd() + "\\2021\\day_22\\day_22-input.txt", 'r') as file:
    instruction_parse = compile("{} x={:d}..{:d},y={:d}..{:d},z={:d}..{:d}")
    line = file.readline()
    while line:
        line = line.strip()
        instruction, x_1, x_2, y_1, y_2, z_1, z_2 = instruction_parse.search(line)
        cuboid = Cuboid(x_1, y_1, z_1, x_2, y_2, z_2)
        reboot_steps.append((instruction, cuboid))
        line = file.readline()

cubes = {}
target_area = Cuboid(-50, -50, -50, 50, 50, 50)

for step in reboot_steps:
    intersection = get_intersection(target_area, step[1])
    if intersection:
        if step[0] == "on":
            for x in range(intersection.x_1, intersection.x_2 + 1):
                for y in range(intersection.y_1, intersection.y_2 + 1):
                    for z in range(intersection.z_1, intersection.z_2 + 1):
                        cubes[(x, y, z)] = True
        else:
            for x in range(intersection.x_1, intersection.x_2 + 1):
                for y in range(intersection.y_1, intersection.y_2 + 1):
                    for z in range(intersection.z_1, intersection.z_2 + 1):
                        if (x, y, z) in cubes:
                            cubes.pop((x, y, z))

print(len(cubes))