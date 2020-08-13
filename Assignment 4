import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

tags = soup('a')
link = ''
for n in range(count):
    link = str(tags[pos - 1]).split('"')
    http = urllib.request.urlopen(link[1], context=ctx).read()
    bsoup = BeautifulSoup(http, 'html.parser')
    tags = bsoup('a')
    print(link[1])

'This is the link for the file: http://py4e-data.dr-chuck.net/known_by_Wiktorja.html. This will be put in input. count = 7 and pos = 18. The last name starts with a G.'
