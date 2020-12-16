from scanner import Scanner
f = open("tiny_snippet.txt", "r")
tinyCode = ""
for line in f:
    tinyCode += line
# print(tinyCode)
scanner = Scanner()
for index in range(len(tinyCode)):
    token = scanner.getToken(tinyCode)
    if token is not None:
        print(token)
# token1 = scanner.getToken(tinyCode)
# token2 = scanner.getToken(tinyCode)
# token3 = scanner.getToken(tinyCode)
# print(token1)
# print(token2)
# print(token3)