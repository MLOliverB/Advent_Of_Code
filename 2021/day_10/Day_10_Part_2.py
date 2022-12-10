import os
from collections import deque

score_map = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

brackets_map = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

completion_scores = []

with open(os.getcwd() + "\\2021\\day_10\\day_10-input.txt", 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        stack = deque()
        stack_size = 0
        corrupted = False
        for c in line:
            if c in ["(", "[", "{", "<"]:
                stack.append(c)
                stack_size += 1
            else:
                s = stack.pop()
                stack_size -= 1
                b = brackets_map[s]
                if c != b:
                    # Line is corrupted
                    corrupted = True
                    break
        if not corrupted and stack_size > 0:
            # Line is incomplete
            completion_score = 0
            while stack_size > 0:
                completion_score *= 5
                completion_score += score_map[brackets_map[stack.pop()]]
                stack_size -= 1
            completion_scores.append(completion_score)
        line = file.readline()

completion_scores.sort()
middle_score = completion_scores[int(len(completion_scores)/2)]
print("Middle Score: {}".format(middle_score))