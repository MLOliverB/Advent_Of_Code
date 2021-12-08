import os

# Define the 7-Segment Display Mapping as follows:
#          0
#        -----
#     5 |     | 1
#       |  6  |
#        -----
#     4 |     | 2
#       |  3  |
#        -----

def get_number_segments(number):
    number_map = {
        0: [0, 1, 2, 3, 4, 5],
        1: [1, 2],
        2: [0, 1, 3, 4, 6],
        3: [0, 1, 2, 3, 6],
        4: [1, 2, 5, 6],
        5: [0, 2, 3, 5, 6],
        6: [0, 2, 3, 4, 5, 6],
        7: [0, 1, 2],
        8: [0, 1, 2, 3, 4, 5, 6],
        9: [0, 1, 2, 3, 5, 6],
    }
    if number in number_map:
        return number_map[number]
    else:
        return []

def get_segments_number(segments):
    if segments == [0, 1, 2, 3, 4, 5]:
        return 0
    elif segments == [1, 2]:
        return 1
    elif segments == [0, 1, 3, 4, 6]:
        return 2
    elif segments == [0, 1, 2, 3, 6]:
        return 3
    elif segments == [1, 2, 5, 6]:
        return 4
    elif segments == [0, 2, 3, 5, 6]:
        return 5
    elif segments == [0, 2, 3, 4, 5, 6]:
        return 6
    elif segments == [0, 1, 2]:
        return 7
    elif segments == [0, 1, 2, 3, 4, 5, 6]:
        return 8
    elif segments == [0, 1, 2, 3, 5, 6]:
        return 9
    return -1

def is_map_uncertain(letter_map):
    uncertain = False
    for letter in letter_map:
        if len(letter_map[letter]) > 1:
            uncertain = True
            break
    return uncertain

input_digits = []
output_digits = []
letter_map = []

with open(os.getcwd() + "\\2021\\day_8\\day_8-input.txt", 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        input, output = line.split(" | ")
        input = input.split(" ")
        input.sort(key=lambda e: len(e)) # Sort the entries by length in ascending order)
        input_digits.append(input)
        output_digits.append(output.split(" "))
        line = file.readline()

for row in input_digits:
    letter_map_row = {}
    # row[0] is the digit 1 - they're either in segment 1 or 2
    for letter in row[0]:
        letter_map_row[letter] = [1, 2]
    # row[1] is the digit 7 - we can determine which letter is for segment 0
    for letter in row[1]:
        if letter not in letter_map_row:
            letter_map_row[letter] = [0, ]
    # row[3] is the digit 4 - we can determine probability of 5 or 6 for two of the letters
    for letter in row[2]:
        if letter not in letter_map_row:
            letter_map_row[letter] = [5, 6]
    # Add the remaining letters with the remaining segments as their mappings
    segments = [0, 1, 2, 3, 4, 5, 6]
    for letter in letter_map_row:
        for segment in letter_map_row[letter]:
            if segment in segments:
                segments.remove(segment)
    for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        if letter not in letter_map_row:
            letter_map_row[letter] = list(segments)
    # Now let's try to make some deductions - Each letter can map to maximally one of two segments
    i = 3
    while is_map_uncertain(letter_map_row):
        #print(i, row[i], letter_map_row)
        possible_numbers = []
        if len(row[i]) == 5:
            possible_numbers = [2, 3, 5]
        elif len(row[i]) == 6:
            possible_numbers = [0, 6, 9]
        elif len(row[i]) == 7:
            possible_numbers = [8, ]
        certain_segments = []
        for letter in row[i]:
            if len(letter_map_row[letter]) == 1:
                if letter_map_row[letter][0] not in certain_segments:
                    certain_segments.append(letter_map_row[letter][0])
            else:
                for letter2 in row[i]:
                    if letter != letter2:
                        if letter_map_row[letter] == letter_map_row[letter2]:
                            if letter_map_row[letter][0] not in certain_segments:
                                certain_segments.append(letter_map_row[letter][0])
                            if letter_map_row[letter][1] not in certain_segments:
                                certain_segments.append(letter_map_row[letter][1])
        for j in range(len(possible_numbers)-1, -1, -1):
            number_segments = get_number_segments(possible_numbers[j])
            for seg in certain_segments:
                if seg not in number_segments:
                    possible_numbers.pop(j)
                    break
        if len(possible_numbers) == 1:
            # We can now determine more mappings
            leftover_segments = get_number_segments(possible_numbers[0])
            for j in range(len(leftover_segments)-1, -1, -1):
                if leftover_segments[j] in certain_segments:
                    leftover_segments.pop(j)
            if len(leftover_segments) > 0:
                for letter in row[i]:
                    for seg in letter_map_row[letter]:
                        if seg in leftover_segments:
                            letter_map_row[letter] = [seg, ]
                            break
        i += 1
        if i == len(row):
            i = 3
    letter_map.append(letter_map_row)

sum = 0

for i in range(len(output_digits)):
    number = ""
    for string in output_digits[i]:
        segments = []
        for letter in string:
            segments.append(letter_map[i][letter][0])
        segments.sort()
        number += str(get_segments_number(segments))
    sum += int(number)

print("Sum of output values {}".format(sum))