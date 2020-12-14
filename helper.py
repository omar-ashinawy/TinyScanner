A = 65
Z = 90
a = 97
z = 122
def isDigit(char_token):
    if char_token >= 0 and char_token <= 9:
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