from functions import *

print('3. feladat: CB-Rádió')

FajlBeolvasas()

print(f'3.2 feladat: Bejegyzések száma: {len(cbAdasok)} db')

print(f'3.3 feladat: Sanyihoz tartozó bejegyzések: {Sanyi()} db')

print('3.4 feladat: A legtöbb adás:')
for item in cbAdasok:
    if item.Darab==MaxDb():
        print(f'\tIdő: {item.Ora}:{item.Perc} Darab: {item.Darab} Név: {item.Nev}')

FajlbaIras()