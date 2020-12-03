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
    print(min, maximum,char, password)
    if (password[min-1] == char or password[maximum-1] == char) and not(password[min-1] == char and password[maximum-1] == char):
        print(True)
        return True
    else:
        print(False)
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

"""
for i in range (0, len(contents)):
    for j in range(i+1, len(contents)):
        sum = int(contents[i]) + int(contents[j])
        print(contents[i], "+", contents[j], "=", sum)
        if sum == 2020:
            x = contents[i]
            y = contents[j]
            product = int(contents[i]) * int(contents[j])
            break
print("x =", x, "y =", y, "Product", product)
"""
