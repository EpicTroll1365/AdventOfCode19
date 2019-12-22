def ReadFile():
    fd = open('./Day3Input.txt', 'r')
    wires = []
    for data in fd:
        wires.append(data.strip())
    return wires

def getDistance(wire, intersections):
    x,y = 0,0
    distanceDict = dict()
    distance = 0

    for i in range(0,len(wire)):
        for k in range(int(wire[i][1:])):
            op = wire[i][0]
            if op == 'L':
                x -= 1
            elif op == 'R':
                x += 1
            elif op == 'U':
                y += 1
            elif op == 'D':
                y -= 1
            distance += 1
            if (x,y) in intersections:
                distanceDict[(x,y)] = distance
    return distanceDict

def getPositions(wire):
    positions = set()
    x,y = 0,0
    
    for i in range(0,len(wire)):
        vroom = int(wire[i][1:])
        op = wire[i][0]
        for k in range(vroom):
            if op == 'L':
                x -= 1
            elif op == 'R':
                x += 1
            elif op == 'U':
                y += 1
            elif op == 'D':
                y -= 1
            positions.add((x,y))
    return positions

def findDistance():
    fd = ReadFile()
    wire1 = fd[0].split(',')
    wire2 = fd[1].split(',')
    positions1 = getPositions(wire1)
    positions2 = getPositions(wire2)

    intersections = positions1.intersection(positions2)

    distance1 = getDistance(wire1, intersections)
    distance2 = getDistance(wire2, intersections)

    return min(distance1[crossing] + distance2[crossing] for crossing in intersections)

print(findDistance())
