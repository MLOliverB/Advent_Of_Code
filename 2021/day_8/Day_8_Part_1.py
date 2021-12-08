import os

output_digits = []


with open(os.getcwd() + "\\2021\\day_8\\day_8-input.txt", 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        input, output = line.split(" | ")
        output_digits.append(output.split(" "))
        line = file.readline()

appearances = 0
for row in output_digits:
    for digit in row:
        if len(digit) in [2, 4, 3, 7]:
            appearances += 1

print("Digits 1, 4, 7, 8 appear {} times".format(appearances))