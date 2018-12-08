import re

with open('input.txt') as input:
    steps = input.readlines()

# initialize trackers for last item, available items and final string
last = str()
avail = []
final = []
# put each step in dictionary, appending dependent for ea key as necessary {'dependency': [dependent]}
counters = dict()
for step in steps:
    step.rstrip()
    temp = re.compile(r'[sS]tep ([A-Z]{1})').findall(step)
    try:
        counters[temp[0]].append(temp[1])
    except KeyError:
        counters[temp[0]] = [temp[1]]
# find last item in final string (the only letter which has no dependents)
for key in counters:
    for value in counters[key]:
        if value not in counters:
            last = value

def check_it():
    # for each key in counters, we want to check if it is dependent on any other key
    # if it is, mark it as such and break
    # if we get through the whole list and don't find key, we can add it to available and pop it out of counters
    for key in counters:
        x = 0
        for dependency in counters:
            if key in counters[dependency]:
                x = 1
                break
        if x == 0 and key not in avail:
            avail.append(key)
    avail.sort()

# start!
check_it()
while len(final) < 26:
    # append first available step (from alpha sorted list of steps)
    final.append(avail[0])
    # remove step from dependency dictionary and available items list
    if avail[0] in counters:
        del counters[avail[0]]
    del avail[0]
    # if final is 25 chars, we know we just have the last step left, so make it available if it isn't already
    if len(final) == 25 and last not in avail:
        avail.append(last)
    # see what we can do now that we've completed a step
    check_it()

print(''.join(final))
