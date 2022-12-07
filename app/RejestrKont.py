from app.Konto import Konto

class RejestrKont():
    konta = []
    # def __init__(self):
    #     konta = []

    @classmethod
    def dodaj_konto(cls, konto):
        if cls.wyszukaj_konto_z_peselem(konto.pesel):
            return False
        cls.konta.append(konto)
        return True
    
    @classmethod
    def wyszukaj_konto_z_peselem(cls, pesel):
        for konto in cls.konta:
            if (konto.pesel == pesel):
                return konto
        return None
    
    @classmethod
    def ile_kont(cls):
        return len(cls.konta)

    @classmethod
    def edytuj_konto(cls, dane, pesel):
        konto = cls.wyszukaj_konto_z_peselem(pesel)
        if (dane['imie']):
            konto.imie = dane['imie']
        if (dane['nazwisko']):
            konto.nazwisko = dane['nazwisko']
        if (dane['pesel']):
            konto.pesel = dane['pesel']
        if (dane['saldo']):
            konto.saldo = dane['saldo']

    @classmethod
    def usun_konto(cls, pesel):
        for konto in cls.konta:
            if konto.pesel == pesel:
                cls.konta.remove(konto)
                return