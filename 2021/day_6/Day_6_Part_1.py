import os
import numpy as np

current_day = 0
days = 80
timer_list = []


with open(os.getcwd() + "\\2021\\day_6\\day_6-input.txt", 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        init_timers = line.split(",")
        for timer in init_timers:
            timer_list.append(int(timer))
        line = file.readline()

fish_timers = np.array(timer_list, dtype=np.short)
while current_day < days:
    print(f"\rProcessing: {current_day} / {days}" + " " * (days % 10), end=" ")
    # decrease all timings by one
    fish_timers -= 1
    new_fish = (fish_timers < 0).sum()
    fish_timers[fish_timers < 0] = 6
    if new_fish > 0:
        fish_timers = np.concatenate((fish_timers, np.full(new_fish, 8, dtype=np.short)))

    current_day += 1

print(f"\rProcessing: {current_day} / {days}" + " " * (days % 10), end=" ")
print()
print("done")

print("Number of lanternfish after {} days: {}".format(days, fish_timers.shape[0]))