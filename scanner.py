import enum
from helper import isDigit, isLetter, isSpace, isSpecialSymbol
class States(enum.Enum):
    START = 1
    INCOMMENT = 2
    INNUM = 3
    INID = 4
    INASSIGN = 5
    DONE = 6
    ERROR = 7
class Scanner():
    charPointer = 0
    def getToken(self, tinyCode):
        state = States.START
        numToken = ""
        idToken = ""
        assignToken = ""
        symbolToken = ""
        while state is not States.DONE:
            if state is States.START:
                if isSpace(tinyCode[self.charPointer]):
                    self.charPointer += 1
                    continue
                elif tinyCode[self.charPointer] == '{':
                    self.charPointer += 1
                    state = States.INCOMMENT
                    continue
                elif isDigit(tinyCode[self.charPointer]):
                    numToken += str(tinyCode[self.charPointer])
                    self.charPointer += 1
                    state = States.INNUM
                    continue
                elif isLetter(tinyCode[self.charPointer]):
                    idToken += tinyCode[self.charPointer]
                    self.charPointer += 1
                    state = States.INID
                    continue
                elif tinyCode[self.charPointer] == ':':
                    self.charPointer += 1
                    state = States.INASSIGN
                    continue
                elif isSpecialSymbol(tinyCode[self.charPointer]):
                    symbolToken = tinyCode[self.charPointer]
                    self.charPointer += 1
                    state = States.DONE
                    continue
                else:
                    state = States.ERROR
                    continue
            elif state is States.INCOMMENT:
                self.charPointer += 1
                if tinyCode[self.charPointer] != '}':
                    continue
                else:
                    state = States.START
                    continue
            elif state is States.INNUM:
                if isDigit(tinyCode[self.charPointer]):
                    numToken += str(tinyCode[self.charPointer])
                    self.charPointer += 1
                    continue
                else:
                    self.charPointer += 1
                    state = States.DONE
                    continue
            elif state is States.INID:
                if isLetter(tinyCode[self.charPointer]):
                    idToken += tinyCode[self.charPointer]
                    self.charPointer += 1
                    continue
                else:
                    self.charPointer += 1
                    state = States.DONE
                    continue
            elif state is States.INASSIGN:
                if tinyCode[self.charPointer] == '=':
                    assignToken = ':='
                    self.charPointer += 1
                    state = States.DONE
                    continue
                else:
                    self.charPointer += 1
                    state = States.DONE
                    continue
            elif state is States.DONE:
                if numToken != "":
                    return numToken
                elif idToken != "":
                    return idToken
                elif symbolToken != "":
                    return symbolToken
                elif assignToken != "":
                    return assignToken
            elif state is States.ERROR:
                self.charPointer = 0
                return "Error!"