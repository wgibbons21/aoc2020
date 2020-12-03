################################################################################
#
# Author: Walter Gibbons
# Title: Advent of Code Challenge Day02
# Source: https://adventofcode.com/2020/day/2
#
# --- Day 2: Password Philosophy ---
#
################################################################################

with open('input/day02') as fh:
    contents = fh.read().splitlines()


def validatePassword(min, maximum, char, password):
    #print(password, password.count(char))
    if password.count(char) <= maximum and password.count(char) >= min:
        return True
    else:
        return False

validPasswords = 0 

for i in range (0, len(contents)):
    #extract first (min) value from string array
    min = int(contents[i].split("-")[0])

    #extract second (max) value from string array
    maximum = int(contents[i].split("-")[1].split()[0])

    #extract third (char) value from string array
    char = contents[i].split("-")[1].split()[1].strip(":")

    #extract fourth (password) value from string array
    password = contents[i].split("-")[1].split()[2]

    if validatePassword(min, maximum, char, password):
       validPasswords += 1
    #print("Min", min, "Max", maximum, "Char", char, "Password", password)

print(validPasswords)
