import unittest

from ..Konto import Konto

imie = "dariusz"
nazwisko = "januszewski"
pesel = "12345678910"
n_pesel = "1234"
rok_ur = "1965"
n_rok_ur = "1960"
kod_rabatowy = "PROM_XYZ"
n_kod_rabatowy = "PROM_ZYX"
class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(imie, nazwisko, pesel, rok_ur)
        self.assertEqual(pierwsze_konto.imie, imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        

    #tutaj proszę dodawać nowe testy
        self.assertEqual(pierwsze_konto.rok_ur, rok_ur, "Rok urodzenia nie został zapisany!")
        self.assertEqual(pierwsze_konto.pesel, pesel, "Pesel nie został zapisany!")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Pesel nie posiada odpowiedniej liczby znaków!")
        
    def test_pesel(self):
        pierwsze_konto = Konto(imie, nazwisko, n_pesel, rok_ur)
        self.assertEqual(pierwsze_konto.pesel, "Niepoprawny pesel!", "Pesel nie został poprawnie sprawdzony w konstruktorze")

    def test_kod_rabatowy(self):
        pierwsze_konto = Konto(imie, nazwisko, pesel, rok_ur, kod_rabatowy)
        self.assertEqual(pierwsze_konto.saldo, 50, "Kod rabatowy został niepoprawnie sprawdzony!")
        drugie_konto = Konto(imie, nazwisko, pesel, rok_ur, n_kod_rabatowy)
        self.assertEqual(drugie_konto.saldo, 0, "Kod rabatowy został niepoprawnie sprawdzony!")

        trzecie_konto = Konto(imie, nazwisko, pesel, n_rok_ur, kod_rabatowy)
        self.assertEqual(trzecie_konto.saldo, 0, "Wiek nie został poprawnie sprawdzony!")
