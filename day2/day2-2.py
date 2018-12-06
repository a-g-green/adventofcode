input = open('input.txt')
boxids = input.readlines()

ids = []
diff = 0

# save all strings to array first
for boxid in boxids:
    boxid = boxid.rstrip()

    ids.append([i for i in boxid])

# compare boxid to every other boxid in boxids, looking for exactly 1 difference
for x in range(len(ids)):
    for i in range(len(boxids)):
        boxids[i] = boxids[i].rstrip()

        for q in range(len(boxids[i])):
            # if letters are different, add to counter
            if not ids[x][q] == boxids[i][q]:
                diff += 1
        # if diff count still 1 after iterating whole string, we have our box
        if diff == 1:
            print(''.join(ids[x]) + ''.join(boxids[i]))
            break

        diff = 0
