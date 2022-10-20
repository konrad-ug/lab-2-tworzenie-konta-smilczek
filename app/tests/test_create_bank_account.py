import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        imie = "dariusz"
        nazwisko = "januszewski"
        pesel = "12345678910"
        n_pesel = "1234"
        kod_rabatowy = "PROM_XYZ"
        n_kod_rabatowy = "PROM_ZYX"

        pierwsze_konto = Konto(imie, nazwisko, pesel)
        self.assertEqual(pierwsze_konto.imie, imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        

    #tutaj proszę dodawać nowe testy
        self.assertEqual(pierwsze_konto.pesel, pesel, "Pesel nie został zapisany!")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Pesel nie posiada odpowiedniej liczby znaków!")
        
    def test_pesel:
        pierwsze_konto = Konto(imie, nazwisko, n_pesel)
        self.assertEqual(pierwsze_konto.pesel, "Niepoprawny pesel!", "Pesel nie został poprawnie sprawdzony w konstruktorze")

    def test_kod_rabatowy
        drugie_konto = Konto(imie, nazwisko, n_pesel, kod_rabatowy)
        self.assertEqual(drugie_konto.saldo, 50, "Kod rabatowy został niepoprawnie sprawdzony!")

        trzecie_konto = Konto(imie, nazwisko, pesel, n_kod_rabatowy)
        self.assertEqual(trzecie_konto.saldo, 0, "Kod rabatowy został niepoprawnie sprawdzony!")
