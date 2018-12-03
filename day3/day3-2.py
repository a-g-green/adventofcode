# open and read file line by line
input = open('input.txt')
cuts = input.readlines()

# parse input (id @ colstart,rowstart: collen\x\rowlen)
id = []
colstart = []
rowstart = []
collen = []
rowlen = []
# keep track of canvas dimension requirements
height = 0
width = 0
for cut in cuts:
    cut = cut.rstrip()

    at = cut.split(' @ ')
    id.append(at[0])
    cut = at[1]

    comma = cut.split(',')
    colstart.append(int(comma[0]))
    cut = comma[1]

    colon = cut.split(': ')
    rowstart.append(int(colon[0]))
    cut = colon[1]

    x = cut.split('x')
    collen.append(int(x[0]))
    rowlen.append(int(x[1]))

    if (int(comma[0]) + int(x[0])) > width:
        width = int(comma[0]) + int(x[0])
    if (int(colon[0]) + int(x[1])) > height:
        height = int(colon[0]) + int(x[1])

# initialize canvas; height and width reqs based on max cut coords in respective dimension
grid = [[0 for i in range(width)] for j in range(height)]

# function to insert an item into array
def insert_cut(row, col):
    grid[row][col] += 1
    if grid[row][col] == 2:
        return 1
    else:
        return 0

# insert data into grid
for i in range(len(cuts)):
    for x in range(rowstart[i], rowstart[i] + rowlen[i]):
        for y in range(colstart[i], colstart[i] + collen[i]):
            insert_cut(x, y)

# function for checking each row of a cut for overlaps
def check_row(i, x):
    for y in range(colstart[i], colstart[i] + collen[i]):
        # if any square in cut overlaps, we can't use it
        if grid[x][y] >= 2:
            # we found an overlap
            return 0
    # if x is last row in cut and we made it to end with no duplicates, we have our solution
    if x == rowstart[i] + rowlen[i] - 1:
        return 2
    # we made it through the whole row with no overlaps
    else:
        return 1

# iterate over list of cuts one more time, checking for duplicates in each row
for i in range(len(cuts)):
    for x in range(rowstart[i], rowstart[i] + rowlen[i]):
        # if check_row returns 0, we can't use cut
        if check_row(i, x) == 0:
            break
        # print id of solution cut
        elif check_row(i, x) == 2:
            print(id[i])
            break
