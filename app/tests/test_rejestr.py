import unittest
from parameterized import parameterized

from ..RejestrKont import RejestrKont
from ..Konto import Konto

imie = "dariusz"
nazwisko = "januszewski"
pesel = "65345678910"

imie2 = "Maciek"
nazwisko2 = "Kowalski"
pesel2 = "69345612377"

class TestRejestr(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        RejestrKont.dodaj_konto(Konto(imie, nazwisko, pesel))
    
    @classmethod
    def tearDownClass(cls):
        RejestrKont.konta = []

    # def test_1_dodawanie_pierwszego_konta(self):
    #     konto = Konto(imie, nazwisko, pesel)
    #     RejestrKont.dodaj_konto(konto)
    #     self.assertEqual(RejestrKont.ile_kont(), 1)
        
    def test_2_dodawanie_drugiego_konta(self):
        konto = Konto(imie, nazwisko, pesel)
        RejestrKont.dodaj_konto(konto)
        self.assertEqual(RejestrKont.ile_kont(), 2)
        
    def test_3_szukanie_konta(self):
        konto = Konto(imie2, nazwisko2, pesel2)
        RejestrKont.dodaj_konto(konto)
        self.assertEqual(RejestrKont.wyszukaj_konto_z_peselem(pesel2), konto)