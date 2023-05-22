class tamagotchi:
    # nev: str
    # karakter: str
    # ehseg: int
    # elet: int 
    # kedv: int 

    def __init__(self, sor) -> None:
        adatok = sor.split(';')
        self.nev = adatok[0]
        self.karakter = adatok[1]
        self.ehseg = int(adatok[2])
        self.elet = int(adatok[3])
        self.kedv = int(adatok[4])

    @property
    def név(self):
        return self.nev
    
    @property
    def kar(self):
        return self.karakter
    
    @property
    def éhség(self):
        return self.ehseg
    
    @property
    def élet(self):
        return self.elet
    
    @property
    def kedvv(self):
        return self.kedv