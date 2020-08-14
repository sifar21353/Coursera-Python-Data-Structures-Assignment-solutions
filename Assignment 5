import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
input = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_701208.xml')

s = 0
for line in input:
    line = str(line).strip()
    line = line.split('b')
    line.remove('')
    if 'count' in line[0]:
        spl = line[0].split('>')
        spl2 = spl[1].split('<')
        s += int(spl2[0])

print(s)
