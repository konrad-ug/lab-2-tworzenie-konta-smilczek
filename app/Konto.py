class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko

        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"

        self.saldo = 0
        if kod_rabatowy:
            if kod_rabatowy == "PROM_XYZ":
                if int(pesel[:2]) > 60:
                    self.saldo += 50
