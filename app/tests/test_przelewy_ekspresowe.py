import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe


imie = "asdf"
nazwisko = "fdas"
pesel = "12345678910"
nazwa_firmy = "asdf sdf gd.sd"
nip = "1234567890"
class TestKsiegowaniePrzelewow(unittest.TestCase):
    def test_udany_przelew_ekspresowy(self):
        konto = Konto(imie, nazwisko, pesel)
        konto.saldo = 1000
        konto.zaksieguj_przelew_ekspresowy(300)
        self.assertEqual(konto.saldo, 1000 - 300 - 1, "Przelew ekspresowy nie został zaksięgowany")

    def test_nieudany_przelew_ekspresowy(self):
        konto = Konto(imie, nazwisko, pesel)
        konto.saldo = 1000
        konto.zaksieguj_przelew_ekspresowy(1000)
        self.assertEqual(konto.saldo, -1, "Przelew nie został poprawnie sprawdzony")

    def test_udany_przelew_eksresowy_konto_firmowe(self):
        konto = KontoFirmowe(nazwa_firmy, nip)
        konto.saldo = 1000
        konto.zaksieguj_przelew_ekspresowy(300)
        self.assertEqual(konto.saldo, 1000 - 300 - 5, "Przelew ekspresowy nie został zaksięgowany")

    def test_nieudany_przelew_ekspresowy_konto_firmowe(self):
        konto = KontoFirmowe(nazwa_firmy, nip)
        konto.saldo = 1000
        konto.zaksieguj_przelew_ekspresowy(1000)
        self.assertEqual(konto.saldo, -5, "Przelew nie został poprawnie sprawdzony")
