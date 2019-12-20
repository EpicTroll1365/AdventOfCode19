def opcodeExecute() :
    fd = open('Day2Input.txt', 'r')
    opcodes = fd.readline().split(',')
    opcodes = [int(i) for i in opcodes]
    opcodes[1] = 12
    opcodes[2] = 2
    count = 0
    while True:
        code = opcodes[count]
        param1 = opcodes[count+1]
        param2 = opcodes[count+2]
        position = opcodes[count+3]
        if code == 1 :
            opcodes[position] = opcodes[param1] + opcodes[param2]
        elif code == 2 :
            opcodes[position] = opcodes[param1] * opcodes[param2]
        elif code == 99 :
            break
        count += 4
    print(opcodes[0])

opcodeExecute()
