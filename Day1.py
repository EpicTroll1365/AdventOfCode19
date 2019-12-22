allMasses = []

def calculateFuel():
    totalFuel = 0
    fd = open('./Day1Input.txt','r')
    for data in fd :
        allMasses.append(int(data.strip()))
    for mass in allMasses :
        totalFuel += (mass//3) - 2
    print(totalFuel)

calculateFuel()