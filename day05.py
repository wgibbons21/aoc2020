################################################################################
#
# Author: Walter Gibbons
# Title: Advent of Code Challenge Day05
# Source: https://adventofcode.com/2020/day/5
#
#--- Day 5: Binary Boarding ---
#
################################################################################
import math as m
import pdb

#pdb.set_trace()

with open('input/day05') as fh:
    contents = fh.read().splitlines()

#for spec in contents:
#    print(spec)

#spec is a string of the 10 binary directions for seat determination
#index is the current location of the instruction i.e. 'F' 'B' 'R' 'L'
#start is the lower bound and stop is the upper bound for seating
def find_row(spec, index, start, stop):
    #print('Passed in: spec:', spec, 'index:', spec[index], 'start:', start, 'stop:', stop)

    if index == 6:
        # for r we return stop seat row
        if spec[index] == 'B':
            return stop
        # otherwise return start seat row
        else:
            return start
    else:
        #Calculate the lower half recursively
        if spec[index] == 'F':
            #print("Calculating lower half", start, ',', stop, '= start:', start, 'stop:', m.floor(((start + stop) / 2)) )
            return find_row(spec, index+1, start, m.floor(((start + stop) / 2)))
        #Calculate the uppper half recursively
        else:
            #print("Calculating upper half", start, ',', stop, '= start:', m.ceil(((start + stop) / 2)), 'stop:', stop)
            return find_row(spec, index+1, m.ceil(((start + stop) / 2)), stop)

#spec is a string of the 10 binary directions for seat determination
#index is the current location of the instruction i.e. 'F' 'B' 'R' 'L'
#start is the lower bound and stop is the upper bound for seating
def find_seat(spec, index, start, stop):
    #print('Passed in: spec:', spec, 'index:', spec[index], 'start:', start, 'stop:', stop)

    # check if we are at the last instruction
    if index == 9:
        # for r we return stop seat column
        if spec[index] == 'R':
            return stop
        # otherwise return start seat column
        else:
            return start
    else:
        #Calculate the lower half recursively
        if spec[index] == 'L':
            #print("Calculating lower half", start, ',', stop, '= start:', start, 'stop:', m.floor(((start + stop) / 2)) )
            return find_seat(spec, index+1, start, m.floor(((start + stop) / 2)))
        #Calculate the uppper half recursively
        else:
            #print("Calculating upper half", start, ',', stop, '= start:', m.ceil(((start + stop) / 2)), 'stop:', stop)
            return find_seat(spec, index+1, m.ceil(((start + stop) / 2)), stop)

index = 0
start = 0
stop = 127
highest_seat_ID = 0
#print("Row:", find_row(contents[0], index, start, stop))
#print("Seat:", find_seat(contents[0], 7, 0, 7))

for i in range(0, len(contents)):
    #print(i)
    seat_ID = (find_row(contents[i], index, start, stop)*8) + find_seat(contents[i], 7, 0, 7)
    #print("Seat ID:", seat_ID)
    if  seat_ID > highest_seat_ID:
        highest_seat_ID = seat_ID
    else:
        continue

print("Highest Seat ID:", highest_seat_ID)
