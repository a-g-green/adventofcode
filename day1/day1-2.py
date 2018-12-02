# open text file containing input
input = open('input.txt')

t = 0
numarray = []
sums = []

while t == 0:
    # read input line by line
    nums = input.readlines()

    # strip newlines and append line int value to numarray
    for line in nums:
        line.rstrip()
        numarray.append(int(line))

        # check sum(numarray) against list of sums
        # if present, print it and break
        if sum(numarray) in sums:
            t = 1
            print(sum(numarray))
            break
        # if not, append sum of numarray to list of sums
        else:
            sums.append(sum(numarray))

    # seek to start of file to continue reading
    input.seek(0,0)
