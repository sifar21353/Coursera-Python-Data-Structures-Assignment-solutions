import re

hand = open('http:py4e-data.dr-chuck.netregex_sum_701204.txt')
lis = list()

for line in hand:
    a = re.findall('[0-9]+', line)
    if a == []:
        continue
    else:
        for i in a:
            lis.append(int(i))
            
print(sum(lis))

' This is the link to this file - http:py4e-data.dr-chuck.netregex_sum_701204.txt. http://py4e-data.dr-chuck.net/regex_sum_701204.txt '
