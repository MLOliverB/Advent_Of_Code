import os

binary_list_oxygen = []
binary_list_scrubber = []

with open(os.getcwd() + "\\2021\\day_3\\day_3-input.txt", 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        binary_string_oxygen = []
        binary_string_scrubber = []
        for c in line:
            binary_string_oxygen.append(int(c))
            binary_string_scrubber.append(int(c))
        binary_list_oxygen.append(binary_string_oxygen)
        binary_list_scrubber.append(binary_string_scrubber)
        line = file.readline()

pos_oxygen = 0
while len(binary_list_oxygen) > 1:
    most_common = 0
    one_counter = 0
    zero_counter = 0

    for i in range(len(binary_list_oxygen)):
        if binary_list_oxygen[i][pos_oxygen] == 0:
            zero_counter += 1
        else:
            one_counter += 1

    if zero_counter > one_counter:
        most_common = 0
    else:
        most_common = 1
    
    for i in range(len(binary_list_oxygen)-1, -1, -1):
        if binary_list_oxygen[i][pos_oxygen] != most_common:
            binary_list_oxygen.pop(i)
    
    pos_oxygen += 1


pos_scrubber = 0
while len(binary_list_scrubber) > 1:
    least_common = 0
    one_counter = 0
    zero_counter = 0

    for i in range(len(binary_list_scrubber)):
        if binary_list_scrubber[i][pos_scrubber] == 0:
            zero_counter += 1
        else:
            one_counter += 1

    if one_counter < zero_counter:
        least_common = 1
    else:
        least_common = 0

    for i in range(len(binary_list_scrubber)-1, -1, -1):
        if binary_list_scrubber[i][pos_scrubber] != least_common:
            binary_list_scrubber.pop(i)

    pos_scrubber += 1


oxygen_rate_string = ""
scrubber_rate_string = ""

for i in range(len(binary_list_oxygen[0])):
    oxygen_rate_string += str(binary_list_oxygen[0][i])
    scrubber_rate_string += str(binary_list_scrubber[0][i])

oxygen_rate = int(oxygen_rate_string, 2)
scrubber_rate = int(scrubber_rate_string, 2)

print("Oxygen rate: {o}, Scrubber rate: {s}, Product: {prod}".format(o=oxygen_rate, s=scrubber_rate, prod=oxygen_rate*scrubber_rate))