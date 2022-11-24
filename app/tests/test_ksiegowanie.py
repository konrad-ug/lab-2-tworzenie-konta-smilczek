import unittest

from ..Konto import Konto


imie = "Darek"
nazwisko = "Kowalski"
pesel = "66041739457"
class TestKsiegowanie(unittest.TestCase):
    def test_udany_przelew_wychodzacy(self):
        konto = Konto(imie, nazwisko, pesel)
        konto.saldo = 1000
        konto.zaksieguj_przelew_wychodzacy(1000)
        self.assertEqual(konto.saldo, 0, "Przelew nie został zaksięgowany")

    def test_udany_przelew_przychodzacy(self):
        konto = Konto(imie, nazwisko, pesel)
        konto.zaksieguj_przelew_przychodzacy(1000)
        self.assertEqual(konto.saldo, 1000, "Przelew nie został zaksięgowany")
