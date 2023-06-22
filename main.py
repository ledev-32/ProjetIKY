import time                     #
import random                   #
import math                     #
import os                       # Importation des modules nécessaires au bon fonctionnement de IKY
import getpass                  #
from googlesearch import search #
import requests                 #
from bs4 import BeautifulSoup   #
import re                       #

def transfo(x):                         #  
    check = str(x)                      #
    if len(check) == 2:
        return 0
    check1 = check.rstrip(check[-1])    #
    check2 = check1.rstrip(check1[-1])  # Fonction : suppression des crochets + \n 
    check3 = check2.rstrip(check2[-1])  # Entrée : str
    check4 = check3.rstrip(check3[-1])  # Sortie : str
    check5 = check4[1:]                 #
    final = check5[1:]                  #
    return final                        #


psw = getpass.getpass('Password: ')     # Demande à l'utilisateur de renseigner le mot de passe

def check(psw):                                 #
    if (psw == "AAAA"):                         #
        return "good!"                          # Fonction : Permet la vérification du mot de passe
    else:                                       #
        print("This is not the good password")  #
        exit()                                  #

print(check(psw))

#print(str(research))
"""
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
"""

happy = open("happy.txt", "r+", encoding="utf-8")       #
angry = open("angry.txt", "r+", encoding="utf-8")       # Défintion des ouvertures de fichiers
sad = open("sad.txt", "r+", encoding="utf-8")           # Mode d'ouverture : lecture + écriture
surprise = open("surprise.txt", "r+", encoding="utf-8") #

happier = []
angryier = []
sadier = []
surpriseier = []

ver = 0
while ver < 1:
    element = transfo(str(happy.readlines(1)))
    if element == 0:
        ver += 1
    else:
        happier.append(element)

ver = 0
while ver < 1:
    element = transfo(str(surprise.readlines(1)))
    if element == 0:
        ver += 1
    else:
        surpriseier.append(element)

ver = 0
while ver < 1:
    element = transfo(str(angry.readlines(1)))
    if element == 0:
        ver += 1
    else:
        angryier.append(element)

ver = 0
while ver < 1:
    element = transfo(str(sad.readlines(1)))
    if element == 0:
        ver += 1
    else:
        sadier.append(element)


main = 0
while main < 1:

    n = 0                   #
    index = 0               # Initialisation
    main = 0                #

    print("facial : facial (indisponible)")
    print("Hash22 : hash (indisponible)")
    print("SAE : sae (indisponible)")
    print("IKYSM : IKYSM (indisponible)")
    request = input("Que souhaites-tu ? ")   # On pose la question initiale

    chest = ""                                 #
    new_str = []                               # On définit les variables pour le stock de la réponse

    while index < len(request):            # Boucle de séparation des mots
        inter1 = request[index]            # Avec index
        chest = chest + inter1             #
        if inter1 == " ":                  #
            new_str.append(chest)          #
            chest = ""                     #
        index += 1                         #

    #print(new_str)

    n = 0                   #
    index = 0               # Re-initialisation

    main = 0                #

    while index < len(new_str):             # Boucle de suppression de l'espace
        rem1 = str(new_str[index])          # Avec index
        rem2 = rem1.rstrip(rem1[-1])
        index2 = 0

        if rem2 == "exit":
            exit()
        elif rem2 == "facial":
            os.system("python facial.py")
        elif rem2 == "sae":
            os.system("python SAE.py")
        elif rem2 == "hash":
            os.system("python hash22.py")
        elif rem2 == "again":
            os.system("start starter.bat")

        #while index2 < len(happier):
            #print(rem2)
            #index2 += 1
            #if rem2 == happier[index2]:
                #print("YOUU AURE SO HAPPPPPPPPPPPPY")
                #break

        for i in range(0,len(happier)):
            che = happier[i]
            if rem2 == che:
                print("Oh cool ça et pourquoi es tu heureux")
        for i in range(0,len(surpriseier)):
            che = surpriseier[i]
            if rem2 == che:
                print("Quelle est la raison de ta surprise")
        for i in range(0,len(angryier)):
            che = angryier[i]
            if rem2 == che:
                print("And why you are surprised")
        for i in range(0,len(surpriseier)):
            che = surpriseier[i]
            if rem2 == che:
                print("And why you are surprised")
        index += 1

#os.remove("main.py") #permet de supprimer le fichier
