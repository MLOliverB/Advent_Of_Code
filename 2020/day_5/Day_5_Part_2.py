import os

seats = []

with open(os.getcwd() + "\\2020\\day_5\\day_5-input.txt", 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        row_str = ""
        col_str = ""

        # F => 0, B => 1
        for c in line[:7]:
            if c.lower() == "f":
                row_str += '0'
            elif c.lower() == 'b':
                row_str += '1'

        # L => 0, R => 1
        for c in line[7:]:
            if c.lower() == "l":
                col_str += '0'
            elif c.lower() == 'r':
                col_str += '1'

        row = int(row_str, 2)
        col = int(col_str, 2)

        seats.append((row * 8) + col)

        line = file.readline()

my_seat = 0
seats.sort()
for i in range(1, len(seats)):
    if seats[i] == seats[i-1] + 2:
        my_seat = seats[i] - 1

print("Seat ID:", my_seat)