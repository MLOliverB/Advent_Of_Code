import os

binary_list = []

with open(os.getcwd() + "\\2021\\day_3\\day_3-input.txt", 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        binary_string = []
        for c in line:
            binary_string.append(int(c))
        binary_list.append(binary_string)
        line = file.readline()

most_common = []

for j in range(len(binary_list[0])):
    one_counter = 0
    zero_counter = 0
    for i in range(len(binary_list)):
        if binary_list[i][j] == 0:
            zero_counter += 1
        else:
            one_counter += 1
    if one_counter > zero_counter:
        most_common.append(1)
    else:
        most_common.append(0)

gamma_rate_string = ""
epsilon_rate_string = ""

for i in range(len(most_common)):
    cur = most_common[i]
    if cur == 0:
        gamma_rate_string += '0'
        epsilon_rate_string += '1'
    else:
        gamma_rate_string += '1'
        epsilon_rate_string += '0'

gamma_rate = int(gamma_rate_string, 2)
epsilon_rate = int(epsilon_rate_string, 2)

print("Gamma rate: {g}, Epsilon rate: {e}, Product: {prod}".format(g=gamma_rate, e=epsilon_rate, prod=gamma_rate*epsilon_rate))