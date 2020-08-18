import urllib.request, urllib.parse, urllib.error
input = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_701209.json')
l = list()
for line in input:
    if line.decode().strip().startswith('"count"'):
        a = line.decode().strip().split()
        b = a[0].split(':')
        l.append(int(b[1]))
print(sum(l))
