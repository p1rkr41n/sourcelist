# -*- coding: utf-8 -*-
from sys import argv
from traceback import print_tb
import requests
from bs4 import BeautifulSoup
from requests.api import request
# from threading import Thread
# import threading
# import time

# request
import requests
try:
    packet = argv[1]
except:
    print("Usage: python3 onlineSearch.py <packet>")
    exit()
burp0_url = "https://pkg.kali.org:443/" + packet
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-GB,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1", "Cache-Control": "max-age=0"}
req = requests.get(burp0_url, headers=burp0_headers)
getter = ""
# print(req.text)
soup = BeautifulSoup(req.text, 'html.parser')
# print(soup.prettify())
print("[?] Starting")
for link in soup.find_all('a'):
    if link.get('href').startswith('http://http'):
        if (link.get('href').endswith('dsc'))==False:
            # print(link.get('href'))
            getter = link.get('href')
            break
if getter == "":
    print("[!] No link found")
    print("[?] Could you access to", burp0_url)
else:
    print("[+] Directory link: ", getter)
    
    new_burp0_url = getter
    req2 = requests.get(new_burp0_url, headers=burp0_headers)
    soup = BeautifulSoup(req2.text, 'html.parser')
    
    # print(soup)
    for link in soup.find_all('a'):
        if link.get('href').endswith('deb'):
            print("[+] Final link: " + getter + "/" + link.get('href'))
            exit()

    print("[!] No deb file found")
    print("[?] Could you access to", burp0_url)