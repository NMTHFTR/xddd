from functions import *

FajlBeolvasas()
print(f'3.2 feladat: Épületek száma: {len(epuletek)} db')

print(f'3.3 feladat: Emeletek összege: {EmeletOsszeg()}')

print('3.4 feladat: A legmagasabb épület adatai')
print(f'\tNév: {epuletek[Legmagasabb()].Nev}')
print(f'\tVáros: {epuletek[Legmagasabb()].Varos}')
print(f'\tOrszág: {epuletek[Legmagasabb()].Orszag}')
print(f'\tMagasság: {epuletek[Legmagasabb()].Magassag}')
print(f'\tEmeletek száma: {epuletek[Legmagasabb()].Emeletek}')
print(f'\tÉpítés éve: {epuletek[Legmagasabb()].Epult}')

if Olasz():
    print(f'3.5 feladat: Van olasz épület az adatok között!')
else:
    print(f'3.5 feladat: Nincs olasz épület az adatok között!')
