from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
a = ' '
l = list()

tags = soup('span')
for tag in tags:
    tag = str(tag)
    a = re.findall('[0-9]+', tag)
    if a == []:
        continue
    else:
        l.append(float(a[0]))

print(sum(l))

'The link of the file is this : http://py4e-data.dr-chuck.net/comments_701206.html'
