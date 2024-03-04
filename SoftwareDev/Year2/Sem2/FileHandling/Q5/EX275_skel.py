

def main():

    infile= open('input5.txt', "r")
    outfile = open('output5.txt', "w")
    line = infile.readline()
    line = infile.readline()

    print('List of Overall Marks=: ', file=outfile)
    print('----------------------- ', file=outfile)
    for line in infile:
        line.rstrip()
        list = line.split(" ")
        nextname = list[0]
        list1 = list[1].split(";")
        val1 = int(list1[0])
        val2 = int(list1[1])
        val3 = int(list1[2])
        val4 = int(list1[3])
        result = int((val1 + val2 + val3 + val4)/4)
        print(nextname, "\t", result, file=outfile)


main()
