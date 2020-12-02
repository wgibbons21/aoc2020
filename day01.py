################################################################################
#
# Author: Walter Gibbons
# Title: Advent of Code Challenge Day01
# Source: https://adventofcode.com/2020/day/1
#
# --- Day 1: Report Repair ---
#
################################################################################

with open('input/day01') as fh:
    contents = fh.read().splitlines()

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
