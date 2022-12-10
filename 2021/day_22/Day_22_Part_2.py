import os
from parse import compile

class Cuboid:
    def __init__(self, x1, x2, y1, y2, z1, z2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2

    def __str__(self):
        return "{" + "({}, {}), ({}, {}), ({}, {})".format(self.x1, self.x2, self.y1, self.y2, self.z1, self.z2) + "}"

    def count(self, target_area=None):
        if target_area == None:
            target_area = Cuboid(self.x1, self.x2, self.y1, self.y2, self.z1, self.z2)
        x1 = target_area.x1 if self.x1 < target_area.x1 else self.x1
        x2 = target_area.x2 if self.x2 > target_area.x2 else self.x2
        y1 = target_area.y1 if self.y1 < target_area.y1 else self.y1
        y2 = target_area.y2 if self.y2 > target_area.y2 else self.y2
        z1 = target_area.z1 if self.z1 < target_area.z1 else self.z1
        z2 = target_area.z2 if self.z2 > target_area.z2 else self.z2
        if x1 > target_area.x2 or x2 < target_area.x1 or y1 > target_area.y2 or y2 < target_area.y1 or z1 > target_area.z2 or z2 < target_area.z1:
            return 0
        else:
            return (x2 + 1 - x1) * (y2 + 1 - y1) * (z2 + 1 - z1)

    def is_intersecting(self, cuboid):
        x_intersect = False
        y_intersect = False
        z_intersect = False
        if cuboid.x1 <= self.x1 and self.x1 <= cuboid.x2:
            x_intersect = True
        if cuboid.x1 <= self.x2 and self.x2 <= cuboid.x2:
            x_intersect = True
        if self.x1 <= cuboid.x1 and cuboid.x1 <= self.x2:
            x_intersect = True
        if self.x1 <= cuboid.x2 and cuboid.x2 <= self.x2:
            x_intersect = True

        if cuboid.y1 <= self.y1 and self.y1 <= cuboid.y2:
            y_intersect = True
        if cuboid.y1 <= self.y2 and self.y2 <= cuboid.y2:
            y_intersect = True
        if self.y1 <= cuboid.y1 and cuboid.y1 <= self.y2:
            y_intersect = True
        if self.y1 <= cuboid.y2 and cuboid.y2 <= self.y2:
            y_intersect = True

        if cuboid.z1 <= self.z1 and self.z1 <= cuboid.z2:
            z_intersect = True
        if cuboid.z1 <= self.z2 and self.z2 <= cuboid.z2:
            z_intersect = True
        if self.z1 <= cuboid.z1 and cuboid.z1 <= self.z2:
            z_intersect = True
        if self.z1 <= cuboid.z2 and cuboid.z2 <= self.z2:
            z_intersect = True
        return (x_intersect and y_intersect and z_intersect)

    def get_intersection(self, cuboid):
        if self.is_intersecting(cuboid):
            # Compute the cuboid that forms the intersection
            x1 = max(self.x1, cuboid.x1)
            x2 = min(self.x2, cuboid.x2)
            y1 = max(self.y1, cuboid.y1)
            y2 = min(self.y2, cuboid.y2)
            z1 = max(self.z1, cuboid.z1)
            z2 = min(self.z2, cuboid.z2)
            return Cuboid(x1, x2, y1, y2, z1, z2)
        else:
            return None


    def subtract(self, cuboid):
        cuboids = []
        if self.is_intersecting(cuboid):
            cuboid = self.get_intersection(cuboid)
            # Make the 6 exclusion regions (Divide the cuboid into 6 cuboids that exclude the cuboid to be subtracted)
            cuboids.append(Cuboid(self.x1, cuboid.x1 - 1, self.y1, self.y2, self.z1, self.z2))
            cuboids.append(Cuboid(cuboid.x2 + 1, self.x2, self.y1, self.y2, self.z1, self.z2))
            cuboids.append(Cuboid(cuboid.x1, cuboid.x2, self.y1, cuboid.y1 - 1, self.z1, self.z2))
            cuboids.append(Cuboid(cuboid.x1, cuboid.x2, cuboid.y2 + 1, self.y2, self.z1, self.z2))
            cuboids.append(Cuboid(cuboid.x1, cuboid.x2, cuboid.y1, cuboid.y2, self.z1, cuboid.z1 - 1))
            cuboids.append(Cuboid(cuboid.x1, cuboid.x2, cuboid.y1, cuboid.y2, cuboid.z2 + 1, self.z2))

            # Pop any illogical regions
            cuboids_len = len(cuboids)
            for i in range(cuboids_len-1, -1, -1):
                c = cuboids[i]
                if c.x1 > c.x2 or c.y1 > c.y2 or c.z1 > c.z2:
                    cuboids.pop(i)
        else:
            cuboids.append(self)
        return cuboids

reboot_steps = []

with open(os.getcwd() + "\\2021\\day_22\\day_22-input.txt", 'r') as file:
    instruction_parse = compile("{} x={:d}..{:d},y={:d}..{:d},z={:d}..{:d}")
    line = file.readline()
    while line:
        line = line.strip()
        instruction, x_1, x_2, y_1, y_2, z_1, z_2 = instruction_parse.search(line)
        cuboid = Cuboid(x_1, x_2, y_1, y_2, z_1, z_2)
        reboot_steps.append((instruction, cuboid))
        line = file.readline()

on_cuboids = []
#target_area = Cuboid(-50, 50, -50, 50, -50, 50)
target_area = None

counter = 0
max_count = len(reboot_steps)
for step in reboot_steps:
    counter += 1
    print("\rReboot step {} / {}".format(counter, max_count), end=' ')
    instruction, step_cuboid = step
    new_cuboids = []
    for cuboid in on_cuboids:
        new_cuboids += cuboid.subtract(step_cuboid)
    if instruction == "on":
        new_cuboids.append(step_cuboid)
    on_cuboids = new_cuboids
print()

if target_area:
    print("Number of 'on' cubes in the target area", str(target_area), "-", sum(c.count(target_area) for c in on_cuboids))
else:
    print("Number of total 'on' cubes -", sum(c.count(target_area) for c in on_cuboids))