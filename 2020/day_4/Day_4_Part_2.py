import os
import string

valid_count = 0
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

def process_passport(passport):
    counted_fields = []
    passport_fields = passport.split(" ")
    for key_value in passport_fields:
        if not validate_field(key_value):
            return False
        key = key_value.split(":")[0]
        if (key in fields) and (key not in counted_fields):
            counted_fields.append(key)
    if len(fields) == len(counted_fields):
        return True
    elif (len(counted_fields) == len(fields) - 1) and ("cid" not in counted_fields):
        return True
    else:
        return False

def validate_field(key_value):
    key, value = key_value.split(":")
    if key == "byr":
        value = int(value)
        if 1920 <= value and value <= 2002:
            return True
    elif key == "iyr":
        value = int(value)
        if 2010 <= value and value <= 2020:
            return True
    elif key == "eyr":
        value = int(value)
        if 2020 <= value and value <= 2030:
            return True
    elif key == "hgt":
        if (value[-2:] in ["cm", "in"]) and (value[: -2].isdigit()):
            unit = value[-2:]
            value = int(value[:-2])
            if (unit == "cm") and (150 <= value) and (value <= 193):
                return True
            elif (unit == "in") and (59 <= value) and (value <= 76):
                return True
    elif key == "hcl":
        if (value[0] == '#') and (all(c in string.hexdigits for c in value[1:])):
            return True
    elif key == "ecl":
        if value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return True
    elif key == "pid":
        if (len(value) == 9) and (value.isdigit()):
            return True
    elif key == "cid":
        return True
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