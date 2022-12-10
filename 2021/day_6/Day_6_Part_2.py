import os
import numpy as np

current_day = 0
days = 256
timer_list = []
max_timer = 8


with open(os.getcwd() + "\\2021\\day_6\\day_6-input.txt", 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        init_timers = line.split(",")
        for timer in init_timers:
            timer = int(timer)
            timer_list.append(timer)
            if timer > max_timer:
                max_timer = timer
        line = file.readline()

fish = np.zeros(max_timer+1, dtype=np.longlong)
for timer in timer_list:
    fish[timer] += 1

while current_day < days:
    print(f"\rProcessing: {current_day} / {days}" + " " * (days % 10), end=" ")
    lowest = fish[0]
    for i in range(1, fish.shape[0]):
        fish[i-1] = fish[i]
    fish[-1] = 0
    fish[6] += lowest
    fish[8] += lowest
    current_day += 1

print(f"\rProcessing: {current_day} / {days}" + " " * (days % 10), end=" ")
print()
print("done")

print("Number of lanternfish after {} days: {}".format(days, fish.sum()))