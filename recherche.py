import time                     #
import random                   #
import math                     #
import os                       # Importation des modules nécessaires au bon fonctionnement de IKY
import getpass                  #
from googlesearch import search #
import requests                 #
from bs4 import BeautifulSoup   #
import re       

query = "tir à l'arc"
links = []
inter_one = open("inter_one.txt", "w", encoding="utf-8")
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    links.append(j)
    inter_one.write(j)
    inter_one.write('\n')
print(links[0])
url = str(links[0]) 

output = open("output_codex.txt", 'w', encoding='utf-8')
inter_two = open("inter_two.txt", "w+", encoding='utf-8')

request = requests.get(url, 'lxml')
output.write(request.text)
output.close()

soup = BeautifulSoup(request.text, 'html.parser')
research = soup.find_all("h1")
inter_two.write(str(research))

print("Tout les titres balisés h1 sont : ", research)

n = 0
chase = []
character = ""

while n < len(research):
    termedone = str(research[n])            # Avec index
    character = character + termedone             #
    if termedone == "/":                  #
        chase.append(character)          #
        character = ""                     #
    print(termedone)
    n += 1                         #

print(chase)
