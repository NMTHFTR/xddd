from data import *

def FajlBeolvasas():
    f=open('legmagasabb.txt','r',encoding='utf-8')
    f.readline()
    for sor in f:
        epuletek.append(Épület(sor))
    f.close()

def EmeletOsszeg():
    osszeg=0
    for item in epuletek:
        osszeg+=item.Emeletek
    return osszeg   

def Legmagasabb():
    maxPoz=0
    for i in range(len(epuletek)):
        if epuletek[i].Magassag>epuletek[maxPoz].Magassag:
            maxPoz=i
    return maxPoz

def Olasz():
    for item in epuletek:
        if item.Orszag=='Olaszország':
            return True
    return False

