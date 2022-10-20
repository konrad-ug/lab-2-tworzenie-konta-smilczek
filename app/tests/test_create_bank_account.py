import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        imie = "dariusz"
        nazwisko = "januszewski"
        pesel = "12345678910"
        pierwsze_konto = Konto(imie, nazwisko, pesel)
        self.assertEqual(pierwsze_konto.pesel, pesel, "Pesel nie został zapisany!")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Pesel nie posiada odpowiedniej liczby znaków!")
        self.assertEqual(pierwsze_konto.imie, imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    #tutaj proszę dodawać nowe testy
