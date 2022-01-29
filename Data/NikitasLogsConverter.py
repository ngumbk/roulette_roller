import re

file1 = open('result_1_bet.txt', 'r')
file3 = open('newresult_1_bet.txt', 'a+')

while True:
    resStr = ""
    line2 = file1.readline()
    match = re.findall(r'C.+\WP:\w\W', line2)
    resStr += match[0][0:len(match[0]) - 1]

    resStr += "|"

    match = re.findall(r'W.+', line2)
    resStr += match[0]

    resStr += '\n'
    file3.write(resStr)

    print(resStr)
