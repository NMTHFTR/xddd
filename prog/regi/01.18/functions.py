from data import *

def FajlBeolvas():
    file = open("fob2016.txt", 'r', encoding="utf-8")
    for sor in file:
        versenyzok.append(Versenyzo(sor))
    file.close()

def NoiVersenyzok():
    noiDb = 0
    for item in versenyzok:
        if item.Kategoria == "Noi":
            noiDb += 1
    return noiDb / len(versenyzok) * 100

def NoiBajnok():
    bajnokPoz = 0
    for i in range(len(versenyzok)):
        if versenyzok[i].Kategoria == "Noi" and versenyzok[i].Osszpont() > versenyzok[bajnokPoz].Osszpont():
            bajnokPoz = i
    return bajnokPoz

def FerfiPontok():
    file = open("osszpontFF.txt", 'w', encoding="utf-8")
    for item in versenyzok:
        if item.Kategoria == "Felnott ferfi":
            file.write(f"{item.Nev};{item.Osszpont()}\n")
    file.close()

def Statisztika():
    stat = {}
    for item in versenyzok:
        if item.Egyesulet != "n.a.":
            if item.Egyesulet in stat.keys():
                stat[item.Egyesulet] += 1
            else:
                stat[item.Egyesulet] = 1

    # képernyőre
    for key, value in stat.items():
        if value > 2:
            print(f"\t{key} - {value}")
    
    # fájlba
    file = open("statisztika.txt", 'w', encoding="utf-8")
    for key, value in stat.items():
        if value > 2:
            file.write(f"{key} - {value}\n")
    file.close()