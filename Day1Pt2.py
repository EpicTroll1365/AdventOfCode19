allMasses = []

def calculateFuel():
    totalFuel = 0
    fd = open('./Day1Input.txt','r')
    for data in fd :
        allMasses.append(int(data.strip()))
    for mass in allMasses :
        fuelToAdd = (mass//3) - 2
        totalFuel += fuelToAdd
        while (((fuelToAdd//3) - 2) > 0) :
            fuelToAdd = (fuelToAdd//3) - 2
            totalFuel += fuelToAdd
    print(totalFuel)

calculateFuel()