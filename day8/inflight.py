
class Instr:
    def __init__(self, instrName, value):
        self.instrName = instrName
        self.value = value
        self.visited = False


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
        if self.iP in self.instructions:
            return False
        (instrName, value) = self.instructions[self.iP]
        return self.runInstr(instrName,value)

    def runStepDebug(self):
        if self.iP in self.visitedInstructions:
            print("Stopped running due to duplicate instruction encountered")
            print("#POST: ACC: "+ str(self.acc) + ", IP: " + str(self.iP) + "###")
            return False
        print("#PRE: ACC: "+ str(self.acc) + ", IP: " + str(self.iP) + "###")
        (instrName, value) = self.instructions[self.iP]
        retRes = self.runInstr(instrName,value)
        print("#POST: ACC: "+ str(self.acc) + ", IP: " + str(self.iP) + "###")
        return retRes



instructions = []

with open("input.txt") as file_in:
    for line in file_in:
        line = line.rstrip()
        (instr, value) = line.split()
        value = int(value)
        instructions.append( (instr, value) )


prg = Program(instructions)
while prg.runStepDebug():
    x = 1


