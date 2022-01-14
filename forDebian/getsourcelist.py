
# get all source list in debian.org
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

req = Request("https://www.debian.org/mirror/list")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))
out = ""
for link in links:
    if link.startswith('http') and link.find("/debian") != -1:
        out = out + link + "\n"
with open("downloadSource.txt", "w") as output:
    output.write(out)