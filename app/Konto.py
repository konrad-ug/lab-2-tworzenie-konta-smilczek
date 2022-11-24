class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oplata_za_ekspres = 1
        self.historia = []

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
            self.historia.append(-kwota)

    def zaksieguj_przelew_przychodzacy(self, kwota):
        self.saldo += kwota
        self.historia.append(kwota)

    def zaksieguj_przelew_ekspresowy(self, kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota + self.oplata_za_ekspres
            self.historia.append(-kwota)
            self.historia.append(-self.oplata_za_ekspres)

    def kredyt_zasluzony(self, kwota):
        if len(self.historia) < 3:
            return False
        if self.historia[-1] > 0 and self.historia[-2] > 0 and self.historia[-3] > 0:
            return True
        if sum(self.historia[-5:]) >= kwota:
            return True
        return False

    def zaciagnij_kredyt(self, kwota):
        if self.kredyt_zasluzony(kwota):
            self.saldo += kwota
            return True
        return False
        