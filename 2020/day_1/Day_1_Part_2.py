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
        for k in range(j, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] ==2020:
                sum = (numbers[i], numbers[j], numbers[k])

print(sum[0], "+", sum[1], "+", sum[2], "= 2020")
print(sum[0], "*", sum[1], "*", sum[2], "=", sum[0] * sum[1] * sum[2])