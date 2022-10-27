from app.Konto import Konto


class KontoFirmowe(Konto):
    def __init__(self, nazwa_firmy, nip):
        self.nazwa_firmy = nazwa_firmy
        self.nip = nip if self.czy_poprawny_nip(nip) else "Niepoprawny NIP!"
        self.saldo = 0
        self.oplata_za_ekspres = 5

    def czy_poprawny_nip(self, nip):
        return len(nip) == 10
