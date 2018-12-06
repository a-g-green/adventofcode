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

# keep score for each coord
score = [0 for coord in coords]
# for each coordinate in plane:
for y in range(min_[1], max_[1] + 1):
    for x in range(min_[0], max_[0] + 1):
        # give newlowdist arbitrary large value (we use distance between min_ and max_)
        newlowdist = dist(min_, max_)
        closestcoord = int()
        for i in range(len(coords)):
            # calculate distance from x,y to coord
            currentdist = dist((x, y), coords[i])
            # check this against newlowdist
            if currentdist < newlowdist:
                # if it's smaller, keep it and also save which coord we're looking at
                newlowdist = currentdist
                closestcoord = i
            elif currentdist == newlowdist:
                # if currentdist ends up being equal to newlowdist (implying x,y is
                # equally closest to two or more points in coords), we don't count it
                closestcoord = None

        # if x,y is closest to one point in coords, add to that coord's score
        if closestcoord:
            score[closestcoord] += 1

highest = max(score)
print(highest)
print(score)
