"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Hana Šimečková
email: simeckova.hana8@gmail.com
discord: Hanka Š.

"""

TEXTS = ['''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
] 

dekorace1 = "-" * 40
dekorace2 = "-" * 23

#ověření uživatele
uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123" }
jmeno = input("Zadejte své jméno: ")
heslo = input("Zadejte své helo: ")

if jmeno in uzivatele and uzivatele[jmeno] == heslo:
    print("Vítej", jmeno, "!")

else:
    print("Neregistrovaný uživatel! Ukončuji program...")
    quit()


#výběr textu
vyber = input("Vyberte jeden ze tří textů.")
if vyber.isnumeric and int(vyber) in range(1,4):
    print("Bude analyzován text č.", vyber)
    print(dekorace1)
    vyber = int(vyber)
else:
    print("Špatný výběr!")
    quit()


#analýza textu
seznam_objektu = list()

import re
for slovo in (vybrany_text := re.split(" |-|\n",TEXTS[vyber-1])):
    seznam_objektu.append(slovo.strip(".,"))


#rozdělení
cisla = list()
slova= list()
for objekt in seznam_objektu:
    if objekt.isnumeric():
        cisla.append(int(objekt))

    #elif objekt.isalpha():
    #    slova.append(objekt)
    
    else:
        slova.append(objekt)

title_words = list()
lower_words = list()
upper_words = list()

for slovo in slova:
    if slovo.istitle():
      title_words.append(slovo)
    
    elif slovo.islower():
        lower_words.append(slovo)

    elif slovo.isupper():
        upper_words.append(slovo)


print(
f"There are {len(seznam_objektu)} words in the selected text.",
f"There are {len(title_words)} titlecase words.",
f"There are {len(upper_words)} uppercase words.",
f"There are {len(lower_words)} lowercase words.",
f"There are {len(cisla)} numeric strings.",
f"The sum of all numbers: {sum(cisla)}",
dekorace1,
sep= "\n"
)


#četnost délek různých slov v textu
delky_slov = list()
for word in slova:
    delky_slov.append(len(word))

serazeno = sorted(delky_slov)

pocty_cislic = {}
for cislice in serazeno:
    if not cislice in pocty_cislic:
        pocty_cislic[cislice] = 0
    pocty_cislic[cislice] += 1 

#Výstup graf
hvezda = "*"
print(f"LEN|  OCCURENCES   |NR.",
        dekorace2,
        sep= "\n")
for udaj in pocty_cislic:
    print(
        f"{udaj: ^3}|{pocty_cislic[udaj] * hvezda: <15}|{pocty_cislic[udaj]}",
        dekorace2,
        sep = "\n"
    )