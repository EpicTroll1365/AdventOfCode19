def findInputs():
    for noun in range(0,101) :
        for verb in range(0,101) :
            if (opcodeExecute(noun,verb) == 19690720) :
                return 100 * noun + verb

def opcodeExecute(noun,verb):
    fd = open('Day2Input.txt', 'r')
    opcodes = fd.readline().split(',')
    opcodes = [int(i) for i in opcodes]
    opcodes[1] = noun
    opcodes[2] = verb
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
    return opcodes[0]

print(findInputs())