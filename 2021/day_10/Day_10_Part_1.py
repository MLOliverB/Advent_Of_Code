import os
from collections import deque

points_map = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

brackets_map = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

syntax_error_score = 0

with open(os.getcwd() + "\\2021\\day_10\\day_10-input.txt", 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        stack = deque()
        stack_size = 0
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
                    #print("Expected {}, but found {} instead.".format(b, c))
                    syntax_error_score += points_map[c]
                    break
        line = file.readline()

print("Total Syntax Error Score: {}".format(syntax_error_score))