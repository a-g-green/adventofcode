import re
import operator
from datetime import datetime

with open('input.txt') as input:
    entries = input.readlines()

log = []
# split entries into [datetime] logentry
for entry in entries:
    #pdb.set_trace()
    entry = entry[6:]
    entry = entry.split('] ')
    log.append(entry)

# sort entries by datetime
log.sort(key = lambda x: datetime.strptime(x[0], '%m-%d %H:%M'))

# add all guards to dict
guards = dict()
sleeptimes = dict()
lastguard = str()
for i in range(0, len(log)):
    guard = re.findall(r'#\d+', str(log[i]))
    if guard:
        guard = guard[0]
        # if guard isn't in dict, put him there
        try:
            guards[guard]
        except KeyError:
            guards[guard] = [[] for i in range(60)]
        sleeptimes[guard] = 0
    # keep track of most recent guard
    if guard:
        lastguard = guard

    # add sleep times for each guard
    sleep = re.findall(r'falls\sasleep', str(log[i][1]))
    if sleep:
        # get fall asleep time and wake up time
        minute = int(log[i][0][-2:])
        nextminute = int(log[i+1][0][-2:])
        # mark guard awake (0) or asleep (1) during each period
        for j in range(minute):
            guards[lastguard][j].append(0)
        for j in range(minute, nextminute):
            guards[lastguard][j].append(1)
        for j in range(nextminute, 60):
            guards[lastguard][j].append(0)

# calculate total amount of time each guard slept
for guard in guards:
    # sum, but first make sure array isn't empty (implying guard never slept)
    if not guards[guard][0] == []:
        for i in range(len(guards[guard])):
            sleeptimes[guard] = sum(map(sum, guards[guard]))

maxtime = max(sleeptimes.items(), key = operator.itemgetter(1))
minutes = list()
#maxminute = map(sum, guards[maxtime[0]])
for i in range(len(guards[maxtime[0]])):
    minutes.append(sum(guards[maxtime[0]][i]))

print(sleeptimes)
print(f"sleepiest guard, minutes slept: {maxtime}")
print(f"minute most likely to be asleep: {minutes.index(max(minutes))}")
