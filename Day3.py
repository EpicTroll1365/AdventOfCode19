def ReadFile():
    fd = open('./Day3Input.txt', 'r')
    wires = []
    for data in fd:
        wires.append(data.strip())
    return wires

def manhattan(position):
    return (abs(position[0]) + abs(position[1]))

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

def findIntersection():
    fd = ReadFile()
    wire1 = fd[0].split(',')
    wire2 = fd[1].split(',')
    positions1 = getPositions(wire1)
    positions2 = getPositions(wire2)

    intersections = positions1.intersection(positions2)

    return min(manhattan(pos) for pos in intersections)

print(findIntersection())
