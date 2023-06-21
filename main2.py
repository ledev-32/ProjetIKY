import time
import random
import math
import os
import getpass
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re
"""
psw = getpass.getpass('Password: ')
def check(psw):
    if (psw == "AAAA"):
        return "good!"
    else:
        print("This is not the good password")
        exit()
#os.remove("main.py")
print(check(psw))
query = "tir à l'arc"
links = []
inter_one = open("inter_one.txt", "w", encoding="utf-8")
for j in search(query, tld="co.in", num=10, stop=5, pause=2):
    links.append(j)
    inter_one.write(j)
    inter_one.write('\n')
print(links)
url = str(links[0])"""


inter_two = open("main.py", "r", encoding="utf-8")
rebuild = open("main2.py", "w", encoding="utf-8")
n = 0
t = 1
while n < 100:
    rem1 = (inter_two.read(10000))
    if rem1 == "":
        rebuild.write("\n")
        rebuild.write("ending = 'Génération' ")
        rebuild.write("\n")
        rebuild.write("print(ending)")
        n += 1000
    else:
        print(rem1)
        rebuild.write(rem1)
        rebuild.write('\n')
        n += 1

#os.system("cmd")
#os.system("exit")
os.system("python printing.py")

ending = 'Génération' 
print(ending)