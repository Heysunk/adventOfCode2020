
def modifyInstructions(instructions):
    listOfInstructions = []
    for i in range(0, len(instructions)):
        #Create a shallow copy of the instructions
        newInstructions = instructions[:]
        (instrName, instrValue) = instructions[i]
        if instrName == "nop":
            newInstructions[i] = ("jmp", instrValue)
            listOfInstructions.append(newInstructions)
        elif instrName == "jmp":
            newInstructions[i] = ("nop", instrValue)
            listOfInstructions.append(newInstructions)

    return listOfInstructions


class Program:
    def __init__(self, listOfInstructions):
        self.instructions = listOfInstructions
        self.acc = 0
        self.iP = 0 # instruction pointer
        self.visitedInstructions = dict()
    def runInstr(self, instrName, value):
        self.visitedInstructions[self.iP] = True
        nextInstrOffset = 1
        if instrName == "nop":
            nextInstrOffset = 1 # Can't have an empty if-statement
        elif instrName == "acc":
            self.acc += value
        elif instrName == "jmp":
            nextInstrOffset = value
        else:
            raise InvalidArgument("Instruction not supported: " + instrName)

        self.iP += nextInstrOffset
        return True

    def runStep(self):
        if self.iP >= len(self.instructions):
            return (False, True)
        elif self.iP in self.visitedInstructions:
            return (False, False)
        (instrName, value) = self.instructions[self.iP]
        return (self.runInstr(instrName,value), False)

    def runStepDebug(self):
        print("#PRE: ACC: "+ str(self.acc) + ", IP: " + str(self.iP) + "###")
        (validState, endOfInstrs) = res = self.runStep()
        if (endOfInstrs):
            print("Stopped running due to duplicate instruction encountered")
        print("#POST: ACC: "+ str(self.acc) + ", IP: " + str(self.iP) + "###")
        return res

listOfInstructions = []
with open("input.txt") as file_in:
    for line in file_in:
        line = line.rstrip()
        (instr, value) = line.split()
        value = int(value)
        listOfInstructions.append( (instr, value) )

modifiedInstructions = modifyInstructions(listOfInstructions)
for instructions in modifiedInstructions:
    prg = Program(instructions)
    run = True
    while run:
        (validState, endOfInstrs) = res = prg.runStep()
        if endOfInstrs == True:
            print(prg.acc)
            break
        run = validState

