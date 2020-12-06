################################################################################
#
# Author: Walter Gibbons
# Title: Advent of Code Challenge Day03
# Source: https://adventofcode.com/2020/day/3
#
# --- Day 3: Toboggan Trajectory ---
#
################################################################################

with open('input/day03') as fh:
    contents = fh.read().splitlines()

def toboggan_tree_count(input_map, xmove, ymove):

    trees_encountered = 0
    x = 0
    y = 0

    # loop through each row as determined by the ymove
    # print("Len of input map", len(input_map))
    # i starts at 1 since we don't evaluate row 0
    for i in range(1, len(input_map)):
        print(i, x)
        # if the x move takes us out of bounds, wrap around the array
        if xmove + x >= len(input_map[0]):
            x = xmove + x - len(input_map[0])
        # no wrapping needed
        else:
            print("Evaluating else")
            x = xmove + x
        # did we run into a tree (#)
        if input_map[i][x] == '#':
            print("Encountered a tree at", i, x)
            trees_encountered += 1
    return trees_encountered

# what is the slope we are using to traverse the map
#x_move = 3
#y_move = 1

print(toboggan_tree_count(contents, 1, 1))
print(toboggan_tree_count(contents, 3, 1))
print(toboggan_tree_count(contents, 5, 1))
print(toboggan_tree_count(contents, 7, 1))
print(toboggan_tree_count(contents, 1, 2))
