################################################################################
#
# Author: Walter Gibbons
# Title: Advent of Code Challenge Day04
# Source: https://adventofcode.com/2020/day/4
#
#--- Day 4: Passport Processing ---
#
################################################################################
import re
# split into string array by the blank line
with open('input/day04') as fh:
    contents = fh.read().split('\n\n')

def validate_fields(passport_data):

    invalid_token = 0
    eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    print(passport_data)
    for field in passport_data:
        #print(field)
        #check byr is between 1920 and 2002
        #print(field.split(':')[1])
        if field.split(':')[0] == 'byr' and int(field.split(':')[1]) in range(1920, 2002+1):
            print('byr is valid', field.split(':')[1])
        else:
            invalid_token += 1

        #check iyr is between 2010 and 2002
        if field.split(':')[0] == 'iyr' and int(field.split(':')[1]) in range(2010, 2020+1):
            print('iyr is valid', field.split(':')[1])
        else:
            invalid_token += 1

        #check eyr is between 2010 and 2002
        if field.split(':')[0] == 'eyr' and int(field.split(':')[1]) in range(2020, 2030+1):
            print('eyr is valid', field.split(':')[1])
        else:
            invalid_token += 1

        #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth
        if field.split(':')[0] == 'ecl' and field.split(':')[1] in eye_color:
            print('ecl is valid', field.split(':')[1])
        else:
            invalid_token += 1

        #pid (Passport ID) - a nine-digit number, including leading zeroes
        if field.split(':')[0] == 'pid' and len(field.split(':')[1]) == 9:
            print('pid is valid', field.split(':')[1])
        else:
            invalid_token += 1

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f
        if field.split(':')[0] == 'hcl' and re.search('[0-9a-f]{6}', field.split(':')[1]) != None:
            print('hcl is valid', field.split(':')[1])
        else:
            invalid_token += 1

    return invalid_token

valid_passports = 0

# loop through each passport record string
for i in range(0, len(contents)):
    # split into 2 dimensions on a blank or a \n
    contents[i] = contents[i].split()
    #print(contents[i])
    if len(contents[i]) >= 7:
        # if length is 7 and it contains CID field its missing a mandatory field
        if not (([j for j in contents[i] if "cid" in j]) and len(contents[i]) == 7):
            print(validate_fields(contents[i]))
            if validate_fields(contents[i]) == 0:
                valid_passports += 1

print("Valid Passports:", valid_passports)
