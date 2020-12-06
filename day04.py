################################################################################
#
# Author: Walter Gibbons
# Title: Advent of Code Challenge Day04
# Source: https://adventofcode.com/2020/day/4
#
#--- Day 4: Passport Processing ---
#
################################################################################

# split into string array by the blank line
with open('input/day04') as fh:
    contents = fh.read().split('\n\n')

valid_passports = 0

# loop through each passport record string
for i in range(0, len(contents)):
    # split into 2 dimensions on a blank or a \n
    contents[i] = contents[i].split()

    if len(contents[i]) >= 7:
        # if length is 7 and it contains CID field its missing a mandatory field
        if ([j for j in contents[i] if "cid" in j]) and len(contents[i]) == 7:
            print("invalid", contents[i])
        else:
            valid_passports += 1

print("Valid Passports:", valid_passports)
