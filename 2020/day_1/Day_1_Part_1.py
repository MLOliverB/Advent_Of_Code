import os

numbers = []

with open(os.getcwd() + "\\2020\\day_1\\day_1-input.txt", 'r') as file:
    line = file.readline()
    while line:
        numbers.append(int(line))
        line = file.readline()

sum = []
for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if numbers[i] + numbers[j] ==2020:
            sum = (numbers[i], numbers[j])

print(sum[0], "+", sum[1], "= 2020")
print(sum[0], "*", sum[1], "=", sum[0] * sum[1])