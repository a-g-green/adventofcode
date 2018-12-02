# open and read text file containing input
input = open('input.txt')
nums = input.readlines()

# initialize numarray and append each line of file, strip newlines
numarray = []
for line in nums:
    line.rstrip()
    numarray.append(int(line))

# print sum of array
print(sum(numarray))
