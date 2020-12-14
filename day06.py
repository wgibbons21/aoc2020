################################################################################
#
# Author: Walter Gibbons
# Title: Advent of Code Challenge Day06
# Source: https://adventofcode.com/2020/day/6
#
#--- Day 6: Custom Customs ---
#
################################################################################

with open('input/day06') as fh:
    contents = fh.read().split('\n\n')

sum = 0
for i in range (0, len(contents)):
    sum = sum + len(set(contents[i].replace('\n', '')))
    print("i:", i, len(set(contents[i].replace('\n', ''))))
print("Sum:", sum)
