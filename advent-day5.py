
inputprogram = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,78,40,225,1102,52,43,224,1001,224,-2236,224,4,224,102,8,223,223,101,4,224,224,1,224,223,223,1,191,61,224,1001,224,-131,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,1101,86,74,225,1102,14,76,225,1101,73,83,224,101,-156,224,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,1102,43,82,225,2,196,13,224,101,-6162,224,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1001,161,51,224,101,-70,224,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,102,52,187,224,1001,224,-832,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,1102,19,79,225,101,65,92,224,1001,224,-147,224,4,224,1002,223,8,223,101,4,224,224,1,223,224,223,1102,16,90,225,1102,45,44,225,1102,92,79,225,1002,65,34,224,101,-476,224,224,4,224,102,8,223,223,1001,224,5,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,107,226,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,1007,226,226,224,102,2,223,223,1005,224,344,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,359,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,374,101,1,223,223,1107,226,677,224,1002,223,2,223,1006,224,389,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,404,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,419,1001,223,1,223,7,677,226,224,102,2,223,223,1005,224,434,101,1,223,223,1007,677,677,224,102,2,223,223,1005,224,449,1001,223,1,223,108,226,677,224,102,2,223,223,1005,224,464,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,479,101,1,223,223,107,226,677,224,102,2,223,223,1006,224,494,1001,223,1,223,7,226,226,224,1002,223,2,223,1006,224,509,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,524,101,1,223,223,1107,677,226,224,102,2,223,223,1005,224,539,101,1,223,223,1008,677,226,224,102,2,223,223,1005,224,554,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,569,101,1,223,223,1107,677,677,224,102,2,223,223,1006,224,584,1001,223,1,223,1108,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,614,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,629,101,1,223,223,1007,677,226,224,102,2,223,223,1006,224,644,101,1,223,223,8,677,677,224,1002,223,2,223,1006,224,659,101,1,223,223,8,677,226,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226]

#inputprogram = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
def main(input, inputprogram):
    memory = inputprogram
    program(memory, input)


def getOperandmode(position, memory):
    instructionvalue = memory[position]
    operandmodes = [0,0,0]
    if len(str(instructionvalue)) >= 3:
        operandmodes[0] = int(str(instructionvalue)[-3:-2])
    if len(str(instructionvalue)) >= 4:
        operandmodes[1] = int(str(instructionvalue)[-4:-3])
    if len(str(instructionvalue)) >= 5:
        operandmodes[2]= int(str(instructionvalue)[-5:-4])
    return operandmodes

def getValue(index, position, memory, operandmodes):

    value = memory[position + 1 + index]
    operandmode = operandmodes[index]
    if (operandmode == 1):
        return value
    else:
        return memory[value]

def getAddress(index,position,memory,operandmodes):
    value = memory[position + 1 + index]
    operandmode = operandmodes[index]
    # if (operandmode != 0):
    #      print("Operandmode for address %s is wrong" % value)
    # else:
    return value


def program(memory, input):
    position = 0
    index = 0
    output=0

    while True:
        operandmodes = getOperandmode(position, memory)
        opcode = abs(memory[position]) % 100
        if opcode == 99:
            print("Program Finished")
            print("Output is %s" % output)
            return output
        if opcode == 1:
            parameter1 = getValue(0,position,memory,operandmodes)
            parameter2 = getValue(1,position,memory,operandmodes)
            parameter3 = getAddress(2,position,memory,operandmodes)
            memory[parameter3] = parameter1+parameter2
            position += 4
        if opcode == 2:
            parameter1 = getValue(0,position,memory,operandmodes)
            parameter2 = getValue(1,position,memory,operandmodes)
            parameter3 = getAddress(2,position,memory,operandmodes)
            memory[parameter3] = parameter1*parameter2
            position += 4
        if opcode == 3:
            parameter1 = getAddress(0,position,memory,operandmodes)
            memory[parameter1] = input
            position += 2
        if opcode == 4:
            parameter1 = getAddress(0,position,memory,operandmodes)
            output = memory[parameter1]
            position += 2
        if opcode == 5:
            parameter1 = getValue(0,position,memory,operandmodes)
            parameter2 = getValue(1,position,memory,operandmodes)
            if parameter1 != 0:
                position = parameter2
            else:
                position += 3
        if opcode == 6:
            parameter1 = getValue(0,position,memory,operandmodes)
            parameter2 = getValue(1,position,memory,operandmodes)
            if parameter1 == 0:
                position = parameter2
            else:
                position += 3
        if opcode == 7:
            parameter1 = getValue(0,position,memory,operandmodes)
            parameter2 = getValue(1,position,memory,operandmodes)
            parameter3 = getAddress(2,position,memory,operandmodes)
            if parameter1 < parameter2:
                memory[parameter3]=1
            else:
                memory[parameter3]=0
            position += 4
        if opcode == 8:
            parameter1 = getValue(0,position,memory,operandmodes)
            parameter2 = getValue(1,position,memory,operandmodes)
            parameter3 = getAddress(2,position,memory,operandmodes)
            if parameter1 == parameter2:
                memory[parameter3]=1
            else:
                memory[parameter3]=0
            position += 4

#
main(5, inputprogram)
