import unittest

from ..Konto import Konto


imie = "asdf"
nazwisko = "fdas"
pesel = "12345678910"
class TestHistoria(unittest.TestCase):
    def test_historia_przelew_zwykly(self):
        konto = Konto(imie, nazwisko, pesel)
        konto.zaksieguj_przelew_przychodzacy(500)
        konto.zaksieguj_przelew_wychodzacy(500)
        konto.zaksieguj_przelew_przychodzacy(500)
        konto.zaksieguj_przelew_wychodzacy(500)
        konto.zaksieguj_przelew_wychodzacy(500)
        self.assertEqual(konto.historia, [500, -500, 500, -500], 'Historia nie została odpowiednio zapisana!')

    def test_historia_przelew_ekspress(self):
        konto = Konto(imie, nazwisko, pesel)
        konto.saldo = 500
        konto.zaksieguj_przelew_ekspresowy(500)
        self.assertEqual(konto.historia, [-500, -konto.oplata_za_ekspres], 'Historia nie została odpowiednio zapisana!')
