import os

valid_count = 0

with open(os.getcwd() + "\\2020\\day_2\\day_2-input.txt", 'r') as file:
    line = file.readline()
    while line:
        range, letter, text = line.split(" ")
        text = text.strip()
        pos_1, pos_2 = range.split("-")
        pos_1 = int(pos_1) - 1
        pos_2 = int(pos_2) - 1
        letter = letter.split(":")[0]

        if pos_1 < len(text):
            is_pos_1 = True if text[pos_1] == letter else False
        else:
            is_pos_1 = False

        if pos_2 < len(text):
            is_pos_2 = True if text[pos_2] == letter else False
        else:
            is_pos_2 = False

        print(text, range, letter, is_pos_1, is_pos_2, is_pos_1 ^ is_pos_2)
        if is_pos_1 ^ is_pos_2:
            valid_count += 1

        line = file.readline()

print("Valid passwords:", valid_count)