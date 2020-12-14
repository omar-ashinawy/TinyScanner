A = 65
Z = 90
a = 97
z = 122
def isDigit(char_token):
    if char_token == "0" or char_token == "1" or char_token == "2" or char_token == "3" or char_token == "4" or char_token == "5" or char_token == "6" or char_token == "7" or char_token == "8" or char_token == "9":
        return True
    else:
        return False
def isLetter(char_token):
    if (ord(char_token) >= A and ord(char_token) <= Z) or (ord(char_token) >= a and ord(char_token) <= z):
        return True
    else:
        return False
def isSpace(char_token):
    if char_token == ' ' or char_token == '\t' or char_token == '\n':
        return True
    else:
        return False
def isSpecialSymbol(char_token):
    if char_token == '+' or char_token =='-' or char_token == '*' or char_token == '/' or char_token == '=' or char_token =='<' or char_token == '(' or char_token == ')' or char_token == ';':
        return True
    else:
        return False