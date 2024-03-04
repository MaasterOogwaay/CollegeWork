

def main():

    infile= open('input2.txt',"r")
    outfile = open('output2.txt', "w")
    age=0
    oldest=''
    print('Name of Oldest Person is: ', file=outfile, end='')
    for line in infile:
        line= line.rstrip()
        list = line.split(' ')
        nextname= list[0]
        nextage = int(list[1])
        if (nextage>age):
            age=nextage
            oldest=nextname
    print(oldest, file=outfile)

main()
