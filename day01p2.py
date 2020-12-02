################################################################################
#
# Author: Walter Gibbons
# Title: Advent of Code Challenge Day01
# Source: https://adventofcode.com/2020/day/1
#
# --- Day 1 Part 2: Report Repair ---
#
################################################################################

with open('input/day01') as fh:
    contents = fh.read().splitlines()

for i in range (0, len(contents)):
    for j in range(i+1, len(contents)):
        for k in range(j+1, len(contents)):
            sum = int(contents[i]) + int(contents[j]) + int(contents[k])
            print(contents[i], "+", contents[j], "+", contents[k], "=", sum)
            if sum == 2020:
                x = contents[i]
                y = contents[j]
                z = contents[k]
                product = int(contents[i]) * int(contents[j]) * int(contents[k])
                break
print("x =", x, "y =", y, "z =", z, "Product", product)
