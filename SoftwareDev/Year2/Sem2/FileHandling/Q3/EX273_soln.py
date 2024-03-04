

def main():

    infile= open('input3.txt',"r")
    outfile = open('output3.txt', "w")
    highest=0
    nameHighest=''
    print('Highest Overall Mark (CA + Exam) =: ', file=outfile, end='')
    for line in infile:
        list = line.split(' ')
        nextname= list[0]
        nextca = int(list[1])
        nextExam = int(list[2])
        overall = nextca + nextExam
        if (overall>highest):
            highest=overall

    print(highest, file=outfile)

main()
