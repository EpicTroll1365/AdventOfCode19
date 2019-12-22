inputYeet = '357253-892942'
passRange = [int (i) for i in inputYeet.split('-')]

def adjacentNums(num):
    found = False
    for i in range(1,len(num)):
        if num[i] == num[i-1]:
            found = True
            break
    return found

def findDecrease(num):
    decrease = False
    for i in range(1,len(num)):
        if int(num[i]) < int(num[i-1]):
            decrease = True
            break
    return decrease


def findPasswords(passRange):
    passwords = []
    for passw in range(passRange[0]+1,passRange[1]): #Within the range bleh
        strNum = str(passw)
        if len(strNum) != 6:
            continue
        elif not adjacentNums(strNum):
            continue
        elif findDecrease(strNum):
            continue
        passwords.append(passw)
    print(len(passwords))

findPasswords(passRange)