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
    #remove the final \n in the file which throws off the calcuation
    contents[len(contents)-1] = contents[len(contents)-1].strip('\n')
    #print(contents[len(contents)-1].strip('\n'))

sum = 0
for i in range (0, len(contents)):
    #print(contents[i].count('\n') + 1, "in the group")
    #x = set(contents[i].split('\n'))
    #print(contents[i])
    unique_answers = set()
    for j in range(0, len(contents[i])):
        if contents[i].count(contents[i][j]) >= contents[i].count('\n')+1:
            unique_answers.add(contents[i][j])
    sum = len(unique_answers) + sum
    #print(unique_answers, len(unique_answers))
print("Sum:", sum)
