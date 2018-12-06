with open('input.txt') as input:
    lines = input.readlines()

# append coordinates to list of tuples
coords = []
for line in lines:
    line = line.rstrip()
    line = line.split(', ')
    coords.append((int(line[0]), int(line[1])))

# function for determining manhattan distance between a and b
def dist(a, b):
    x = abs(a[0] - b[0])
    y = abs(a[1] - b[1])
    distance = x + y
    return distance

# find geographical bounds
max_ = [0, 0]
min_ = [500, 500]
for pt in coords:
    for i in range(len(pt)):
        if pt[i] < min_[i]:
            min_[i] = pt[i]
        if pt[i] > max_[i]:
            max_[i] = pt[i]

score = 0
# for each coordinate in plane:
for y in range(min_[1], max_[1] + 1):
    for x in range(min_[0], max_[0] + 1):
        manhattans = 0
        for i in range(len(coords)):
            # calculate distance from x, y to each coord in coords, add this to running total
            manhattans += dist((x, y), coords[i])

        # if sum of all manhattan distances is < 10000, add 1 to score
        if manhattans < 10000:
            score += 1

print(score)
