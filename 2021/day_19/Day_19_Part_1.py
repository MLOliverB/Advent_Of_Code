import os
from parse import compile
import numpy as np


class Scanner:
    def __init__(self, label, beacon_positions, beacon_vectors, beacon_distances):
        self.label = label
        self.beacon_positions = beacon_positions
        self.beacon_vectors = beacon_vectors
        self.beacon_distances = beacon_distances
        self.match_scanner = None
        self.has_absolute = False
        self.absolute_zero = None
        self.absolute_beacon_positions = None


def get_rotations(pos_3d_list):
    x_list = [coord[0] for coord in pos_3d_list]
    y_list = [coord[1] for coord in pos_3d_list]
    z_list = [coord[2] for coord in pos_3d_list]
    rotations = []
    for i in range(24):
        rotations.append([])
    for ix in range(len(x_list)):
        x = x_list[ix]
        y = y_list[ix]
        z = z_list[ix]
        # x facing forward
        rotations[0].append(np.array((x, y, z), dtype=np.int))
        rotations[1].append(np.array((x, -z, y), dtype=np.int))
        rotations[2].append(np.array((x, -y, -z), dtype=np.int))
        rotations[3].append(np.array((x, z, -y), dtype=np.int))
        # x facing backward
        rotations[4].append(np.array((-x, -y, z), dtype=np.int))
        rotations[5].append(np.array((-x, -z, -y), dtype=np.int))
        rotations[6].append(np.array((-x, y, -z), dtype=np.int))
        rotations[7].append(np.array((-x, z, y), dtype=np.int))
        # y facing forward
        rotations[8].append(np.array((y, -x, z), dtype=np.int))
        rotations[9].append(np.array((y, -z, -x), dtype=np.int))
        rotations[10].append(np.array((y, x, -z), dtype=np.int))
        rotations[11].append(np.array((y, z, x), dtype=np.int))
        # y facing backward
        rotations[12].append(np.array((-y, x, z), dtype=np.int))
        rotations[13].append(np.array((-y, -z, x), dtype=np.int))
        rotations[14].append(np.array((-y, -x, -z), dtype=np.int))
        rotations[15].append(np.array((-y, z, -x), dtype=np.int))
        # z facing forward
        rotations[16].append(np.array((z, x, y), dtype=np.int))
        rotations[17].append(np.array((z, -y, x), dtype=np.int))
        rotations[18].append(np.array((z, -x, -y), dtype=np.int))
        rotations[19].append(np.array((z, y, -x), dtype=np.int))
        # z facing backward
        rotations[20].append(np.array((-z, -x, y), dtype=np.int))
        rotations[21].append(np.array((-z, -y, -x), dtype=np.int))
        rotations[22].append(np.array((-z, x, -y), dtype=np.int))
        rotations[23].append(np.array((-z, y, x), dtype=np.int))
    return rotations


def set_absolute(absolute_scanner, relative_scanner):
    print("Trying to align {} and {}".format(absolute_scanner.label.ljust(10), relative_scanner.label.ljust(10)), end=' ')
    # Check if it's feasible for these two to align with the given rotation
    same_distance_counter = 0
    i_step = 0
    j_step = 0
    while (i_step < absolute_scanner.beacon_distances.shape[0]-1) or (j_step < relative_scanner.beacon_distances.shape[0]-1):
        if absolute_scanner.beacon_distances[i_step] == relative_scanner.beacon_distances[j_step]:
            same_distance_counter += 1
            i_step += 1
            j_step += 1
        elif absolute_scanner.beacon_distances[i_step] < relative_scanner.beacon_distances[j_step]:
            if i_step < absolute_scanner.beacon_distances.shape[0] - 1:
                i_step += 1
            else:
                j_step += 1
        elif absolute_scanner.beacon_distances[i_step] > relative_scanner.beacon_distances[j_step]:
            if j_step < relative_scanner.beacon_distances.shape[0] - 1:
                j_step += 1
            else:
                i_step += 1
    if same_distance_counter < 11:
        print("- not feasible")
        return False

    abs_beacons = absolute_scanner.absolute_beacon_positions
    total_abs_beacons = len(abs_beacons)
    rel_rotations = get_rotations(relative_scanner.beacon_positions)
    counter = 0
    total_count = len(rel_rotations) * len(abs_beacons) * len(rel_rotations[0])
    for rotation in rel_rotations:
        # Try out every possible alignment of beacons for the given rotation
        np_rotation = np.array(rotation)
        for ix_0 in range(len(abs_beacons)):
            for ix_1 in range(np_rotation.shape[0]):
                counter += 1
                print("\rTrying to align {} and {} - Checking alignment {} / {}".format(absolute_scanner.label.ljust(10), relative_scanner.label.ljust(10), counter, total_count), end=' ')
                matches = 0
                non_matches = 0
                offset = abs_beacons[ix_0] - np_rotation[ix_1]
                abs = None
                rel = None
                for abs_beacon in abs_beacons:
                    eqs = (abs_beacon == np_rotation + offset)
                    if np.any((eqs[:, 0]) & (eqs[:, 1]) & (eqs[:, 2])):
                        matches += 1
                    else:
                        non_matches += 1
                if total_abs_beacons - non_matches < 12:
                    continue
                if matches >= 12:
                    #print(len(abs_beacons), matches, non_matches)
                    relative_scanner.has_absolute = True
                    relative_scanner.beacon_positions = rotation
                    relative_scanner.absolute_zero = offset
                    relative_scanner.absolute_beacon_positions = [coord + relative_scanner.absolute_zero for coord in relative_scanner.beacon_positions]
                    print("\rTrying to align {} and {} - Checking alignment {} / {} - Success".format(absolute_scanner.label.ljust(10), relative_scanner.label.ljust(10), counter, total_count))
                    return True
    print("\rTrying to align {} and {} - Checking alignment {} / {} - Failure".format(absolute_scanner.label.ljust(10), relative_scanner.label.ljust(10), counter, total_count))
    return False

scanners = []

with open(os.getcwd() + "\\2021\\day_19\\day_19-input.txt", 'r') as file:
    scanner_label_parse = compile("--- {} ---")
    line = file.readline()
    while line:
        line = line.strip()
        scanner_label = scanner_label_parse.search(line)[:]
        if scanner_label:
            line = file.readline()
            line = line.strip()
            scanner_label = scanner_label[0]
            beacon_positions_list = []
            beacon_vectors_list = []
            beacon_distances_list = []
            while line != "":
                beacon_positions_list.append(np.array([int(num) for num in line.split(",")], dtype=np.int))
                line = file.readline()
                line = line.strip()
            beacon_positions = np.array(beacon_positions_list)
            for i in range(beacon_positions.shape[0]):
                for j in range(beacon_positions.shape[0]):
                    if i != j:
                        beacon_vectors_list.append(beacon_positions[j] - beacon_positions[i])
                        beacon_distances_list.append(np.linalg.norm(beacon_positions[j] - beacon_positions[i], ord=2))
            beacon_distances_list.sort()
            beacon_vectors = np.array(beacon_vectors_list)
            beacon_vectors = np.sort(beacon_vectors, axis=0)
            beacon_distances = np.array(beacon_distances_list)
            scanners.append(Scanner(scanner_label, beacon_positions, beacon_vectors, beacon_distances))
            scanners[0].has_absolute = True
            scanners[0].absolute_zero = np.array((0, 0, 0), dtype=np.int)
            scanners[0].absolute_beacon_positions = scanners[0].beacon_positions
        line = file.readline()

counter = 1
max_count = len(scanners)
abs_ix = 0
to_check = [scanners[0], ]
while len(to_check) > 0:
    absolute_scanner = to_check.pop(0)
    for relative_scanner in scanners:
        if not relative_scanner.has_absolute:
            if set_absolute(absolute_scanner, relative_scanner):
                counter += 1
                to_check.append(relative_scanner)
                    
print("\nAligned {} / {} scanners".format(counter, max_count))

print("\nScanner positions")
for scanner in scanners:
    print("{} - {}".format(scanner.label.ljust(10), scanner.absolute_zero))

print()
beacons = np.array(scanners[0].absolute_beacon_positions)
for i in range(1, len(scanners)):
    beacons = np.concatenate((beacons, np.array(scanners[i].absolute_beacon_positions)))
beacons = np.unique(beacons, axis=0)

print("In total, there are {} beacons".format(beacons.shape[0]))