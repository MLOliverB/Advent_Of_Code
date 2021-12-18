import os
import math

def can_explode(snail_num):
    depth = 0
    i = 0
    for c in snail_num:
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
        if depth > 4 and c == '[':
            j = i+1
            success = True
            while snail_num[j] != ']':
                if snail_num[j] == '[':
                    success = False
                j += 1
            if success:
                return True
        i += 1
    return False


def explode(snail_num):
    left_num = -1
    right_num = -1
    depth = 0
    left_bracket = -1
    right_bracket = -1
    # Find the positions and numbers to explode
    for i in range(len(snail_num)):
        if snail_num[i] == '[':
            depth += 1
        elif snail_num[i] == ']':
            depth -= 1
        if depth > 4 and snail_num[i] == '[':
            j = i+1
            is_pair = True
            while snail_num[j] != ']':
                if snail_num[j] == '[':
                    is_pair = False
                    break
                j += 1
            if is_pair:
                left_bracket = i
                right_bracket = j
                left_num, right_num = [int(num) for num in snail_num[i+1:j].split(",")]
                break

    # Find the next number to the left (if any)
    for i in range(left_bracket, -1, -1):
        if snail_num[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            h = i
            while snail_num[h-1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                h -= 1
            left_add_int = int(snail_num[h: i+1])
            old_len = len(snail_num[h: i+1])
            new_len = len(str(left_num + left_add_int))
            snail_num = snail_num[:h] + str(left_num + left_add_int) + snail_num[i+1:]
            # Adjust the position according to the length of the new sum
            left_bracket += (new_len - old_len)
            right_bracket += (new_len - old_len)
            break

    # Find the next number to the right (if any)
    for i in range(right_bracket, len(snail_num)):
        if snail_num[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            h = i+1
            while snail_num[h] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                h += 1
            left_add_int = int(snail_num[i: h])
            snail_num = snail_num[:i] + str(right_num + left_add_int) + snail_num[h:]
            break

    # Replace the pair by '0'
    snail_num = snail_num[:left_bracket] + '0' + snail_num[right_bracket+1:]
    #print("Explode {}".format(snail_num))
    return snail_num


def can_split(snail_num):
    for i in range(len(snail_num)):
        if snail_num[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            j = i+1
            while snail_num[j] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                j += 1
            if len(snail_num[i:j]) > 1:
                return True
    return False
            

def split(snail_num):
    num_start = -1
    num_end = -1
    for i in range(len(snail_num)):
        if snail_num[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            j = i
            while snail_num[j] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                j += 1
            if len(snail_num[i:j]) > 1:
                num_start = i
                num_end = j
                break
    num_int = int(snail_num[num_start: num_end])
    left_num = math.floor(num_int / 2.0)
    right_num = math.ceil(num_int / 2.0)
    snail_num =  snail_num[:num_start] + "[{},{}]".format(left_num, right_num) + snail_num[num_end:]
    #print("Split   {}".format(snail_num))
    return snail_num


# Convert the string into a nested list
def listify(str_list):
    if str_list[0] == '[' and str_list[-1] == ']':
        str_list = str_list[1:-1]
    depth = 0
    for i in range(len(str_list)):
        if str_list[i] == '[':
            depth += 1
        elif str_list[i] == ']':
            depth -= 1
        elif str_list[i] == ',' and depth != 0:
            str_list = str_list[:i] + '|' + str_list[i+1:]
    sublists = str_list.split(",")
    for i in range(len(sublists)):
        if '|' not in sublists[i]:
            sublists[i] = int(sublists[i])
        else:
            sublists[i] = listify(sublists[i].replace("|", ","))
    return sublists


# Recursive function to calculate magnitude
def get_magnitude(snail_num_list):
    mag_l = 0
    mag_r = 0
    if len(snail_num_list) != 2:
        return -1000000000
    if type(snail_num_list[0]) == list:
        mag_l = get_magnitude(snail_num_list[0])
    else:
        mag_l = snail_num_list[0]
    if type(snail_num_list[1]) == list:
        mag_r = get_magnitude(snail_num_list[1])
    else:
        mag_r = snail_num_list[1]
    return (3 * mag_l) + (2 * mag_r)










input_number_strings = []

with open(os.getcwd() + "\\2021\\day_18\\day_18-input.txt", 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        input_number_strings.append(line)
        line = file.readline()

max_magnitude = -1
max_summands = ("", "")
result = ""
for summand1 in range(len(input_number_strings)):
    for summand2 in range(len(input_number_strings)):
        if summand1 == summand2:
            continue
        sum = "[{},{}]".format(input_number_strings[summand1], input_number_strings[summand2])
        #print("{} original ({})".format(sum.ljust(100), get_magnitude(listify(sum))))
        action = 0
        if can_explode(sum):
            action = 1
        if action == 0 and can_split(sum):
            action = 2
        while action != 0:
            if action == 1:
                # Explode
                sum = explode(sum)
                #print("{} explode  ({})".format(sum.ljust(100), get_magnitude(listify(sum))))
            else:
                # Split
                sum = split(sum)
                #print("{} split   ({})".format(sum.ljust(100), get_magnitude(listify(sum))))
            action = 0
            if can_explode(sum):
                action = 1
            if action == 0 and can_split(sum):
                action = 2
        magnitude = get_magnitude(listify(sum))
        if magnitude > max_magnitude:
            max_magnitude = magnitude
            max_summands = (input_number_strings[summand1], input_number_strings[summand2])
            result = sum

result_list = listify(result)
magnitude = get_magnitude(result_list)
print("Summing {} + {}\nproduces result {}\nwith magnitude {}".format(max_summands[0], max_summands[1], result, max_magnitude))