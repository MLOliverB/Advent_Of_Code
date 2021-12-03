import os

valid_count = 0
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

def process_passport(passport):
    counted_fields = []
    passport_fields = passport.split(" ")
    for key_value in passport_fields:
        key = key_value.split(":")[0]
        if (key in fields) and (key not in counted_fields):
            counted_fields.append(key)
    if len(fields) == len(counted_fields):
        return True
    elif (len(counted_fields) == len(fields) - 1) and ("cid" not in counted_fields):
        return True
    else:
        return False

with open(os.getcwd() + "\\2020\\day_4\\day_4-input.txt", 'r') as file:
    line = file.readline()
    passport = ""
    while line:
        line = line.strip()
        if line == "":
            if process_passport(passport):
                valid_count += 1
            passport = ""
        else:
            if passport == "":
                passport = line
            else:
                passport = passport + " " + line
        line = file.readline()
    
    if process_passport(passport):
        valid_count += 1

print("Valid passports:", valid_count)