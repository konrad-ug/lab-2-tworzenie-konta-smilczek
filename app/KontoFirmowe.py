from app.Konto import Konto


class KontoFirmowe(Konto):
    def __init__(self, nazwa_firmy, nip):
        self.nazwa_firmy = nazwa_firmy
        self.nip = nip if self.czy_poprawny_nip(nip) else "Niepoprawny NIP!"
        self.saldo = 0
        self.oplata_za_ekspres = 5
        self.historia = []

    def czy_poprawny_nip(self, nip):
        return len(nip) == 10

    def kredyt_zasluzony(self, kwota):
        if -1755 in self.historia:
            if self.saldo >= kwota * 2:
                return True
        return False
    
    def zaciagnij_kredyt(self, kwota):
        if self.kredyt_zasluzony(kwota):
            self.saldo += kwota
            return True
        return False