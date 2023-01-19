from data import *

def FajlBeolvasas():
    f=open('cb.txt','r',encoding='utf-8')
    f.readline()
    for sor in f:
        cbAdasok.append(CBadás(sor))
    f.close()

def Sanyi():
    db=0
    for item in cbAdasok:
        if item.Nev=='Sanyi':
            db+=1
    return db

def MaxDb():
    max=0
    for item in cbAdasok:
        if item.Darab>max:
            max=item.Darab
    return max

def FajlbaIras():
    f=open('cb2.txt','w',encoding='utf-8')
    f.write('Kezdes;Nev;AdasDb\n')
    for item in cbAdasok:
        f.write(f'{item.Ora*60+item.Perc};{item.Nev};{item.Darab}\n')
    f.close()