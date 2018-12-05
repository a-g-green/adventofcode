import string, operator, sys

# SUPERCHARGE THE RECURSION SYSTEM
sys.setrecursionlimit(10000)

# create a dictionary as we go; {'letter': reducedpolymerlength}
letters = dict()
# iterate over each letter
for q in range(len(string.ascii_lowercase)):
    # import input string per character as list items, excluding q and Q and \n
    poly = []
    with open('input.txt') as input:
        for char in input.read():
            if not char == '\n' and not char == string.ascii_lowercase[q] and not char == string.ascii_lowercase[q].upper():
                poly.append(char)

    # recursive function to eliminate pairs of letters
    def eliminate(list, length):
        for i in range(len(list)):
            if i < (len(list) - 1) and list[i] == list[i+1].swapcase():
                del list[i:i+2]
        # base case condition; pass in new list length if we're still recursing
        if len(list) < length:
            polylen = len(list)
            eliminate(list, polylen)

    # initialize recursive function
    polylen = len(poly)
    eliminate(poly, polylen)

    # add result to letters dictionary
    letters[string.ascii_lowercase[q]] = len(poly)

# print solution: dictionary entry for letter with minimum reduced polymer length
print(min(letters.items(), key = operator.itemgetter(1)))
