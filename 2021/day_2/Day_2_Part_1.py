import os

horizontal = 0
depth = 0

with open(os.getcwd() + "\\2021\\day_2\\day_2-input.txt", 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        motion, step = line.split(" ")
        step = int(step)
        if motion == "forward":
            horizontal += step
        elif motion == "down":
            depth += step
        elif motion == "up":
            depth -= step
        line = file.readline()

print("Horizontal: {horiz}, Depth: {depth}, Product: {prod}".format(horiz=horizontal, depth=depth, prod=horizontal*depth))