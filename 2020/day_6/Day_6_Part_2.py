import os

sum = 0

def process_answers(answers):
    yes_answers = []
    people_answers = answers.split(" ")
    for c in people_answers[0]:
        includes = True
        for answers in people_answers:
            if c not in answers:
                includes = False
        if includes:
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
            if answers == "":
                answers = line
            else:
                answers += " " + line
        line = file.readline()
    
    sum += process_answers(answers)

print("Answer sum:", sum)