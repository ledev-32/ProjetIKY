import random
import os

happy = ["joyeux", "heureux", "en forme"]
happier = ["Oh cool ça et pourquoi est tu heureux"]
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "'", ",", "."]
output = open("output.txt", "w+", encoding='utf-8')


print("Salut je m'appelle Sae")
print("Tu ne me connais pas encore mais je pense qu'on va bien s'entendre")


name = input("Comment t'appelles tu ? ")
output.write("Name : ")
output.write(name)
output.write('\n')


print("C'est un très joli prénom ", name)
age = input("mais dis moi, quel age à tu ? ")




new_age = int(age)
output.write("Age : ")
output.write(age)
output.write('\n')
if new_age < 0:
    print("Comment est ce possible, tu as un age si petit que mon cerveau ne peut pas te trouver")
    exit()
elif new_age < 18:
    print("Tu es encore mineur, je ne sais pas si j'ai le droit de discuter avec toi")
    output.write("Statut : Mineur")
    output.write('\n')
elif new_age >= 18:
    print("Tu es majeur, tu possède plus de droits que les mineurs, je parle des enfants ahahah")
    output.write("Statut : Majeur")
    output.write('\n')
