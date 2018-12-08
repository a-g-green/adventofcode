import re

with open('input.txt') as input:
    steps = input.readlines()

# initialize trackers for last item, available items and final string
last = str()
avail = list()
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

# initialize timer and workers
# workers are ['letter they're currently working on', 0/1 if idle/working, time they will complete current job]
time = 0
workers = [[str(),0,0] for i in range(5)]
def check_it(time):
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
    # for each available item that isn't already assigned to a worker, try to find an available worker
    for item in avail:
        for worker in workers:
            if worker[1] == 0 and item not in [worker[0] for worker in workers]:
                # if we find one, change worker to reflect new item, busy status and indication of when job will be done
                worker[0] = item
                worker[1] = 1
                worker[2] = time + (ord(item) - 4)

# start! we haven't done all steps yet, so didlast is initialized false
check_it(time)
didlast = False
while len(final) < 26:
    # check each worker who is working to see if his job is done yet
    for worker in workers:
        if worker[1] == 1 and (time + 1) > worker[2]:
            # if so, we append his job to final, toggle him to idle, delete
            # his job from dependency dictionary and available items
            final.append(worker[0])
            worker[1] = 0
            if worker[0] in counters:
                del counters[worker[0]]
            for item in avail:
                if item == worker[0]:
                    del avail[avail.index(item)]
            worker[0] = ''
            # see what we can do now that a step has been completed
            check_it(time)

    # if we've done 25 steps, we know there's only one left
    if len(final) == 25 and didlast == False:
        # append it to available list and get started
        avail.append(last)
        didlast = True
        check_it(time)

    # only increment time if we're not done yet
    elif len(final) == 26:
        break
    else:
        time += 1

print(''.join(final))
print(time)
