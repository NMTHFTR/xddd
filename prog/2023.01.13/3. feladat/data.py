class CBadás:
    def __init__(self,sor:str):
        adatok=sor.strip().split(';')
        self.Ora=int(adatok[0])
        self.Perc=int(adatok[1])
        self.Darab=int(adatok[2])
        self.Nev=adatok[3]

cbAdasok:list[CBadás]=[]