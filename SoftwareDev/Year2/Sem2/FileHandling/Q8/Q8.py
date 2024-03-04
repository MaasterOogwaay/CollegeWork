
import re

def main():

    infile= open('input8.txt', "r")
    outfile = open('output8.txt', "w")
    line = infile.readline()
    line = infile.readline()
    totalGoals = 0
    print('Total Goals Scored (Home and Away) by all Players = ', file=outfile, end='')
    for line in infile:
        list = line.split()
        nextname = list[0]
        totalGoals += int(list[1])
        totalGoals += int(list[2])

    print(totalGoals, file=outfile)


main()

