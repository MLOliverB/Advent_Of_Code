import os
from parse import compile
import numpy as np


# X -> Columns
# Y -> Rows
max_x = 0
max_y = 0
input_dots = []
folds = []

with open(os.getcwd() + "\\2021\\day_13\\day_13-input.txt", 'r') as file:
    phase = 0
    fold_p = compile("fold along {}={:d}")
    line = file.readline()
    while line:
        line = line.strip()
        if line == "":
            phase += 1
            line = file.readline()
            continue
        if phase == 0:
            # Read in the dots
            x, y = line.split(",")
            x = int(x)
            y = int(y)
            input_dots.append((x, y))
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
        else:
            # Read in the folds
            axis, pos = fold_p.search(line)
            folds.append((axis, pos))
        line = file.readline()

sheet_size = (max_y+1, max_x+1)
sheet = np.zeros((max_y+1, max_x+1), dtype=bool)
for dot in input_dots:
    sheet[dot[1], dot[0]] = True

for fold in folds[:1]:
    axis, pos = fold
    if axis == 'x':
        # X fold (vertical)
        new_sheet = sheet[:, :pos]
        folding_sheet = sheet[:, pos+1:]
        folding_sheet = np.flip(folding_sheet, axis=1)
        sheet = (new_sheet | folding_sheet)
    else:
        # Y fold (horizontal)
        new_sheet = sheet[:pos, :]
        folding_sheet = sheet[pos+1:, :]
        folding_sheet = np.flip(folding_sheet, axis=0)
        sheet = (new_sheet | folding_sheet)

print("The number of dots after the first fold: {}".format(sheet.sum()))

