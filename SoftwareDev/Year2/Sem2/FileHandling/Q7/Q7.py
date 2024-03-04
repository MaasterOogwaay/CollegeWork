
import re

def main():

    infile= open('input7.txt', "r")
    outfile = open('output7.txt', "w")
    line = infile.readline()
    line = infile.readline()
    smallestPop = 999
    smallestCity=''
    print('City with smallest Population is  - ', file=outfile, end='')
    for line in infile:
        list = line.split()
        nextcity = list[0]
        country = list[1]
        population = list[2]
        if (float(population) < float(smallestPop)):
            smallestPop = population
            smallestCity = nextcity

    print(smallestCity + " " + smallestPop + " Million", file=outfile)




main()

