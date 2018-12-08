import re, pdb

with open('input.txt') as input:
    steps = input.readlines()

last = str()
avail = []
def reorder(letter):
    final.append(avail.pop(0))

    try:
        temp = [let for let in counters[letter]]
        counters.pop(letter)
    except KeyError:
        last = letter
        temp = []

    for let in temp:
        x = 0
        for key in counters.keys():
            if let in counters[key]:
                x = 1
        if x == 0:
            avail.append(let)
    avail.sort()

    if len(avail) > 0:
        reorder(avail[0])

final = []
counters = dict()
for step in steps:
    step.rstrip()
    temp = re.compile(r'[sS]tep ([A-Z]{1})').findall(step)
    try:
        counters[temp[0]].append(temp[1])
    except KeyError:
        counters[temp[0]] = [temp[1]]

for key in counters:
    i = 0
    for key2 in counters:
        if key in counters[key2]:
            i = 1
            break
    if i == 0:
        avail.append(key)

avail.sort()
reorder(avail[0])

final.append(last)
print(''.join(final))
