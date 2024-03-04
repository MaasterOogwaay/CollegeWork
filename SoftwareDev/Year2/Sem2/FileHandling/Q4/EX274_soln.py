

def main():

    infile= open('input4.txt',"r")
    outfile = open('output4.txt', "w")
    line = infile.readline()
    line = infile.readline()
    lowest=999
    nameLowest=''
    print('Name of Person with Lowest Overall Mark (CA + Exam) =: ', file=outfile, end='')
    for line in infile:
        list = line.split(' ')
        nextname= list[0]
        nextca = int(list[1])
        nextExam = int(list[2])
        overall = nextca + nextExam
        if (overall<lowest):
            lowest=overall
            nameLowest=nextname
    print(nameLowest, file=outfile)

main()
