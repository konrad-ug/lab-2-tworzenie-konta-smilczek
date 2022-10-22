class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko
        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"

        if kod_rabatowy:
            if kod_rabatowy == "PROM_XYZ":
                self.saldo = 50
            else:
                self.saldo = 0
        else:
            self.saldo = 0
