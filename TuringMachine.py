import sys

class Tape(object):
    def __init__(self, input="",blank=" "):
        self.tape = {}
        self.blank=blank
        for i in range(len(input)):
            self.tape[i] = input[i]
        
    def __str__(self):
        s = ""
        minID = min(self.tape.keys()) 
        maxID = max(self.tape.keys())
        for i in range(minID,maxID):
            s += self.tape[i]
        return s    
   
    def __getitem__(self,index):
        if index in self.tape:
            return self.tape[index]
        else:
            return self.blank

    def __setitem__(self, pos, char):
        self.tape[pos] = char 


        
class TuringMachine(object):
    def __init__(self, tape = "", tapeAlphabet = ["0", "1","2","$","#"," ","x"],initialState = "",finalStates = [],transitionFunction = {}):
        self.notAccept = "qr"
        self.blank = " "
        self.tape = Tape(tape,self.blank)
        self.headPos = 0
        self.curState = initialState
        self.transFunc = transitionFunction
        self.alph = tapeAlphabet
        self.finalState = finalStates
        
    def showTape(self): 
        print(self.tape)
        return True
    
    def step(self):
        curChar = self.tape[self.headPos]
        if curChar not in self.alph:
            self.curState="qr"
            return
        x = (self.curState, curChar)
        if x in self.transFunc:
            y = self.transFunc[x]
            self.tape[self.headPos] = y[1]
            if y[2] == "R":
                 self.headPos = self.headPos + 1
            elif y[2] == "L":
                self.headPos = self.headPos - 1
            self.curState = y[0]

    def final(self):
        print("%s\t%s\t%d"%(self.curState,self.tape,self.headPos))
        if self.curState in self.finalState:
            return True
        else:
            return False

    def accept(self):
        if self.curState == "qr":
            return False
        else:
            return True

def whichTM():
    choice = raw_input("Which machine? (1, 2, 3, 4): ")
    if choice == "1":
        ## page 118
        transitionFunctions = {("q1","1"):("q1","1", "R"),
                       ("q1","0"):("q2"," ", "R"),
                       ("q1"," "):("qr"," ",""),
                       ("q2","1"):("q2","1", "R"),
                       ("q2","0"):("q3"," ", "L"),
                       ("q2"," "):("ha"," ", "N"),
                       ("q3","1"):("q3","1", "L"),
                       ("q3","0"):("q3","0", "L"),
                       ("q3"," "):("q1"," ", "R"),
                       }
    if choice == "2":
        ## page 119
        transitionFunctions = {("q1","#"):("q1", "#", "R"),
                        ("q1","1"):("q2", "1", "N"),
                        ("q1","0"):("q2", "0", "R"),
                        ("q1"," "):("ha", " ", "N"),
                        ("q2","#"):("q2", "#", "R"),
                        ("q2","1"):("q6", "1", "R"),
                        ("q2","0"):("q3", "#", "R"),
                        ("q2"," "):("q6", " ", "L"),
                        ("q3","#"):("q2", "#", "R"),
                        ("q3","0"):("q2", "0", "R"),
                        ("q3","1"):("q4", "#", "R"),
                        ("q3"," "):("qr", " ", "N"),
                        ("q4","#"):("q2", "#", "R"),
                        ("q4","1"):("q3", "1", "R"),
                        ("q4","0"):("q5", "0", "R"),
                        ("q4"," "):("q6", " ", "L"),
                        ("q5","#"):("q5", "#", "R"),
                        ("q5","1"):("q2", "1", "R"),
                        ("q5","0"):("q4", "#", "R"),
                        ("q5"," "):("qr", " ", "N"),
                        ("q6","#"):("q6", "#", "L"),
                        ("q6","1"):("q6", "1", "L"),
                        ("q6","0"):("q6", "0", "L"),
                        ("q6"," "):("q1", " ", "R"),
                       }
    if choice == "3":
        ## page 120
        transitionFunctions = {("q1","1"):("q2", "1", "L"),
                        ("q1","0"):("q3", "$", "R"),
                        ("q1"," "):("ha", " ", "N"),
                        ("q1","$"):("qr", "$", "N"),
                        ("q2","$"):("q2", "0", "L"),
                        ("q2"," "):("q2", " ", "R"),
                        ("q2","1"):("qr", "1", "N"),
                        ("q2","0"):("qr", "0", "N"),
                        ("q3","0"):("q3", "0", "R"),
                        ("q3","1"):("q4", "1", "R"),
                        ("q3"," "):("qr", " ", "N"),
                        ("q3","$"):("qr", "$", "N"),
                        ("q4","1"):("q4", "1", "R"),
                        ("q4"," "):("q5", " ", "L"),
                        ("q4","0"):("qr", "0", "N"),
                        ("q4","$"):("qr", "$", "N"),
                        ("q5","1"):("q2", " ", "L"),
                        ("q5"," "):("qr", " ", "N"),
                        ("q5","$"):("qr", "$", "N"),
                        ("q5","0"):("qr", "0", "N"),
                        ("q6","1"):("q6", "1", "L"),
                        ("q6","0"):("q6", "0", "L"),
                        ("q6","$"):("q1", "$", "R"),
                        ("q6"," "):("qr", " ", "N"),
                       }
    if choice == "4":
        ## page 121
        transitionFunctions = {("q1","x"):("q5", "x", "R"),
                       ("q1","0"):("q2", " ", "R"),
                       ("q1"," "):("qr", " ", "N"),
                       ("q1","1"):("qr", "1", "N"),
                       ("q1","2"):("qr", "2", "N"),
                       ("q2","x"):("q2", "x", "R"),
                       ("q2","0"):("q2", "0", "R"),
                       ("q2","1"):("q3", "x", "R"),
                       ("q2","2"):("qr", "2", "N"),
                       ("q2"," "):("qr", " ", "N"),
                       ("q3","x"):("q3", "x", "R"),
                       ("q3","1"):("q3", "1", "R"),
                       ("q3","2"):("q4", "x", "R"),
                       ("q3"," "):("qr", " ", "N"),
                       ("q3","0"):("qr", "0", "N"),
                       ("q4","x"):("q4", "x", "L"),
                       ("q4","1"):("q4", "1", "L"),
                       ("q4","0"):("q4", "0", "L"),
                       ("q4"," "):("q1", " ", "R"),
                       ("q4","2"):("qr", "2", "N"),
                       ("q5","x"):("q5", "x", "R"),
                       ("q5"," "):("ha", " ", "N"),
                       ("q5","1"):("qr", "1", "N"),
                       ("q5","0"):("qr", "0", "N"),
                       ("q5","2"):("qr", "2", "N")
                       } 
    if choice != "1" and choice != "2" and choice != "3" and choice != "4":
        print("Not a valid pre-defined TM.")
        sys.exit()

    return transitionFunctions

initialState = "q1"
finalStates = ["ha","qr"]
transitionFunctions = whichTM()
string = raw_input("Enter string you which to simulate: ")
t = TuringMachine(string+" ", initialState = initialState, finalStates = finalStates, transitionFunction=transitionFunctions)

print("Input tape:")
t.showTape()
print("======================")
print("State\tString\tHeadLoc")
print("======================")

while not t.final():
    t.step()

print("Result:")    
t.showTape()
if t.accept() == False:
    print("String is not accepted. (Note that string is not rejected, simply not accepted.)")
