import pdb

# open and read file line by line
input = open('input.txt')
cuts = input.readlines()

# parse input (##### @ colstart,rowstart: collen\x\rowlen)
colstart = []
rowstart = []
collen = []
rowlen = []
# keep track of canvas dimension requirements
height = 0
width = 0
for cut in cuts:
    cut = cut.rstrip()

    at = cut.split('@ ')
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

# initialize fabric sheet; height and width reqs based on max cut coords in respective dimension
grid = [[0 for i in range(width)] for j in range(height)]

# count duplicate insertions
dupes = 0

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
            dupes += insert_cut(x, y)

print(dupes)
