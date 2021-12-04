import os

sum = 0

def process_answers(answers):
    yes_answers = []
    for c in answers:
        if c not in yes_answers:
            yes_answers.append(c)
    return len(yes_answers)

with open(os.getcwd() + "\\2020\\day_6\\day_6-input.txt", 'r') as file:
    line = file.readline()
    answers = ""
    while line:
        line = line.strip()
        if line == "":
            sum += process_answers(answers)
            answers = ""
        else:
            answers += line
        line = file.readline()
    
    sum += process_answers(answers)

print("Answer sum:", sum)