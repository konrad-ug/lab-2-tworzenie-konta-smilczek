class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oplata_za_ekspres = 1

        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"

        self.saldo = 0
        self.check_kod_rabatowy(kod_rabatowy)

    def check_kod_rabatowy(self, kod_rabatowy):
        if kod_rabatowy:
            if kod_rabatowy == "PROM_XYZ":
                if int(self.pesel[:2]) > 60:
                    self.saldo += 50

    def zaksieguj_przelew_wychodzacy(self, kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota

    def zaksieguj_przelew_przychodzacy(self, kwota):
        self.saldo += kwota

    def zaksieguj_przelew_ekspresowy(self, kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota + self.oplata_za_ekspres

