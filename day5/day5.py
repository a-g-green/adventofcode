# import input string per character as list items, excluding \n
poly = []
with open('input.txt') as input:
    for char in input.read():
        if not char == '\n' and not char == (''):
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

# print solution: reduced polymer length
print(len(poly))
