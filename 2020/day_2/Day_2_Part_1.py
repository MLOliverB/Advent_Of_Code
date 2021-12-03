import os

valid_count = 0

with open(os.getcwd() + "\\2020\\day_2\\day_2-input.txt", 'r') as file:
    line = file.readline()
    while line:
        range, letter, text = line.split(" ")
        text = text.strip()
        min_range, max_range = range.split("-")
        min_range = int(min_range)
        max_range = int(max_range)
        letter = letter.split(":")[0]

        letter_count = 0

        for character in text:
            if character == letter:
                letter_count += 1

        if (min_range <= letter_count) and (letter_count <= max_range):
            valid_count += 1

        line = file.readline()

print("Valid passwords:", valid_count)