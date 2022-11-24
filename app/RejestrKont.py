from app.Konto import Konto

class RejestrKont():
    konta = []
    # def __init__(self):
    #     konta = []

    @classmethod
    def dodaj_konto(cls, konto):
        cls.konta.append(konto)
    
    @classmethod
    def wyszukaj_konto_z_peselem(cls, pesel):
        for konto in cls.konta:
            if (konto.pesel == pesel):
                return konto
    
    @classmethod
    def ile_kont(cls):
        return len(cls.konta)