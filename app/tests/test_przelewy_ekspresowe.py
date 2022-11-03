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

