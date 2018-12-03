input = open('input.txt')
boxids = input.readlines()

# init vars to count for checksum
two = 0
three = 0

for boxid in boxids:
    # strip newlines
    boxid.rstrip()

    # see if any letter appears two or three times and count each once
    ALPHALEN = 26
    happened2 = False
    happened3 = False
    for i in range(ALPHALEN):
        let = chr(i + ord('a'))
        if boxid.count(let) == 2 and not happened2:
            two += 1
            happened2 = True
        if boxid.count(let) == 3 and not happened3:
            three += 1
            happened3 = True

        # if both things have happened already, we can break
        if happened2 and happened3:
            break

# calculate and print checksum
checksum = two * three
print(checksum)
